# Text utility functions


import re


def count_words(text: str) -> int:
    """
    Count the number of words in a given text.
    
    Parameters:
        text (str): The input text string.
    
    Returns:
        int: The count of words in the input text.

    Imports:
        import re
    """
    words = re.findall(r'\w+', text)
    return len(words)
