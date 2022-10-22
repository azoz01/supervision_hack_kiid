import logging
from typing import List
from .constants import SECTIONS_NAMES, SPLIT_TOKEN
from .utils import insert_into_string

logger = logging.getLogger(__name__)

def split_text_into_sections(pdf_text: str, filename: str) -> List[str]:
    pdf_text_lower = pdf_text.lower()
    split_indices = {}
    for section in SECTIONS_NAMES:
        try:
            index = pdf_text_lower.index(section)
        except:
            split_indices[section] = None
            logger.warning(f"Didn't succed find {section} in {filename}")
        split_indices[section] = index
    indices_to_insert_split_token = list(split_indices.values())
    for i, index in enumerate(indices_to_insert_split_token):
        shifted_index = index + i * len(SPLIT_TOKEN)
        pdf_text = insert_into_string(pdf_text, shifted_index, SPLIT_TOKEN)
    return pdf_text.split(SPLIT_TOKEN)
