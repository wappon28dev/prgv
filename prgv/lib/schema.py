from dataclasses import dataclass
from json import JSONDecodeError
from urllib.request import Request, urlopen

from typed_json_dataclass import TypedJsonMixin


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
    id: str
    description: str
    tasks: list[Task]


@dataclass
class Schema(TypedJsonMixin):
    namespace: str
    name: str
    description: str
    validators: list[Validator]


def get_schema_from_url(url: str) -> Schema:
    try:
        with urlopen(Request(url)) as res:
            body = res.read().decode("utf-8")
    except Exception as e:
        print("スキーマの取得に失敗しました.")
        raise e

    try:
        schema = Schema.from_json(body)
    except JSONDecodeError as e:
        print("スキーマのパースに失敗しました.  正しい JSON かを確認してください.")
        raise e

    return schema
