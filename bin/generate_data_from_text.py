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
import lib.extract_text_data.levels as levels
from lib.extract_text_data.oplaty import get_oplaty
from lib.extract_text_data.investment_years import get_investment_years
from lib.extract_text_data.profil_ryzyka_i_zysku import (
    get_profil_ryzyka_i_zysku,
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
    "KATEGORIE_JEDNOSTEK_UCZESTNICTWA": entity_category.get_category,
    "MINIMALNY_POZIOM_INWESTYCJI_UDZIALOWE": levels.get_min_udzialowa,
    "MAKSYMALNY_POZIOM_INWESTYCJI_UDZIALOWE": levels.get_max_udzialowa,
    "MINIMALNY_POZIOM_INWESTYCJI_DLUZNE": levels.get_min_dluzna,
    "MAKSYMALNY_POZIOM_INWESTYCJI_DLUZNE": levels.get_max_udzialowa,
    "MINIMALNY_POZIOM_INWESTYCJI_TYTULY_UCZESTNICTWA": levels.get_min_tyt_udz,
    "MAKSYMALNY_POZIOM_INWESTYCJI_TYTULY_UCZESTNICTWA": levels.get_max_tyt_udz,
    "ZALECANY_OKRES_INWESTYCJI": get_investment_years,
    "PROFIL_RYZYKA_I_ZYSKU": get_profil_ryzyka_i_zysku,
    "OPLATY": get_oplaty,
}


def main():
    df_parsed = pd.read_parquet(PARSED_KIIDS_DIR).sample(frac=0.01)
    final_df_columns = ["ID_KIID", "ID_ZESPOLU"]
    final_df = pd.DataFrame(columns=final_df_columns + GENERATED_COLUMNS)
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
