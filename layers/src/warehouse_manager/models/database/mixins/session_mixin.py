from sqlalchemy.orm.session import Session

from warehouse_manager.exceptions.database import SessionDoesNotExistError
from warehouse_manager.utils.class_ import classproperty


class SessionMixin:
    _session = None

    @classmethod
    def set_session(cls, session: Session) -> None:
        if session is None:
            raise SessionDoesNotExistError(session)

        cls._session = session

    @classproperty
    def session(self) -> Session:
        return self._session
