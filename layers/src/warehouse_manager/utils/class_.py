from typing import Any, Callable


class classproperty(object):
    def __init__(self, fget: Callable[..., Any]):
        self.fget = fget

    def __get__(self, owner_self: object, owner_cls: object) -> object:
        return self.fget(owner_cls)
