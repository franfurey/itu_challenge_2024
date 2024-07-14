# sandbox_franfurey/handling_date_formats.py
import pandas as pd

def try_parse_dates(column, formats):
    """
    Attempt to convert a date column to datetime using a list of specified formats and keep datetime format.
    Args:
        column (pd.Series): The date column to be parsed.
        formats (list of str): A list of date formats to try.
    Returns:
        pd.Series: The column with dates converted to datetime64[ns].
    """
    converted = pd.Series(index=column.index, dtype='datetime64[ns]')
    used_formats = []

    for fmt in formats:
        # Try converting using the specified format
        temp_converted = pd.to_datetime(column, format=fmt, errors='coerce')
        if not temp_converted.isnull().all():
            # Apply successful conversions
            converted[temp_converted.notnull()] = temp_converted.dropna()
            used_formats.append(fmt)

    # Warn if more than one format was used
    if len(used_formats) > 1:
        print(f"Multiple date formats needed: {used_formats}")

    # Check for any entries that could not be converted
    if converted.isnull().any():
        print("Some dates could not be converted and were set to NaT. Here are some examples:")
        print(column[converted.isnull()])
    else:
        print("All dates were successfully converted.")

    return converted