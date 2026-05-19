import os
import re


DOCUMENTS_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/documents"
    )
)

TICKER_MAP = {
    "AAPL": "apple",
    "NVDA": "nvidia",
    "TSLA": "tesla"
}

RISK_KEYWORDS = [

    "risk",

    "supply chain",

    "supplier",

    "manufacturing",

    "competition",

    "cybersecurity",

    "privacy",

    "regulation",

    "economic",

    "china",

    "tariff",

    "geopolitical",

    "disruption",

    "inflation",

    "market risk",

    "global operations",

    "foreign exchange"
]


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_sec_filings(ticker):

    company_name = TICKER_MAP.get(
        ticker.upper(),
        ticker.lower()
    )

    retrieved_chunks = []

    if not os.path.exists(DOCUMENTS_PATH):

        return []

    for file in os.listdir(DOCUMENTS_PATH):

        if not file.endswith(".txt"):

            continue

        if company_name not in file.lower():

            continue

        file_path = os.path.join(
            DOCUMENTS_PATH,
            file
        )

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            text = clean_text(text)

            # Better chunking
            chunks = re.split(
                r'(?<=[.!?]) +',
                text
            )

            for chunk in chunks:

                chunk_lower = chunk.lower()

                # Risk-focused retrieval
                if any(

                    keyword in chunk_lower

                    for keyword in RISK_KEYWORDS
                ):

                    # Ignore tiny chunks
                    if len(chunk.strip()) > 120:

                        retrieved_chunks.append(
                            chunk.strip()
                        )

        except Exception as e:

            print(f"SEC TOOL ERROR: {e}")

    # Remove duplicates
    unique_chunks = list(
        dict.fromkeys(retrieved_chunks)
    )

    return unique_chunks[:10]