# Network utility functions


import socket
import sys


def get_local_ip() -> str:
    """
    Get the local IP address of the machine.
    
    Returns:
        str: The local IP address as a string, or '127.0.0.1' if an error occurs.

    Imports:
        import socket
        import sys
    """
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception:
        return '127.0.0.1'
