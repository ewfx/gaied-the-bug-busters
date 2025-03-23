import re

class EmailExtractor:
    def extract_fields(self, text: str):
        patterns = {
            "deal_name": r"Deal Name:\s*(\S+)",
            "amount": r"Amount:\s*\$?([\d,]+)",
            "expiration_date": r"Expiration Date:\s*(\S+)"
        }
        extracted = {key: re.search(pattern, text).group(1) if re.search(pattern, text) else None for key, pattern in patterns.items()}
        return extracted

email_extractor = EmailExtractor()