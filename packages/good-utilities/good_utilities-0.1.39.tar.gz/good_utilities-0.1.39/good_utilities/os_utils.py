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