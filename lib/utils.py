import aspose.words as aw
import shutil
from .constants import TEMPORARY_PATH


def insert_into_string(text: str, index: int, str_to_insert: str) -> str:
    return text[:index] + str_to_insert + text[index:]


def transform_pdf_to_html(path: str) -> str:
    shutil.rmtree(TEMPORARY_PATH, ignore_errors=True)
    TEMPORARY_PATH.mkdir()
    doc = aw.Document(str(path))
    doc.save(str(TEMPORARY_PATH / "temp_doc.html"))
    doc_path = TEMPORARY_PATH / "temp_doc.html"
    pdf_text = doc_path.read_text()
    shutil.rmtree(TEMPORARY_PATH, ignore_errors=True)
    return pdf_text
