import os
import re

from pypdf import PdfReader


PDF_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/pdfs"
    )
)

OUTPUT_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/documents"
    )
)


def clean_text(text):

    # Normalize whitespace
    text = text.replace("\n", " ")

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def ingest_pdfs():

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    for file in os.listdir(PDF_FOLDER):

        if not file.endswith(".pdf"):

            continue

        pdf_path = os.path.join(
            PDF_FOLDER,
            file
        )

        try:

            reader = PdfReader(pdf_path)

            full_text = ""

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:

                    full_text += extracted + " "

            # Clean extracted text
            full_text = clean_text(full_text)

            # Save txt file
            output_file = os.path.join(
                OUTPUT_FOLDER,
                file.replace(".pdf", ".txt")
            )

            with open(
                output_file,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(full_text)

            print(f"Ingested: {file}")

        except Exception as e:

            print(f"FAILED: {file}")

            print(e)


if __name__ == "__main__":

    ingest_pdfs()