import pandas as pd
import spacy
import re

nlp = spacy.load("pl_core_news_lg")
categories = ["A", "A1", "B", "B1", "C", "C1", "E"]


def get_category(row):
    text = row["raw_text"]
    doc = nlp(text)
    sents = list(doc.sents)
    filtered_sents = list(
        filter(lambda s: "kate" in str(s) or "kat." in str(s), sents)
    )
    for sent in filtered_sents:
        matched_cats = []
        for cat in categories:
            if f" {cat}" in str(sent) or f"{cat} " in str(sent):
                matched_cats.append(cat)
        if len(matched_cats) == 1:
            return matched_cats[0]
    return None
