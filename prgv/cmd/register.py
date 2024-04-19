from prgv.lib.args import ArgsRegister
from prgv.lib.pref import pref_from_schema, pref_save
from prgv.lib.schema import get_schema_from_url


def register(args: ArgsRegister) -> None:
    schema = get_schema_from_url(args.url)
    pref = pref_from_schema(schema, args.url)
    pref_save(pref)
