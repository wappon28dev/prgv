from prgv.lib.args import ArgsValidate


def validate(args: ArgsValidate) -> None:
    print(f"Validating {args.file} with schema {args.schema}...")
