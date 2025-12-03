import matplotlib.pyplot as plt
import pandas as pd


class Graph:
    """
    A Class to initiate and plot a graph from a dataframe
    """

    def __init__(
        self, df: pd.core.frame.DataFrame, title: str, x_column: str, y_column: str
    ):
        """
        Parameters:
            df (str): Pandas dataframe.
            x_column (str): name of the column for the x axis
            y_column (str): name of the column for the y axis
            title (str): Title of the graph
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.title = title

    def show(self):
        """
        show graph
        """
        x = self.df[self.x_column].astype(int)
        y = self.df[self.y_column].astype(int)

        plt.plot(x, y)

        plt.xlabel(self.x_column)
        plt.ylabel(self.y_column)
        plt.title(self.title)

        plt.xticks(rotation=50)
        plt.xlabel(self.x_column)
        plt.ylabel(self.y_column)
        plt.title(self.title)
        x_values = self.df[self.x_column].astype(int)
        plt.xticks(x_values)  # show every year on x-axis

        plt.grid(True)

        plt.show()


class MultipleGraph:
    """
    A Class to initiate and plot a multiple graph from two dataframes
    """
     
    def __init__(
        self, df1, df2, x_column_1, x_column_2, y_column_1, y_column_2, title_1, title_2
    ):
        """
        Parameters:
            df1 (str): Pandas dataframe.
            df2 (str): Pandas dataframe.
            x_column_1 (str): name of the column for the x axis from df1
            x_column_2 (str): name of the column for the x axis from df2
            y_column_1 (str): name of the column for the y axis from df1
            y_column_2 (str): name of the column for the y axis from df2
            title_1 (str): Title of the left graph
            title_2 (str): Title of the right graph
        """
        self.df1 = df1
        self.df2 = df2
        self.x_column_1 = x_column_1
        self.x_column_2 = x_column_2
        self.y_column_1 = y_column_1
        self.y_column_2 = y_column_2
        self.title_1 = title_1
        self.title_2 = title_2

    def show_side_by_side(self):
        """
        Show side by side graph for the two dataframes
        """
        # Create a figure with 1 row and 2 columns
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Left plot from df1_data
        axes[0].plot(
            self.df1[self.x_column_1],
            self.df1[self.y_column_1],
            marker="o",
            color="blue",
        )
        axes[0].set_title(self.title_1)
        axes[0].set_xlabel(self.x_column_1)
        axes[0].set_ylabel(self.y_column_1)
        axes[0].tick_params(axis="x", rotation=50)
        axes[0].grid(True)
        axes[0].set_xticks(self.df1[self.x_column_1])

        # Left plot from df2_data
        axes[1].plot(
            self.df2[self.x_column_2],
            self.df2[self.y_column_2],
            marker="s",
            color="orange",
        )
        axes[1].set_title(self.title_2)
        axes[1].set_xlabel(self.x_column_2)
        axes[1].set_ylabel(self.y_column_2)
        axes[1].tick_params(axis="x", rotation=50)
        axes[1].grid(True)
        axes[1].set_xticks(self.df2[self.x_column_2])

        plt.tight_layout()  # adjust spacing
        plt.show()


class NormalizedGraph:
    """
    A Class to initiate and plot a normalized graph from two columns of a dataframe
    """
    def __init__(
        self, df, col_1, col_2
    ):
        """
        Parameters:
            df (str): Pandas dataframe.
            col 1 : name of the column for the x axis
            col 2: name of the column for the y axis
            title (str): Title of the graph
        """
        self.df = df.copy()  # avoid modifying original dataframe
        self.col_1 = col_1
        self.col_2 = col_2

        # Precompute normalized columns
        self.df["GDP_norm"] = self.df.groupby("Country Name")[self.col_1].transform(
            lambda x: (x - x.min()) / (x.max() - x.min())
        )
        self.df["Tourism_norm"] = self.df.groupby("Country Name")[
            self.col_2
        ].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

    def show(self):
        df_country = self.df

        plt.figure(figsize=(12, 6))
        plt.plot(
            df_country["Year"],
            df_country["GDP_norm"],
            label=f"{self.col_1} (normalized)",
        )
        plt.plot(
            df_country["Year"],
            df_country["Tourism_norm"],
            label=f"{self.col_2} (normalized)",
        )
        plt.xlabel("Year")
        plt.ylabel("Normalized Value (0–1)")
        plt.title(f"Normalized data")
        plt.legend()
        plt.grid(True)
        plt.show()
