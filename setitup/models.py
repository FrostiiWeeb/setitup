from dataclasses import dataclass
from typing import Callable, List, Union, Tuple, Any


def FILE(filename: str) -> str:
    with open(filename, "r") as f:
        cntnt = f.read()
    return cntnt


@dataclass
class Attribute:
    name: str
    value: Union[str, Callable[[], Any]]

    def __call__(self, *args, **kwargs) -> Any:
        if callable(self.value):
            return self.value(*args, **kwargs)
        return self.value


@dataclass
class PROJECT_URL:
    type: str
    url: str


@dataclass
class CLASSIFIER:
    classifier: str


@dataclass
class LONG_DESCRIPTION_CONTENT_TYPE:
    type: str

    @property
    def internal_use(self):
        return self.type


class PROJECT_URLS:
    def __init__(self, urls: List[PROJECT_URL]) -> None:
        self.urls = urls

    @property
    def internal_use(self):
        return {u.type: u.url for u in self.urls}


class CLASSIFIERS:
    def __init__(self, classifiers: List[CLASSIFIER]) -> None:
        self.classifiers = classifiers

    @property
    def internal_use(self):
        return [c.classifier for c in self.classifiers]


class LONG_DESCRIPTION:
    def __init__(self, content: str) -> None:
        self.content = content

    @property
    def internal_use(self):
        return self.content
