import re
regex = r"planują wycofać swoje środki w ciągu \d{1,2} lat"

def get_investment_years(row):
    text = row["cele i polityka inwestycyjna"].lower()
    found = re.findall(regex, text)
    if found:
        found = found[0]
    else:
        return None
    num = int(re.findall(r"\d+", found)[0])
    return num