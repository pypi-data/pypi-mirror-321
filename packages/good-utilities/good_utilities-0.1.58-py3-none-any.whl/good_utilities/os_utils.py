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


def remove_empty_directories(path: str) -> int:
    """
    Remove empty directories in the given path.
    
    Parameters:
        path (str): The directory path to search for empty directories.
    
    Returns:
        int: The number of empty directories removed, or -1 if the path is not a directory.

    Imports:
        import os
        import errno
    """
    if not os.path.isdir(path):
        return -1
    removed_count = 0
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            try:
                os.rmdir(dir_to_check)
                removed_count += 1
            except OSError:
                continue
    return removed_count


def list_directory_contents(dir_path: str) -> list:
    """
    List all files and directories in the given directory path.
    
    Parameters:
        dir_path (str): The path of the directory to list contents.
    
    Returns:
        list: A list of names (files and directories) in the specified directory, or an empty list if the directory does not exist or an error occurs.

    Imports:
        import os
    """
    if not os.path.isdir(dir_path):
        return []
    return os.listdir(dir_path)
