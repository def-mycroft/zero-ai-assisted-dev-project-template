import argparse
from zero_aidev_framework import docs_tools
from zero_aidev_framework.docs_tools import new_doc as create_new_doc


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="zero-ai-dev-framework",
        description="Zero AI Dev Framework CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # dev subcommand
    dev_parser = subparsers.add_parser(
        "dev", help="Developer utilities"
    )
    dev_parser.add_argument(
        "--update-toc",
        action="store_true",
        help="Regenerate docs/CONTENTS.md"
    )
    dev_parser.add_argument(
        "--new-doc",
        action="store_true",
        help="create blank doc in docs/"
    )

    args = parser.parse_args(argv)

    if args.command == "dev":
        if args.update_toc:
            docs_tools.update_toc()
        elif args.new_doc:
            path = create_new_doc()
            print(path)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
