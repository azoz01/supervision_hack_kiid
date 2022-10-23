import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))
from typing import Dict, Callable
import pandas as pd

from lib.extract_text_data.srri import extract_srri
from lib.extract_text_data.funds import (retrive_register_id, 
                                         retrive_fund_name,
                                         retrive_subfund_name,
                                         retrive_organisation_name,
                                         retrive_fund_country_id)

from lib.extract_text_data.pratical_info import (
    get_depositary,
    get_krs,
    get_nip,
    get_address,
    get_capital,
    get_currency,
    get_esg,
    get_type
)

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
    "DEPOZYTARIUSZ": get_depositary,
    "KRS_TOWARZYSTWA": get_krs,
    "NIP_TOWARZYSTWA": get_nip,
    "SZIEDZIBA_TOWARZYSTWA": get_address,
    "KAPITAL_ZAKLADOWY_TOWARZYSTWA": get_capital
    "WALUTA_KAPITALU_ZAKLADOWEGO_TOWARZYSTWA": get_currency,
    "CZY_ESG": get_esg,
    "TYP_FUNDUSZU": get_type
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
