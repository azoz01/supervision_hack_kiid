import pandas as pd
import re


def retrive_register_id(knf_df: "pd.DataFrame", intro_text: str) -> int:

    does_not_id_exist = (
        knf_df["nr_w_rejestrze"]
        .apply(lambda register_id: re.search(str(register_id), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_id_exist]

    if len(df_filtered["nr_w_rejestrze"].unique()) != 1:
        return None

    return df_filtered["nr_w_rejestrze"].iloc[0]


def retrive_fund_name(
    knf_df: "pd.DataFrame", intro_text: str, register_id: int = None
) -> str:

    if register_id is None:
        return None

    df_filtered = knf_df[knf_df["nr_w_rejestrze"] == register_id]
    full_fund_name = df_filtered["fundusz"].unique()[0]

    return full_fund_name


def retrive_subfund_name(knf_df: "pd.DataFrame", intro_text: str) -> str:

    does_not_name_exist = (
        knf_df["subfundusz"]
        .apply(lambda register_id: re.search(str(register_id), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_name_exist]

    if df_filtered.size == 0:
        return None

    fund_name = (
        df_filtered["subfundusz"]
        .sort_values(key=lambda x: x.str.len(), ascending=False)
        .iloc[0]
    )

    return fund_name


def retrive_fund_name(
    knf_df: "pd.DataFrame", intro_text: str, register_id: int = None
) -> str:

    if register_id is None:
        return None

    df_filtered = knf_df[knf_df["nr_w_rejestrze"] == register_id]
    full_organisation_name = df_filtered["towarzystwo"].unique()[0]

    return full_organisation_name


def retrive_fund_country_id(knf_df: "pd.DataFrame", intro_text: str):

    does_not_id_exist = (
        knf_df["indentyfikator_krajowy"]
        .apply(lambda register_id: re.search(str(register_id), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_id_exist]

    if df_filtered.shape[0] != 1:
        return None

    return df_filtered["indentyfikator_krajowy"].iloc[0]


def retrive_organisation_id(knf_df: "pd.DataFrame", intro_text: str):

    does_not_id_exist = (
        knf_df["identyfikator_krajowy_funduszu"]
        .apply(lambda register_id: re.search(str(register_id), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_id_exist]

    if df_filtered.shape[0] != 1:
        return None

    return df_filtered["indentyfikator_krajowy"].iloc[0]


def retive_all_info(
    knf_df: "pd.DataFrame", intro_text: str, register_id: int = None
) -> str:
    register_id = retrive_register_id(knf_df, intro_text)
    fund_name = retrive_fund_name(knf_df, intro_text, register_id)
    subfund_name = retrive_subfund_name(knf_df, intro_text)
    # organisation_name = retrive_organisation_name(knf_df, intro_text, register_id)
    fund_country_id = retrive_fund_country_id(knf_df, intro_text)
    organisation_country_id = retrive_organisation_id(knf_df, intro_text)

    return {
        "fund_name": fund_name,
        "subfund_name": subfund_name,
        # 'organisation_name': organisation_name,
        "register_id": register_id,
        "fund_country_id": fund_country_id,
        "organisation_country_id": organisation_country_id,
    }
