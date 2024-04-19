from dataclasses import dataclass


@dataclass
class ArgsValidate:
    schema: str
    file: str


@dataclass
class ArgsRegister:
    url: str
