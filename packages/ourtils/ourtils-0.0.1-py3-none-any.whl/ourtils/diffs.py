from collections import defaultdict
from typing import Callable
import pandas as pd


class DataFrameDiffer:
    """
    A class to help compare dataframes. Deals with:

    - Matching columns
    - Filtering to differing rows

    Example:
        .. ipython:: python

            df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
            df1

            df2 = pd.DataFrame({"a": [1, 2, 4], "B": [4, 5, 1], "c": [5, 6, 1]})
            df2

            # Create a DataFrameDiffer object
            diffy = ut.DataFrameDiffer(df1, df2, "a")
            diffy.print_report()
            diffy.combined

    """

    lsuffix = "__left"
    rsuffix = "__right"

    @classmethod
    def create_diff(cls, row: pd.Series, cols: list[str]) -> dict:
        """Creates a dictionary that stores changes to the columns in a row.

        :param row: A row from a dataframe
        :param cols: A list of strings
        """
        _diff = defaultdict()
        for col in cols:
            b, a = row[f"{col}{cls.lsuffix}"], row[f"{col}{cls.rsuffix}"]
            if b != a:
                _diff[col] = (b, a)
        return _diff

    def __init__(
        self,
        left: pd.DataFrame,
        right: pd.DataFrame,
        join_on: list[str],
        column_cleaner: Callable = lambda x: x.strip().lower(),
    ):
        self.ldata = left.copy()
        self.rdata = right.copy()

        self.join_on = join_on
        self.column_cleaner = column_cleaner

        self.ldata.columns = [column_cleaner(col) for col in self.ldata]
        self.rdata.columns = [column_cleaner(col) for col in self.rdata]

        self.join_on = [column_cleaner(key) for key in self.join_on]

        self.columns_to_compare = [
            col for col in self.matching_columns if col not in self.join_on
        ]

        def create_message(_merge_indicator: str, diff: dict) -> str:
            """
            Creates a label based on the merge indicator as well as the changes
            that have happened to the row.
            """
            if _merge_indicator == "left_only":
                return "[-] Dropped"
            elif _merge_indicator == "right_only":
                return "[+] Added"
            elif diff:
                return "[~] Changed"
            return "[ ] Untouched"

        self.combined = (
            pd.merge(
                self.ldata,
                self.rdata,
                on=self.join_on,
                indicator=True,
                how="outer",
                suffixes=(self.lsuffix, self.rsuffix),
            )
            .assign(
                diff=lambda x: x.apply(
                    lambda x: self.create_diff(x, self.columns_to_compare), axis=1
                )
            )
            .assign(
                descr=lambda x: x.apply(
                    lambda x: create_message(x["_merge"], x["diff"]), axis=1
                )
            )
        )

    @property
    def left_columns(self) -> set:
        return set(self.ldata.columns)

    @property
    def right_columns(self) -> set:
        return set(self.rdata.columns)

    @property
    def matching_columns(self) -> set:
        return self.left_columns.intersection(self.right_columns)

    @property
    def new_columns(self):
        return self.right_columns.difference(self.left_columns)

    @property
    def missing_columns(self):
        return self.left_columns.difference(self.right_columns)

    @property
    def comparable(self) -> pd.DataFrame:
        return self.combined

    def print_report(self) -> None:
        """
        Prints out a handy report of the differences.
        """
        print("-" * 15)
        print("Difference report")
        print("-" * 15)
        print("Columns:")
        print(f"Removed: {self.missing_columns or 'None'}")
        print(f"Added: {self.new_columns or 'None'}")
        print(f"Matching: {self.matching_columns or 'None'}")
        print("-" * 15)
        print("Rows:")
        print(self.combined["descr"].value_counts(dropna=False))
