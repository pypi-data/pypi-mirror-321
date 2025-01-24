# Date utility functions

import datetime

def get_days_between_dates(start_date: str, end_date: str) -> int:
    """
    Calculate the number of days between two dates.
    
    Parameters:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
        int: The number of days between the two dates. Returns a negative number if the start date is after the end date.

    Imports:
        import datetime
    """
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    return (end - start).days