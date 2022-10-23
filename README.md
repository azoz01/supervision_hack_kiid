# Hackhaton **Supervision**hack

## Repo structure

```
├───bin - scripts to run
├───data
│   ├───final - tables specified in task documentation
│   ├───parsed - datatables with merged pdf data
│   ├───raw - pdf before preprocessing
│   └───tmp
├───lib - functions, classes
│   └───extract_text_data - functions to create final CSV  
└───notebooks - .ipynb files with concept work
```

## How to
Proper order of running scripts in `bin`:
 ```
 - scrapper
 - generate_metadata.py
 - parse_pdfs.py
 - extract_funds_from_knf.py
 - generate_bag_of_words_raw.py
 - generate_bag_of_words_norm.py
 - generate_keyphrase_table.py
 - generate_data_from_text.py
 ```
