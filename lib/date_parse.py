import re
from datetime import date

MONTHMAP = {
    'styczeń': 1,
    'stycznia': 1,
    'luty': 2,
    'lutego': 2,
    'marzec': 3,
    'marca': 3,
    'kwiecień':4,
    'kwietnia':4,
    'maj': 5,
    'maja': 5,
    'czerwiec':6,
    'czerwca':6,
    'lipiec':7,
    'lipca':7,
    'sierpień':8,
    'sierpnia':8,
    'wrzesień':9,
    'września':9,
    'październik':10,
    'października':10,
    'listopad': 11,
    'listopada': 11,
    'grudzień': 12,
    'grudnia': 12
}

def get_dates_from_text(text):
    dates_str = re.findall(r'\d{1,2}\W\w+\W20[012]\d', text)
    dates_split = [re.split(r'\W', date_) for date_ in dates_str]
    dates_date = []
    for date_ in dates_split:
        if not (date_[0] and date_[1] and date_[2]):
            continue
        try:
            month = MONTHMAP[date_[1]] if date_[1] in MONTHMAP else int(date_[1])
        except:
            continue
        if month > 12 or month < 1:
            continue
        try:
            cur_date = date(
                int(date_[2]),
                month,
                int(date_[0])
            )
            dates_date.append(cur_date)
        except:
            continue
    return dates_date

def get_dates_from_row(row):
    text = row['']
    dates_str = re.findall(r'\d{1,2}\W\w+\W20[012]\d', text)
    dates_split = [re.split(r'\W', date_) for date_ in dates_str]
    dates_date = []
    for date_ in dates_split:
        if not (date_[0] and date_[1] and date_[2]):
            continue
        try:
            month = MONTHMAP[date_[1]] if date_[1] in MONTHMAP else int(date_[1])
        except:
            continue
        if month > 12 or month < 1:
            continue
        try:
            cur_date = date(
                int(date_[2]),
                month,
                int(date_[0])
            )
            dates_date.append(cur_date)
        except:
            continue
    return dates_date