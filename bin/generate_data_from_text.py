import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))
from typing import Dict, Callable
import pandas as pd

from lib.extract_text_data.srri import extract_srri
from lib.extract_text_data.funds import (
    retrive_register_id,
    retrive_fund_name,
    retrive_subfund_name,
    retrive_organisation_name,
    retrive_fund_country_id,
)
import lib.extract_text_data.entity_category as entity_category
from lib.constants import (
    PARSED_KIIDS_DIR,
    GENERATED_COLUMNS,
    TEAM_ID,
    KIID_DATA_PATH,
)

COLS_TO_GENERATING_FUNCTIONS_MAPPING: Dict[str, Callable] = {
    "SRRI": extract_srri,
    "NAZWA_SUBFUNDUSZU": retrive_subfund_name,
    "NAZWA_FUNDUSZU": retrive_fund_name,
    "IDENTYFIKATOR_KRAJOWY": retrive_fund_country_id,
    "NUMER_RFI": retrive_register_id,
    "PODMIOT_ZARZADZAJACY": retrive_organisation_name,
    "KATEGORIE_JEDNOSTEK_UCZESTNICTWA": entity_category.get_category,
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
