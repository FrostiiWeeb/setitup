# standard library imports
from setuptools import setup, find_packages, Command, Extension

from typing import Callable, Dict, List, Any, Union, Tuple

# third party imports
...

# local imports
from .models import Attribute


class Setup:
    def __init__(self):
        self._attributes: Dict[str, Attribute] = {}

    def attribute(self, name: str) -> Callable[[Callable], Attribute]:
        def decorator(func: Callable[[], Union[Tuple[Any], Any]]) -> Attribute:
            self._attributes[name] = Attribute(name=name, value=(func()))
            return self._attributes[name]

        return decorator

    def attributes(self, *names: str) -> Callable[[Callable], List[Attribute]]:
        def wrapper(func: Callable[[], Union[Tuple[Any], Any]]) -> List[Attribute]:
            for name in names:
                for i, v in enumerate((func())):
                    self._attributes[name] = Attribute(name=name, value=v[i])
            return [
                attribute
                for attribute in self._attributes.values()
                if attribute.name in names
            ]

        return wrapper

    def run(self):
        kwargs = {}
        for attribute in self._attributes.values():
            kwargs[attribute.name] = attribute.value
        return setup(**kwargs)
