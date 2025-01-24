# Config utility functions


import json


def save_config(config: dict, file_path: str) -> bool:
    """
    Save configuration settings to a JSON file.
    
    Parameters:
        config (dict): A dictionary containing configuration settings.
        file_path (str): The path to the JSON file where settings will be saved.
    
    Returns:
        bool: True if the configuration was saved successfully, False otherwise.

    Imports:
        import json
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception:
        return False
