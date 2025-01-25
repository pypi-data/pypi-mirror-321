from dir_tree_printer import TreePrinter


def main():
    # Basic usage
    printer = TreePrinter()
    print("Default exclusions:")
    printer.print_structure(".")

    # Custom exclusions
    print("\nCustom exclusions:")
    printer.print_structure(".", exclude_folders=["tests", "docs"])


if __name__ == "__main__":
    main()
