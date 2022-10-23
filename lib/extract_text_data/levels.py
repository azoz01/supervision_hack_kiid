import re
import spacy

nlp = spacy.load("pl_core_news_lg")


def get_min_udzialowa(row):
    text = row["cele i polityka inwestycyjna"]
    doc = nlp(text)
    percent_regex = r"\d{1,3}%"
    filtered_sents = [sent for sent in doc.sents if "udziałow" in str(sent)]
    min_percent = float("inf")
    for sent in filtered_sents:
        percents = re.findall(percent_regex, str(sent))
        percents = list(map(lambda s: int(s[:-1]), percents))
        min_percent = min(percents + [min_percent])
    if min_percent is float("inf"):
        min_percent = None
    return min_percent


def get_max_udzialowa(row):
    text = row["cele i polityka inwestycyjna"]
    doc = nlp(text)
    percent_regex = r"\d{1,3}%"
    filtered_sents = [sent for sent in doc.sents if "udziałow" in str(sent)]
    max_percent = float("-inf")
    for sent in filtered_sents:
        percents = re.findall(percent_regex, str(sent))
        percents = list(map(lambda s: int(s[:-1]), percents))
        max_percent = max(percents + [max_percent])
    if max_percent is float("-inf"):
        max_percent = None
    return max_percent


def get_min_dluzna(row):
    text = row["cele i polityka inwestycyjna"]
    doc = nlp(text)
    percent_regex = r"\d{1,3}%"
    filtered_sents = [sent for sent in doc.sents if "dłuż" in str(sent)]
    min_percent = float("inf")
    for sent in filtered_sents:
        percents = re.findall(percent_regex, str(sent))
        percents = list(map(lambda s: int(s[:-1]), percents))
        min_percent = min(percents + [min_percent])
    if min_percent is float("inf"):
        min_percent = None
    return min_percent


def get_max_udzialowa(row):
    text = row["cele i polityka inwestycyjna"]
    doc = nlp(text)
    percent_regex = r"\d{1,3}%"
    filtered_sents = [sent for sent in doc.sents if "dłuż" in str(sent)]
    max_percent = float("-inf")
    for sent in filtered_sents:
        percents = re.findall(percent_regex, str(sent))
        percents = list(map(lambda s: int(s[:-1]), percents))
        max_percent = max(percents + [max_percent])
    if max_percent is float("-inf"):
        max_percent = None
    return max_percent


def get_min_tyt_udz(row):
    text = row["cele i polityka inwestycyjna"]
    doc = nlp(text)
    percent_regex = r"\d{1,3}%"
    filtered_sents = [
        sent for sent in doc.sents if "tyt" in str(sent) and "ucz" in str(sent)
    ]
    min_percent = float("inf")
    for sent in filtered_sents:
        percents = re.findall(percent_regex, str(sent))
        percents = list(map(lambda s: int(s[:-1]), percents))
        min_percent = min(percents + [min_percent])
    if min_percent is float("inf"):
        min_percent = None
    return min_percent

def get_max_tyt_udz(row):
    text = row["cele i polityka inwestycyjna"]
    doc = nlp(text)
    percent_regex = r"\d{1,3}%"
    filtered_sents = [
        sent for sent in doc.sents if "tyt" in str(sent) and "ucz" in str(sent)
    ]
    max_percent = float("-inf")
    for sent in filtered_sents:
        percents = re.findall(percent_regex, str(sent))
        percents = list(map(lambda s: int(s[:-1]), percents))
        max_percent = max(percents + [max_percent])
    if max_percent is float("inf"):
        max_percent = None
    return max_percent