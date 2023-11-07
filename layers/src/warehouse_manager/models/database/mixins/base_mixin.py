from typing import Any, List, Optional, Type, cast

from sqlalchemy import select
from sqlalchemy.engine import ScalarResult

from warehouse_manager.exceptions.database import AttributeNotFoundError, ModelNotFoundError
from warehouse_manager.models.database.mixins.base import Base
from warehouse_manager.models.database.mixins.session_mixin import SessionMixin


class BaseMixin(Base, SessionMixin):
    __abstract__ = True

    @classmethod
    def get(cls: Type[Base], id_: int) -> Optional[Base]:
        return cls.session.get(cls, id_)

    @classmethod
    def find_or_fail(cls: Type[Base], id_: int) -> Base:
        model = cls.get(id_)
        if model is None:
            raise ModelNotFoundError(cls.__name__, "id", id_)

        return model

    @classmethod
    def filter_by(cls: Type[Base], **kwargs: Any) -> ScalarResult:
        return cls().fill(**kwargs).session.scalars(select(cls).filter_by(**kwargs))

    @classmethod
    def all(cls: Type[Base]) -> Optional[List[Base]]:
        return cast(Optional[List[Base]], cls.session.scalars(select(cls)).all())

    def fill(self: Base, **kwargs: Any) -> Base:
        valid_keys = self.__mapper__.attrs.keys()
        for attr in kwargs.keys():
            if attr not in valid_keys:
                raise AttributeNotFoundError(attr, self.__class__.__name__)

            setattr(self, attr, kwargs[attr])

        return self

    def save(self: Base) -> Base:
        self.session.add(self)
        self.session.commit()
        return self

    @classmethod
    def create(cls: Type[Base], **kwargs: Any) -> Base:
        return cls().fill(**kwargs).save()

    def update(self: Base, **kwargs: Any) -> Base:
        return self.fill(**kwargs).save()

    def delete(self: Base) -> None:
        ...
