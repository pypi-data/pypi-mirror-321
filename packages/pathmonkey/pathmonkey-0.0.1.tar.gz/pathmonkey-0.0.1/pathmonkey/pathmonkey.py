from pathlib import Path

class PathMonkey:
    @staticmethod
    def construct_path(path_elements):
        """Construct a path from a list of elements, handling '~', '', '/', and '\\'."""
        if not path_elements:
            return Path()


        # Start with handling the first element specially if it indicates a root or home directory
        first_elem = path_elements[0]
        if first_elem in ['~', '', '/', '\\']:
            if first_elem == '~':
                # Path relative to user's home directory
                return Path.home().joinpath(*path_elements[1:])
            elif first_elem in ['', '/', '\\']:
                # Absolute path starting from root
                return Path('/').joinpath(*path_elements[1:])
        elif ':' in first_elem and len(first_elem) == 2 and first_elem[1] == ':':
            # Windows-specific: path starts with a drive letter
            windows_path=Path(first_elem).joinpath(*path_elements[1:])
            return str(windows_path).replace('/', '\\')
        else:
            # Normal path construction
            return Path(*path_elements)

    @staticmethod
    def deconstruct_path(input_path):
        """Deconstruct a Path object into a list of its components, considering special cases."""

        components = []

        # Handle absolute paths, including Windows-specific drive letters
        if input_path.is_absolute():
            if input_path.drive:
                components.append(input_path.drive)
            else:
                components.append('')
            components.extend(input_path.parts[1:])
        elif str(input_path).startswith(str(Path.home())):
            # Handle paths relative to the home directory
            components.append('~')
            components.extend(input_path.relative_to(Path.home()).parts)
        else:
            # Handle relative paths
            components.extend(input_path.parts)

        return components



