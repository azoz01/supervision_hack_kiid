import pandas as pd
import re

datapath = 'data/knf_funds.pkl'
knf_df = pd.read_pickle(datapath)


def retrive_register_id(row) -> int:
    
    intro_text = row['intro']

    does_not_id_exist = (
        knf_df["nr_w_rejestrze"]
        .apply(lambda register_id: re.search(str(register_id), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_id_exist]

    if len(df_filtered["nr_w_rejestrze"].unique()) != 1:
        return None

    return df_filtered["nr_w_rejestrze"].iloc[0]


def retrive_fund_name(row) -> str:

    intro_text = row['intro']
    
    register_id = retrive_register_id(row)

    if register_id is None:
        return None

    df_filtered = knf_df[knf_df["nr_w_rejestrze"] == register_id]
    full_fund_name = df_filtered["fundusz"].unique()[0]

    return full_fund_name


def retrive_subfund_name(row) -> str:

    intro_text = row['intro']

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


def retrive_organisation_name(row) -> str:

    intro_text = row['intro']

    register_id = retrive_register_id(row)

    if register_id is None:
        return None

    df_filtered = knf_df[knf_df["nr_w_rejestrze"] == register_id]
    full_organisation_name = df_filtered["towarzystwo"].unique()[0]

    return full_organisation_name


def retrive_fund_country_id(row):
        
    register_id = retrive_register_id(row)

        does_not_id_exist = (
        knf_df["indentyfikator_krajowy"]
        .apply(lambda x: re.search(str(x), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_id_exist]

    if df_filtered.shape[0] != 1:
        return None

    return df_filtered["indentyfikator_krajowy"].iloc[0]


def retrive_organisation_id(row):
    
    intro_text = row['intro']

    does_not_id_exist = (
        knf_df["identyfikator_krajowy_funduszu"]
        .apply(lambda register_id: re.search(str(register_id), intro_text))
        .isna()
    )
    df_filtered = knf_df[~does_not_id_exist]

    if df_filtered.shape[0] != 1:
        return None

    return df_filtered["identyfikator_krajowy_funduszu"].iloc[0]