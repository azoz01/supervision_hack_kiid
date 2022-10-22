import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))
import logging
import os
import pandas as pd
from pdfminer.high_level import extract_text
from lib.constants import (
    RAW_KIIDS_DIR,
    PARSED_PDFS_FRAME_COLUMNS,
    SECTIONS_NAMES,
    PARSED_KIIDS_DIR,
)
from lib.pdf_process import split_text_into_sections

logger = logging.getLogger(__name__)


def main():
    files_paths = RAW_KIIDS_DIR.iterdir()
    files_paths = list(filter(lambda s: s.suffix == ".pdf", files_paths))
    logger.info(f"Files_paths: {files_paths}")
    df = pd.DataFrame(columns=PARSED_PDFS_FRAME_COLUMNS)

    for path in files_paths:
        logger.info(f"Processing {path}")
        extracted_text = extract_text(path)
        filename = path.name
        sections = split_text_into_sections(extracted_text, filename)
        row_dict = {
            section_name: section
            for section_name, section in zip(
                ["intro"] + SECTIONS_NAMES, sections
            )
        }
        row_dict["filename"] = filename
        row_dict["raw_text"] = extracted_text
        df = pd.concat(
            [df, pd.DataFrame(row_dict, index=[0])], ignore_index=True
        )

    output_path = PARSED_KIIDS_DIR / "kiids_parsed.parquet"
    logger.info(f"Saving output frame to {output_path}")
    df.to_parquet(output_path, index=False)


if __name__ == "__main__":
    main()
