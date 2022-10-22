import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))
from typing import Dict, Callable
import pandas as pd

from lib.extract_text_data.srri import extract_srri
from lib.constants import (
    PARSED_KIIDS_DIR,
    GENERATED_COLUMNS,
    TEAM_ID,
    KIID_DATA_PATH,
)

COLS_TO_GENERATING_FUNCTIONS_MAPPING: Dict[str, Callable] = {
    "SRRI": extract_srri
}


def main():
    df_parsed = pd.read_parquet(PARSED_KIIDS_DIR)
    final_df_columns = ["ID_KIID", "ID_ZESPOLU"]
    final_df = pd.DataFrame(
        columns=["ID_KIID", "ID_ZESPOLU"] + GENERATED_COLUMNS
    )
    final_df["ID_KIID"] = df_parsed["id"]
    final_df["ID_ZESPOLU"] = TEAM_ID
    for column in GENERATED_COLUMNS:
        generator = COLS_TO_GENERATING_FUNCTIONS_MAPPING.get(
            column, lambda arg: None
        )
        final_df[column] = df_parsed.apply(generator, axis=1)
    final_df.to_csv(KIID_DATA_PATH, index=False)


if __name__ == "__main__":
    main()
