from pathlib import Path

SECTIONS_NAMES = [
    "cele i polityka inwestycyjna",
    "profil ryzyka i zysku",
    "opłaty",
    "wyniki osiągnięte w przeszłości",
    "informacje praktyczne",
]
PARSED_PDFS_FRAME_COLUMNS = ["filename", "raw_text", "intro"]
PARSED_PDFS_FRAME_COLUMNS.extend(SECTIONS_NAMES)

SPLIT_TOKEN = "<SPLIT_TOKEN>"

RAW_KIIDS_DIR = Path("data/raw")
PARSED_KIIDS_DIR = Path("data/parsed")
