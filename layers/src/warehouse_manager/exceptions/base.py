from typing import Optional


# I named it 'CustomBaseException' instead of 'BaseException' as that is what the python built-in exception class is
# called, that 'Exception' inherits from
class CustomBaseException(Exception):
    _custom_message: Optional[str] = None
    _specific_message: Optional[str] = None
    _default_message: str = "An unexpected error has occurred"

    def __str__(self) -> str:
        if self._custom_message:
            return self._custom_message

        if self._specific_message:
            return self._specific_message

        return self._default_message
