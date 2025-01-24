# String utility functions


import re


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Parameters:
        text (str): The input string.
    
    Returns:
        str: The input string with each word capitalized.

    Imports:
        import re
    """
    return re.sub(r'(\w)', lambda m: m.group(1).upper(), text)
