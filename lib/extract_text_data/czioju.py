import spacy
from spacy.matcher import Matcher

pattern = [{"LOWER": "jednostek"}, {"LOWER": "uczestnictwa"}, {}, {}, {}]
CZOIJUDICT = {
    "dzień": "D",
    "tydzień": "W",
    "kwartał": "Q",
    "miesiąc": "M",
    "dziennie": "D",
    "codziennie": "D",
    "cotygodniowo": "W",
    "kwartalnie": "Q",
    "miesięcznie": "M",
}
nlp = spacy.load("pl_core_news_lg", exclude=["parser"])


def get_czioju(row):
    cele_i_polityka = row["cele i polityka inwestycyjna"]
    doc = nlp(cele_i_polityka)
    matcher = Matcher(nlp.vocab)
    czioju = []
    matcher.add("test_pat", [pattern])
    matches = matcher(doc)
    for match in matches:
        czioju.append(doc[match[1] : match[2]])
    if len(czioju) == 1:
        return CZOIJUDICT.get(czioju[0], None)
    elif len(czioju) == 0:
        return None
    else:
        return CZOIJUDICT.get(czioju[-1], None)
