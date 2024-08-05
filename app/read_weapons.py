import pandas as pd
import os


def read_weapons():
    if os.path.exists("./weapons.xlsx"):
        df = pd.read_excel("weapons.xlsx")
        return df.to_dict(orient="records")
    return []
