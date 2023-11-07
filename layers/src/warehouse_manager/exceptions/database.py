from typing import Any, Optional

from warehouse_manager.exceptions.base import CustomBaseException


class SessionDoesNotExistError(CustomBaseException):
    def __init__(self, session_name: Optional[str] = None, custom_message: Optional[str] = None) -> None:
        self._custom_message = custom_message
        self._default_message = "Session does not exist"

        if session_name:
            self._specific_message = f"{session_name!r} session does not exist"


class ModelNotFoundError(CustomBaseException):
    def __init__(
        self,
        model_name: Optional[str] = None,
        attr_name: Optional[str] = None,
        attr_value: Optional[Any] = None,
        custom_message: Optional[str] = None,
    ) -> None:
        self._custom_message = custom_message
        self._default_message = "Model was not found"

        if model_name and attr_name and attr_value:
            self._specific_message = (
                f"{model_name!r} model was not found with {attr_name!r} attribute with a value of {attr_value!r}"
            )


class AttributeNotFoundError(CustomBaseException):
    def __init__(
        self, attr_name: Optional[str] = None, model_name: Optional[str] = None, custom_message: Optional[str] = None
    ) -> None:
        self._custom_message = custom_message
        self._default_message = "Attribute not found"
        if attr_name and model_name:
            self._specific_message = f"{attr_name!r} attribute not found in {model_name!r} model"
