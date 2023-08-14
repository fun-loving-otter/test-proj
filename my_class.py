# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df.
# BONUS: Return the data grouped in the best manner you see fit.

import pandas as pd


class CSVFormatter:
    def __init__(self, file_path):
        self.file_path = file_path

    def fix_formatting(self):
        df = pd.read_csv(self.file_path, skipinitialspace=True)
        numeric_cols = [
            "Revenue",
            "Profit",
            "Cost",
            "Expense",
            "Income",
            "Price",
            "Salary",
            "Investment",
        ]
        df[numeric_cols] = (
            df[numeric_cols].replace("[\$,]", "", regex=True).astype(float)
        )
        merged_df = df.groupby(["Master", "ID"]).sum().reset_index()

        return merged_df


formatter = CSVFormatter("sample.csv")
formatted_df = formatter.fix_formatting()

grouped_df = formatted_df.groupby("ID").sum()
print(grouped_df)
