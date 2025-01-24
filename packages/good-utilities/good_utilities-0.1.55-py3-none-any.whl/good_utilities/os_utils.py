# Os utility functions


import errno
import os


def create_directories(path: str) -> bool:
    """
    Create a directory and any necessary parent directories.
        
    Parameters:
        path (str): The path of the directory to create.

    Returns:
        bool: True if the directory was created, False if it already exists or an error occurred.

    Imports:
        import os
        import errno
    """
    try:
        os.makedirs(path)
        return True
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            return False
        raise


def get_file_size(file_path: str) -> int:
    """
    Get the size of a file in bytes.
    
    Parameters:
        file_path (str): The path to the file.
    
    Returns:
        int: The size of the file in bytes, or -1 if the file does not exist.

    Imports:
        import os
    """
    if not os.path.isfile(file_path):
        return -1
    return os.path.getsize(file_path)
