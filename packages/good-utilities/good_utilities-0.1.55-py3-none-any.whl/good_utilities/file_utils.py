# File utility functions


import errno
import os


def write_to_file(file_path: str, content: str) -> bool:
    """
    Write content to a specified file.
    
    Parameters:
        file_path (str): The path to the file to write to.
        content (str): The content to write to the file.
    
    Returns:
        bool: True if the write was successful, False otherwise.

    Imports:
        import os
        import errno
    """
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except (IOError, OSError) as e:
        return False


def read_file_lines(file_path: str) -> list:
    """
    Read lines from a specified text file.
    
    Parameters:
        file_path (str): The path to the file to read from.
    
    Returns:
        list: A list of lines from the file, or an empty list if the file does not exist or cannot be read.

    Imports:
        import os
    """
    if not os.path.isfile(file_path):
        return []
    with open(file_path, 'r') as f:
        return f.readlines()
