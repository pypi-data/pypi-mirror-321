```markdown
# Tree Printer Documentation

## Installation
```pip install dir-tree-printer```

## Usage
### Command Line Interface
```bash
# Basic usage
dir-tree-printer /path/to/directory

# Exclude specific folders
dir-tree-printer /path/to/directory --exclude folder1 folder2
```

### Python API
```python
from tree_printer import TreePrinter

# Create printer with default exclusions
printer = TreePrinter()

# Print structure
printer.print_structure("./my_directory")

# Custom exclusions
printer.print_structure("./my_directory", exclude_folders=["env", "cache"])
```