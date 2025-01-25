import os
from typing import List, Optional


class TreePrinter:
    def __init__(self, default_exclude: Optional[List[str]] = None):
        self.default_exclude = default_exclude or [
            "node_modules",
            ".git",
            "__pycache__",
            ".next",
            "venv",
            "dist",
            "build",
        ]

    def print_structure(
        self,
        path: str,
        exclude_folders: Optional[List[str]] = None,
        prefix: str = "",
        is_last: bool = True,
    ) -> None:

        exclude_folders = exclude_folders or self.default_exclude

        base_name = os.path.basename(path)

        if base_name in exclude_folders:
            return

        connector = "└──" if is_last else "├──"

        print(f"{prefix}{connector} {base_name}")

        if os.path.isdir(path):

            items = os.listdir(path)

            items = [
                item
                for item in items
                if not item.startswith(".") and item not in exclude_folders
            ]

            items.sort(key=lambda x: (
                not os.path.isdir(os.path.join(path, x)), x))

            for idx, item in enumerate(items):

                new_prefix = prefix + ("    " if is_last else "│   ")
                self.print_structure(
                    os.path.join(path, item),
                    exclude_folders,
                    new_prefix,
                    idx == len(items) - 1,
                )
