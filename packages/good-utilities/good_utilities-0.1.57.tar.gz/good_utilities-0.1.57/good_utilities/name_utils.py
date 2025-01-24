# Name utility functions


import datetime
import uuid


def generate_unique_name(prefix: str) -> str:
    """
    Generate a unique name based on UUID and current timestamp.
    
    Parameters:
        prefix (str): A prefix to prepend to the unique name.
    
    Returns:
        str: A unique name combining the prefix, UUID, and current timestamp.

    Imports:
        import uuid
        import datetime
    """
    unique_id = uuid.uuid4()
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return f'{prefix}_{unique_id}_{timestamp}'
