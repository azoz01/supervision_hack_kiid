import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

import pandas as pd
from lib.constants import RAW_KIIDS_DIR, META_FILE_PATH


def main():
    list_of_files = RAW_KIIDS_DIR.iterdir()
    list_of_files = [
        f.name for f in list_of_files if f.suffix in [".ashx", ".pdf"]
    ]
    out_df = pd.DataFrame(columns=["ID_KIID", "ID_ZESPOLU", "NAZWA_PLIKU"])
    id = 0
    for file in list_of_files:
        id += 1
        row_dict = {
            "ID_KIID": id,
            "ID_ZESPOLU": 2,
            "NAZWA_PLIKU": file
        }
        row_df = pd.DataFrame(data=row_dict, index=[0])
        out_df = pd.concat([out_df, row_df])
    out_df.to_csv(META_FILE_PATH, index=False)


if __name__ == "__main__":
    main()
