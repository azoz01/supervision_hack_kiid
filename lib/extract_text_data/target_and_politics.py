import spacy

nlp =spacy.load("pl_core_news_lg", exclude=["parser"])

def get_cel(row):
    text = row['cele_i_polityka']
    doc = nlp(text)
    for it, cel in enumerate(doc.sents):
        return it

    return doc.sents

def get_ncel(row):
    text = row['cele_i_polityka']
    doc = nlp(text)
    polityka = ' '.join([polityka for i, polityka in enumerate(doc.sents) if i!=0])
    return polityka