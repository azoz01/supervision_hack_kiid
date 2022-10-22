import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))
import logging
from collections import Counter
from operator import itemgetter
import pandas as pd
import spacy
from lib.constants import PARSED_KIIDS_DIR, BAG_OF_WORDS_NORM_PATH, TEAM_ID

nlp = spacy.load("pl_core_news_lg")

logger = logging.getLogger(__name__)


def main():
    df_parsed = pd.read_parquet(PARSED_KIIDS_DIR)
    final_df = pd.DataFrame(
        columns=["ID_KIID", "ID_ZESPOLU", "SLOWO", "LICZBA_WYSTAPIEN"]
    )

    for _, record_data in df_parsed.iterrows():
        logger.info(f"Processing document {record_data['id']}")
        counter = calculate_bow_counter_lemmatized(record_data["raw_text"])
        items = counter.items()
        tokens = list(map(itemgetter(0), items))
        counts = list(map(itemgetter(1), items))
        partial_df = pd.DataFrame(
            {"SLOWO": tokens, "LICZBA_WYSTAPIEN": counts}
        )
        partial_df = partial_df.assign(ID_KIID=record_data["id"])
        partial_df = partial_df.assign(ID_ZESPOLU=TEAM_ID)
        final_df = pd.concat([final_df, partial_df])

    final_df.to_csv(BAG_OF_WORDS_NORM_PATH, index=False)


def calculate_bow_counter_lemmatized(text):
    text = text.lower()
    text = nlp(text)
    lemmas = [token.lemma_ for token in text if token.is_alpha]
    return Counter(lemmas)


if __name__ == "__main__":
    main()
