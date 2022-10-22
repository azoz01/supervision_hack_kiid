def insert_into_string(text: str, index: int, str_to_insert: str) -> str:
    return text[:index] + str_to_insert + text[index:]
