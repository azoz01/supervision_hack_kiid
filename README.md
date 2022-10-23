# Hackhaton **Supervision**hack

## About

Project aims to **Extract** PDF files about TFIs' (*Towarzystwo Funduszy Inwestycyjnych*) KIID (*Key Investor Information Document*) from web, **Transform** data to structured and **Export** them as CSV files ready to load to database.

Project mostly based on **NLP** and **regular expressions**.

## Repo structure

```
├───bin - scripts to run
├───data
│   ├───final - CSV tables
│   ├───parsed - datatables with merged pdf data
│   ├───raw - pdf before preprocessing
│   └───tmp
├───lib - functions, classes
│   └───extract_text_data - functions to create CSV
└───notebooks - .ipynb files with concept work
```

## How to
Proper order of running scripts in `bin`:
 ```
 - scrappy2.py 
 - filter.py
 - generate_metadata.py
 - parse_pdfs.py
 - extract_funds_from_knf.py
 - generate_bag_of_words_raw.py
 - generate_bag_of_words_norm.py
 - generate_keyphrase_table.py
 - generate_data_from_text.py
 ```

 ## Prerequirements

 ```
# python=3.8.10
pip install -r requirements.txt
 ```
