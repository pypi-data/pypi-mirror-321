import argparse

from .core import TreePrinter


def main():

    parser = argparse.ArgumentParser(
        description="Print directory structure in a tree-like format"
    )

    parser.add_argument(
        "path",
        help="Path to the directory to visualize"
    )

    parser.add_argument(
        "--exclude",
        nargs="+",
        help="Folders to exclude (space-separated)",
        default=None
    )

    args = parser.parse_args()

    printer = TreePrinter()

    printer.print_structure(args.path, args.exclude)


if __name__ == "__main__":
    main()
