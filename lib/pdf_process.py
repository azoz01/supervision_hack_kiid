import logging
from collections import Counter
from bs4 import BeautifulSoup
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
            split_indices[section] = index
        except Error as e:
            logger.warning(f"Didn't succed find {section} in {filename}")
            raise e
    indices_to_insert_split_token = list(split_indices.values())
    for i, index in enumerate(indices_to_insert_split_token):
        shifted_index = index + i * len(SPLIT_TOKEN)
        pdf_text = insert_into_string(pdf_text, shifted_index, SPLIT_TOKEN)
    return pdf_text.split(SPLIT_TOKEN)


def get_srri_from_pdf(pdf_html: str, filename: str):
    soup = BeautifulSoup(pdf_html, features="html.parser")
    marks = soup.find_all()
    SRRI_POSSIBLE_VALUES = [str(i) for i in range(1, 8)]
    spans = list(filter(lambda m: m.text in SRRI_POSSIBLE_VALUES, marks))
    depth = 0
    if len(spans) > 7:
        logger.warning(f"Invalid count of srri values {len(spans)}")
        return -1
    if len(spans) < 7:
        for i in range(1, 8):
            if i not in spans:
                return i
    while depth < 5:
        styles = [span["style"] for span in spans]
        counter = Counter(styles)
        least_common_style = counter.most_common()[-1][0]
        item_with_least_common = list(
            filter(lambda s: s.get("style", "") == least_common_style, spans)
        )
        if len(item_with_least_common) == 1:
            return int(item_with_least_common[0].text)
        else:
            spans = [span.parent for span in spans]
            depth += 1
    logger.warning(f"Didn't find srri for {filename}")
    return None
