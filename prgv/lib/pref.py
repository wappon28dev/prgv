from dataclasses import dataclass
from pathlib import Path

from appdirs import user_config_dir
from typed_json_dataclass import TypedJsonMixin

from prgv.lib.consts import VERSION
from prgv.lib.schema import Schema

config_path = (
    Path(
        user_config_dir("prgv", version=f"v{VERSION}"),
    )
    / "settings.json"
)


@dataclass
class PrefSchema:
    name: str
    url: str
    namespace: str


@dataclass
class Pref(TypedJsonMixin):
    schemas: list[PrefSchema]


def pref_load(pref_or_default: bool = False) -> Pref:
    if not config_path.exists():
        if pref_or_default:
            return Pref(schemas=[])
        else:
            raise FileNotFoundError("設定ファイルが見つかりません.")

    with open(config_path) as f:
        return Pref.from_json(f.read())


def pref_save(pref: Pref) -> None:
    if not config_path.exists():
        config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, "w") as f:
        f.write(pref.to_json())


def pref_from_schema(schema: Schema, url: str) -> Pref:
    pref = pref_load(pref_or_default=True)
    namespaces = [s.namespace for s in pref.schemas]
    if schema.namespace in namespaces:
        pref.schemas = [
            s
            for s in pref.schemas
            if s.namespace != schema.namespace  #
        ]
        print("スキーマが既に登録されています. 上書きしました.")

    pref.schemas.append(
        PrefSchema(
            name=schema.name,
            url=url,
            namespace=schema.namespace,
        )
    )

    return pref
