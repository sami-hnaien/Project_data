import pandas as pd


class Dataset:
    """
    A simple wrapper for loading selected columns of a CSV file
    into a pandas DataFrame.
    """

    def __init__(self, file_path: str, columns: list[str] = None):
        """
        Parameters:
            file_path (str): Path to the CSV file.
            columns (list[str], optional): List of column names to read.
        """
        self.file_path = file_path

    def to_dataframe(self, cols = None) -> pd.DataFrame:
        """
        Load the CSV file into a pandas DataFrame,
        reading only the specified columns if provided.
        """
        try:
            return pd.read_csv(self.file_path, usecols=cols, low_memory=False)
        except Exception as e:
            print(f"Error reading '{self.file_path}': {e}")
            return None

    def __repr__(self):
        return f"Dataset(file_path='{self.file_path}')"
