import pandas as pd

def retrive_register_id(knf_df: 'pd.DataFrame', intro_text: str) -> int:
    
    does_not_id_exist = knf_df['nr_w_rejestrze'].apply(lambda register_id: re.search(str(register_id) , intro_text)).isna()
    df_filtered = knf_df[~ does_not_id_exist]

    if len(df_filtered['nr_w_rejestrze'].unique()) > 1:
        return None
    
    return df_filtered['nr_w_rejestrze'].iloc[0]

def retrive_fund_name(knf_df: 'pd.DataFrame', intro_text: str) -> str:

    does_not_name_exist = knf_df['fundusz'].apply(lambda register_id: re.search(str(register_id) , intro_text)).isna()
    df_filtered = knf_df[~ does_not_id_exist]

    fund_name = df_filtered['fundusz'].sort_values(key=lambda x: x.str.len(), ascending=False).iloc[0]

    return fund_name
   
def retrive_subfund_name(knf_df: 'pd.DataFrame', intro_text: str) -> str:

    does_not_name_exist = knf_df['subfundusz'].apply(lambda register_id: re.search(str(register_id) , intro_text)).isna()
    df_filtered = knf_df[~ does_not_id_exist]

    fund_name = df_filtered['subfundusz'].sort_values(key=lambda x: x.str.len(), ascending=False).iloc[0]

    return fund_name

def retrive_organisation_name(knf_df: 'pd.DataFrame', intro_text: str) -> str:

    does_not_name_exist = knf_df['towarzystwo'].apply(lambda register_id: re.search(str(register_id) , intro_text)).isna()
    df_filtered = knf_df[~ does_not_id_exist]

    fund_name = df_filtered['towarzystwo'].sort_values(key=lambda x: x.str.len(), ascending=False).iloc[0]

    return fund_name

def retive_all_info(knf_df: 'pd.DataFrame', intro_text: str) -> str:
    fund_name = retrive_fund_name(knf_df, intro_text)
    subfund_name = retrive_subfund_name(knf_df, intro_text)
    organisation_name = retrive_organisation_name(knf_df, intro_text)
    register_id = retrive_register_id(knf_df, intro_text)

    return {
        'fund_name': fund_name,
        'subfund_name': subfund_name,
        'organisation_name': organisation_name,
        'register_id': register_id
    }



def main(
    df_knf_path: str = './../data/knf_funds.pkl'
):
    knf_df = pd.read_pickle(df_knf_path)
    

if __name__ == "__main__":
    main()