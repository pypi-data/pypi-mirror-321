# Regular expression
import re

# def convert_case(text: str, to: str = "camel") -> str:
#     """
#     Converts text between different cases: camelCase, snake_case, and PascalCase.

#     Args:
#         text (str): The input text to convert.
#         to (str): The target case ("camel", "snake", "Pascal"). Default is "camel".

#     Returns:
#         str: The text converted to the specified case.
#     """
#     # Remove special characters and split by space or underscores
#     words = re.sub(r'[^a-zA-Z0-9\s]', '', text).replace("_", " ").split()

#     if not words:
#         return ""

#     if to == "camel":
#         # Lowercase the first word, capitalize the others
#         return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
#     elif to == "snake":
#         # Join words with underscores in lowercase
#         return '_'.join(word.lower() for word in words)
    
#     elif to == "Pascal":
#         # Capitalize all words and join them
#         return ''.join(word.capitalize() for word in words)
    
#     else:
#         raise ValueError(f"Unsupported case conversion type: {to}")






    
def extract_emails(text: str) -> list:
    """
    Extracts all email addresses from a given block of text.

    Args:
        text (str): The input text containing potential email addresses.

    Returns:
        list: A list of email addresses found in the text.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def validate_url(url: str) -> bool:
    """
    Validates if a string is a valid URL.

    Args:
        url (str): The input URL string.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    url_pattern = (
        r'^(https?|ftp):\/\/'                # Protocol (http, https, ftp)
        r'([a-zA-Z0-9.-]+)'                 # Domain name
        r'(\.[a-zA-Z]{2,})'                 # Top-level domain
        r'(:\d+)?'                          # Optional port
        r'(\/[^\s]*)?$'                     # Optional path
    )
    return bool(re.match(url_pattern, url))
