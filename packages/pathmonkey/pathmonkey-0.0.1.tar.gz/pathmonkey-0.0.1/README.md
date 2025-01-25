# PathMonkey

`PathMonkey` is a lightweight, cross-platform Python utility that simplifies path manipulation. It supports advanced path construction and deconstruction for both Linux and Windows, making it easier to handle paths reliably across different operating systems.

## Features

- Construct paths from a list of components (e.g., `['~', 'projects', 'example']`).
- Deconstruct paths into individual components, with support for:
  - Home directory (`~`)
  - Windows drive letters (`C:`)
  - Absolute and relative paths
- Handles edge cases like trailing slashes, mixed separators, and empty paths.
- Built on Python's modern `pathlib` for robust path handling.

---

## Installation

Install `PathMonkey` from PyPI using pip:

```bash
pip install pathmonkey
```

---

## Usage

Here's how to use `PathMonkey` in your Python project:

### Import the Module

```python
from pathmonkey.pathmonkey import PathMonkey
from pathlib import Path
```

### Constructing Paths
```python
# Construct a path relative to the home directory
path = PathMonkey.construct_path(['~', 'projects', 'example'])
print(path)  # Output: /home/user/projects/example (on Linux)

# Construct an absolute path
path = PathMonkey.construct_path(['/', 'usr', 'bin'])
print(path)  # Output: /usr/bin

# Construct a Windows path
path = PathMonkey.construct_path(['C:', 'Users', 'example'])
print(path)  # Output: C:\Users\example
```

### Deconstructing Paths
```python
# Deconstruct a path relative to the home directory
components = PathMonkey.deconstruct_path(Path.home().joinpath('projects', 'example'))
print(components)  # Output: ['~', 'projects', 'example']

# Deconstruct an absolute path
components = PathMonkey.deconstruct_path(Path('/usr/bin'))
print(components)  # Output: ['', 'usr', 'bin']

# Deconstruct a Windows path
components = PathMonkey.deconstruct_path(Path('C:\\Users\\example'))
print(components)  # Output: ['C:', 'Users', 'example']
```

---

## Examples

### Path Construction
```python
examples = [
    (['~', 'projects', 'example'], "Home directory relative"),
    (['/', 'usr', 'bin'], "Root directory"),
    (['', 'usr', 'bin'], "Absolute path from root"),
    (['C:', 'Users', 'example'], "Windows drive letter"),
    (['..', 'another_folder'], "Relative path"),
    (['usr', 'bin'], "Additional relative path"),
]

for elements, description in examples:
    path = PathMonkey.construct_path(elements)
    print(f"{description}: {path}")
```

### Path Deconstruction
```python
paths = [
    (Path.home().joinpath('projects', 'example'), "Home directory relative"),
    (Path('/usr/bin'), "Root directory"),
    (Path('usr/bin'), "Relative path"),
    (Path('C:\\Users\\example'), "Windows drive letter"),
]

for path, description in paths:
    components = PathMonkey.deconstruct_path(path)
    print(f"{description}: {components}")
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository on [GitHub](https://github.com/RexBytes/PathMonkey).
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Links

- **Source Code**: [GitHub Repository](https://github.com/RexBytes/PathMonkey)
- **Bug Tracker**: [Report Issues](https://github.com/RexBytes/PathMonkey/issues)
```

