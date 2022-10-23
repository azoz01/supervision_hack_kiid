import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pl_core_news_lg", exclude=["parser"])

pattern = [{"LOWER": "nie"}, {"LEMMA": "wypłaca"}, {"OP": "?"}, {}]


def get_dywidenda(row):
    matcher = Matcher(nlp.vocab)
    cele_i_polityka = row["cele i polityka inwestycyjna"]
    doc = nlp(cele_i_polityka)
    dyws = []
    matcher.add("cele i polityka inwestycyjna", [pattern])
    matches = matcher(doc)
    for match in matches:
        dyws.append(doc[match[1] : match[2]])
    if len(dyws) > 0:
        return False
    return True
