# Data utility functions

from typing import List, Dict
import json

def filter_data(data: List[Dict], key: str, value: any) -> List[Dict]:
    """
    Filter a list of dictionaries based on a specified key-value pair.
    
    Parameters:
        data (List[Dict]): The list of dictionaries to filter.
        key (str): The key to filter on.
        value (Any): The value that the key should match.
    
    Returns:
        List[Dict]: A list of dictionaries that match the key-value pair.

    Imports:
        import json
        from typing import List, Dict
    """
    return [item for item in data if key in item and item[key] == value]