import pandas as pd

class DataAdapter:
    """
    A simple data adapter that loads player data from a CSV file.
    """

    def __init__(self, player_csv: str):
        self.player_csv = player_csv

    def load_players(self) -> pd.DataFrame:
        """
        Load player data from the CSV file.
        """
        try:
            return pd.read_csv(self.player_csv)
        except FileNotFoundError:
            return pd.DataFrame()

    def filter_players(self, df: pd.DataFrame, min_minutes: int = 0, max_age: int = 100) -> pd.DataFrame:
        """
        Filter players based on minimum minutes played and maximum age.
        """
        return df[(df.get('minutes_played', 0) >= min_minutes) & (df.get('age', 0) <= max_age)]
