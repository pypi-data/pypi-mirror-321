# Tree Printer

A simple Python library that helps developers generate and share their project directory structures. Perfect for documenting project layouts in GitHub READMEs, technical documentation, or when explaining project organization to other developers.

## Why Tree Printer?

When sharing your project on platforms like GitHub or discussing code organization with other developers, it's important to show your project's folder structure. However, manually typing out directory structures is:
- Time-consuming
- Error-prone
- Hard to maintain as your project grows

Tree Printer solves this by automatically generating a clean, consistent directory structure that you can instantly copy into your documentation.

## Example

Run:
```bash
dir-tree-printer /path/to/your/project
```

Get:
```
└── my-project
    ├── src
    │   └── components
    │       ├── Header.js
    │       └── Footer.js
    ├── tests
    ├── README.md
    └── package.json
```

Now you can directly paste this into your README, documentation, or anywhere else you need to show your project structure!

## Installation

```bash
pip install dir-tree-printer
```

## Usage

### Command Line
```bash
# Basic usage
dir-tree-printer /path/to/directory

# Exclude specific folders
dir-tree-printer /path/to/directory --exclude node_modules .git
```

### Python API
```python
from tree_printer import TreePrinter

printer = TreePrinter()
printer.print_structure("./my_directory")
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
