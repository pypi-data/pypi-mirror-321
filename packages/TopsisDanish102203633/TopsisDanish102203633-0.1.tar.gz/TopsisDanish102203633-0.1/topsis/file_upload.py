import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor
import threading

# Lock to prevent race conditions in multi-threaded environment
lock = threading.Lock()

def upload_file(file_path, async_upload=False):
    """
    Function to upload a file (CSV or Excel) and return a DataFrame with advanced features.
    
    Args:
    file_path (str): Path to the file to be uploaded. Supports CSV and Excel formats.
    async_upload (bool): Whether the upload should happen asynchronously (default is False).
    
    Returns:
    pandas.DataFrame: The DataFrame containing the data from the uploaded file, or an error message.
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check file size (Example: Limit file size to 50MB)
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # File size in MB
    if file_size > 500:
        raise ValueError("File is too large. Maximum allowed size is 500MB.")

    # Read file based on its extension
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")

    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The uploaded file is empty.")

    # Optionally, check for valid columns/rows (for decision matrix)
    expected_columns = ['Criteria1', 'Criteria2', 'Criteria3']  # Example criteria columns
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {', '.join(missing_columns)}")
    
    # Data Type Enforcement (Numeric data for criteria columns)
    for col in expected_columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"Column {col} must contain numeric values.")
    
    # Asynchronous File Handling (Optional: Enables faster handling for large files)
    if async_upload:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(process_file, df)
            result = future.result()  # Ensure the task is completed
    else:
        result = process_file(df)

    return result

def process_file(df):
    """
    A helper function to process the uploaded DataFrame after validation.
    
    Args:
    df (pandas.DataFrame): The DataFrame to process.
    
    Returns:
    pandas.DataFrame: The cleaned and processed DataFrame.
    """
    with lock:
        # Additional data cleaning steps here (e.g., drop duplicates, handle missing values)
        print("Processing file...")

        # Example: Removing duplicates
        df = df.drop_duplicates()

        # Handle missing data with default 'mean' strategy (or any custom logic)
        df = fill_missing_data(df)

        # Display a preview of the cleaned data (for user feedback)
        print("File summary after cleaning:")
        print(f"File summary: {df.shape[0]} rows and {df.shape[1]} columns.")
        print(f"First few rows:\n{df.head()}")

    return df

def fill_missing_data(df, strategy='mean'):
    """
    Fill missing data in the DataFrame using the specified strategy.
    Args:
    df (pandas.DataFrame): The DataFrame with missing values.
    strategy (str): The strategy to use for filling missing data. Default is 'mean'.
    Returns:
    pandas.DataFrame: The DataFrame with missing values filled.
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'ffill':
        return df.fillna(method='ffill')
    elif strategy == 'bfill':
        return df.fillna(method='bfill')
    elif strategy == 'interpolate_linear':
        return df.interpolate(method='linear')
    elif strategy == 'interpolate_polynomial':
        return df.interpolate(method='polynomial', order=2)  # You can change the order as needed
    else:
        raise ValueError(f"Unknown missing data strategy: {strategy}")
