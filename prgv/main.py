from argparse import ArgumentParser

from prgv.cmd.register import register
from prgv.cmd.validate import validate
from prgv.lib.args import ArgsRegister, ArgsValidate
from prgv.lib.consts import LOGO


def parse_args() -> None:
    parser = ArgumentParser(
        description="A simple PRoGram Validator",
    )
    sub_parsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    parser_validate = sub_parsers.add_parser(
        "validate",
        aliases=["v"],
        help="Validate a file",
    )
    parser_validate.add_argument(
        "schema",
        help="The name of the schema",
    )
    parser_validate.add_argument(
        "file",
        help="The file to validate",
    )
    parser_validate.set_defaults(
        handler=lambda args: validate(
            ArgsValidate(file=args.file, schema=args.schema),
        ),
    )

    parser_register = sub_parsers.add_parser(
        "register",
        aliases=["r"],
        help="Register a schema",
    )
    parser_register.add_argument(
        "url",
        help="The URL of the schema",
    )
    parser_register.set_defaults(
        handler=lambda args: register(
            ArgsRegister(url=args.url),
        )
    )

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


def main() -> None:
    print(LOGO)
    parse_args()


if __name__ == "__main__":
    main()
