from dataclasses import dataclass


@dataclass
class Task:
    name: str
    description: str
    command: str
    stdin: str
    except_returncode: int
    expect_stdout: str


@dataclass
class Validator:
    name: str
    description: str


@dataclass
class Schema:
    name: str
    id: str
    baseUrl: str
