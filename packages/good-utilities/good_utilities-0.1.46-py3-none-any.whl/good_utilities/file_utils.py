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
