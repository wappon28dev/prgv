from dataclasses import dataclass
from pathlib import Path

from appdirs import user_config_dir
from typed_json_dataclass import TypedJsonMixin

from prgv.lib.consts import VERSION

config_path = (
    Path(
        user_config_dir("prgv", version=f"v{VERSION}"),
    )
    / "settings.json"
)


@dataclass
class PrefSchema:
    name: str
    base_url: str
    namespace: str


@dataclass
class Pref(TypedJsonMixin):
    schemas: list[PrefSchema]


def load_pref() -> Pref:
    with open(config_path) as f:
        return Pref.from_json(f.read())


def save_pref(pref: Pref) -> None:
    if not config_path.exists():
        config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, "w") as f:
        f.write(pref.to_json())
