import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))
import logging
import os
import fitz
import pandas as pd
from lib.constants import (
    RAW_KIIDS_DIR,
    PARSED_PDFS_FRAME_COLUMNS,
    SECTIONS_NAMES,
    PARSED_KIIDS_DIR,
    META_FILE_PATH,
)
from lib.pdf_process import split_text_into_sections, get_srri_from_pdf
from lib.utils import transform_pdf_to_html

logger = logging.getLogger(__name__)


def main():
    metadata = pd.read_csv(META_FILE_PATH)
    df = pd.DataFrame(columns=PARSED_PDFS_FRAME_COLUMNS)
    for index, row in metadata.iterrows():
        id = row["ID_KIID"]
        filename = row["NAZWA_PLIKU"]
        path = RAW_KIIDS_DIR / filename
        logger.info(f"Processing {id} - {path}")
        try:
            extracted_text = ""
            with fitz.open(path) as doc:
                for page in doc:
                    extracted_text += page.get_text()
            sections = split_text_into_sections(extracted_text, filename)
            html_pdf = transform_pdf_to_html(path)
            srri = get_srri_from_pdf(html_pdf, filename)
            row_dict = {
                section_name: section
                for section_name, section in zip(
                    ["intro"] + SECTIONS_NAMES, sections
                )
            }
            row_dict["srri"] = int(srri)
            row_dict["filename"] = filename
            row_dict["raw_text"] = extracted_text
            row_dict["id"] = id
            df = pd.concat(
                [df, pd.DataFrame(row_dict, index=[0])], ignore_index=True
            )
        except:
            logger.warning(f"Error during processing {filename}")
            pass

    output_path = PARSED_KIIDS_DIR / "kiids_parsed.parquet"
    logger.info(f"Saving output frame to {output_path}")
    df.to_parquet(output_path, index=False)


if __name__ == "__main__":
    main()
