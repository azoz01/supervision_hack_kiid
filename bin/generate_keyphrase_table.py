import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from lib.check_key_phrases import check_doc
from lib.constants import KIID_WYRAZENIA, META_FILE_PATH

import pandas as pd

def create_table():
    
    df_docs = pd.read_parquet('./data/parsed/kiids_parsed.parquet')
    df_docs = df_docs.rename(columns={'filename': 'NAZWA_PLIKU'})
    df_meta = pd.read_csv(META_FILE_PATH)
    
    df_full = pd.merge(df_docs, df_meta)

    df_output = pd.DataFrame()
    for index, row in df_full.iterrows():
        df_phrase = check_doc(row)
        df_phrase['ID_KIID'] = row['ID_KIID']
        df_phrase['ID_ZESPOLU'] = 2
        df_output = pd.concat([df_output, df_phrase])
        
    df_output.to_csv(KIID_WYRAZENIA, index=False)
    

def main():
    create_table()

if __name__ == "__main__":
    main()