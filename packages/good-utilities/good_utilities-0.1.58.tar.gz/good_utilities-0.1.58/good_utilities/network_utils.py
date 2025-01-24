# Network utility functions


import requests
import socket


def get_local_ip() -> str:
    """
    Get the local IP address of the machine.
            
    Returns:
        str: The local IP address as a string, or '127.0.0.1' if an error occurs.

    Imports:
        import socket
    """
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception:
        return '127.0.0.1'


def check_port_open(host: str, port: int) -> bool:
    """
    Check if a specific port on a given host is open.
        
    Parameters:
        host (str): The hostname or IP address.
        port (int): The port number to check.

    Returns:
        bool: True if the port is open, False otherwise.

    Imports:
        import socket
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        return result == 0


def get_public_ip() -> str:
    """
    Retrieve the public IP address of the machine.
    
    Returns:
        str: The public IP address as a string, or 'Unable to retrieve' if an error occurs.

    Imports:
        import socket
        import requests
    """
    try:
        response = requests.get('https://api.ipify.org')
        return response.text.strip()
    except Exception:
        return 'Unable to retrieve'
