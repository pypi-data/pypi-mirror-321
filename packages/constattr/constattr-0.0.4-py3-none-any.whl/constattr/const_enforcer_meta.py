from typing import Any

from constattr.exceptions import ConstAssignmentError


class ConstantEnforcerMeta(type):
    def __setattr__(cls, name: str, value: Any):
        if cls.__is_constant(name=name):
            raise ConstAssignmentError(f'You cannot set the constant {name} in class {cls.__name__}')
        super().__setattr__(name, value)

    @staticmethod
    def __is_constant(name: str):
        return name.isupper()
