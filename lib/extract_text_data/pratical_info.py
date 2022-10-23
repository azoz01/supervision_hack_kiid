import pandas as pd
import re

def split_text(text: str) -> list:
    text = text.replace('\n\n', '<p>')
    text = ' '.join(text.split())
    text = text.replace('<p>', '\n')
    # text = text.lower()
    return text

def get_depo(text: str) -> str or None:
    regex = depo_regex.search(text)
    if regex is None:
        return None
    else:     
        if not_depo_regex.search(regex.group(2)):
            return None
        
        if regex.group(3) is not None:
            return regex.group(2) + regex.group(3)
        else:
            return regex.group(2)

def get_depositary(row) -> str:
    
    text = row['informacje praktyczne']
    
    text = split_text(text)
        
    return get_depo(text)
    
def get_krs(row) -> str:
    text = row['informacje praktyczne']
    text = split_text(text)   
    
    krs_regex = re.compile('(krs:?\s*)([0-9]{9})', re.IGNORECASE)
    regex = krs_regex.search(text)
    if regex is None:
        return None
    else:
        return regex.group(2)
    
def get_nip(row) -> str:
    text = row['informacje praktyczne']
    text = split_text(text)   
    
    nip_regex = re.compile('(nip:?\s*)([0-9\-]*)(\s|\.|,)', re.IGNORECASE)   
    regex = nip_regex.search(text)
    if regex is None:
        return None
    else:
        return regex.group(2) 
    
def get_address(row) -> str:
    text = row['informacje praktyczne']
    text = split_text(text)   
    
    address_regex = re.compile('(ul\.\s\w+\s\d{1,3},?\s\d{2}-\d{3}\s\w+)')
    
    regex = address_regex.search(text)
    if regex is None:
        return None
    else:
        return regex.group(1)    
    
def get_capital(row) -> str:
    text = row['informacje praktyczne']
    text = split_text(text)      
    
    capital_regex = re.compile('zakładowy:?.{,20}([\d\s,]+)', re.IGNORECASE)
    
    regex = capital_regex.search(text)
    
    if regex is None:
        return None
    else:
        return regex.group(1)
    
def get_currency(row) -> str:
    text = row['informacje praktyczne']
    text = split_text(text)      
    
    currency_regex = re.compile('(przedstawiono\sw\s)(\w{3})', re.IGNORECASE)
    
    regex = currency_regex.search(text)
    if regex is None:
        return None
    else:
        return regex.group(2)     
    
def get_esg(row) -> str:
    text = row['informacje praktyczne']
    text = split_text(text)   
    
    esg_regex = re.compile('esg' , re.IGNORECASE)
    not_esg_regex = re.compile('.{0,10}nie.{0,10}esg.{0,10}nie.{0,10}')  
    
    regex = esg_regex.search(text)
    
    if regex is None:
        return False
    else:
        not_regex = not_esg_regex.search(text)
        if not_regex is None:
            return False
        return True
    
def get_type(row) -> str:
    text = row['raw_text']
    text = split_text(text)  
    
    type_regex = re.compile('(S?FIO)')
    
    regex = type_regex.search(text)
    
    if regex is None:
        return None
    else:
        return regex.group(1) 
    
def get_isin(row) -> str:
    text = row['raw_text']
    text = split_text(text)  
    
    isin_regex = re.compile('(\w{2}[\w\d]{9}\d)', re.IGNORECASE)    
    
    regex = isin_regex.search(text)
    
    if regex is None:
        return None
    else:
        return regex.group(1)    
    
def get_previous_scoring_desc(row) -> str:
    text = row['wyniki osiągnięte w przeszłości']
    return split_text(text)

def get_first_date(row) -> str:
    text = row['wyniki osiągnięte w przeszłości']
    text = split_text(text)
    
    first_date_regex = re.compile('((tworzon|ceni)).+(\d{4})\w?r?\.?')
    
    regex = first_date_regex.search(text)
    
    if regex is None:
        return None
    else:
        return regex.group(3)
    