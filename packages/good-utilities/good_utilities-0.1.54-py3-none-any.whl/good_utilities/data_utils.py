# Data utility functions


from typing import List, Dict


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
        from typing import List, Dict
    """
    return [item for item in data if key in item and item[key] == value]


def merge_data(data: List[Dict]) -> Dict:
    """
    Merge a list of dictionaries into a single dictionary.
    
    Parameters:
        data (List[Dict]): A list of dictionaries to merge.
    
    Returns:
        Dict: A single dictionary containing all key-value pairs from the provided dictionaries.
        In case of key conflicts, the last value encountered will be used.

    Imports:
        from typing import List, Dict
    """
    result = {}
    for dictionary in data:
        result.update(dictionary)  # Update the result with the current dictionary
    return result
