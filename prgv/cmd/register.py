from prgv.lib.args import ArgsRegister
from prgv.lib.pref import Pref, PrefSchema, save_pref


def register(args: ArgsRegister) -> None:
    print(f"Registering schema from {args.url}...")
    save_pref(
        Pref(
            schemas=[
                PrefSchema(
                    name="name",
                    base_url=args.url,
                    namespace="namespace",
                )
            ]
        )
    )
