"""
----------------------------------------------------------------------------------------------------
Written by Yovany Dominico Girón (y.dominico.giron@elprat.cat) for Ajuntament del Prat de Llobregat
----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
"""
from abc import abstractmethod
from typing import Union
from sqlalchemy.orm import Session

from nomenclators_archetype.domain.commons import BaseSimpleNomenclator, BaseNomenclator
from nomenclators_archetype.domain.mapper.commons import BaseSimpleNomenclatorMapper, BaseNomenclatorMapper
from nomenclators_archetype.infrastructure.db.commons import BaseSimpleNomenclator as BaseSimpleNomenclatorEntity
from nomenclators_archetype.infrastructure.db.commons import BaseNomenclator as BaseNomenclatorEntity

from nomenclators_archetype.domain.repository.commons import JpaRepository

from nomenclators_archetype.infrastructure.db.builders import QueryBuilderImpl

NomenclatorId = Union[int, str]


class BaseSimpleNomenclatorRepository(JpaRepository[BaseSimpleNomenclator, NomenclatorId, BaseSimpleNomenclatorEntity]):
    """BaseSimpleNomenclator Repository Class"""

    def __init__(self, session: Session):
        self._session = session

    def get_builder(self):
        return QueryBuilderImpl()

    def get_session(self):
        return self._session

    def get_mapper(self):
        return BaseSimpleNomenclatorMapper()

    @abstractmethod
    def get_peristence_model(self):
        """Get persistence class"""


class BaseNomenclatorRepository(JpaRepository[BaseNomenclator, NomenclatorId, BaseNomenclatorEntity]):
    """BaseNomenclator Repository Class"""

    def __init__(self, session: Session):
        self._session = session

    def get_builder(self):
        return QueryBuilderImpl()

    def get_session(self):
        return self._session

    def get_mapper(self):
        return BaseNomenclatorMapper()

    @abstractmethod
    def get_peristence_model(self):
        """Get persistence class"""
