import requests
from bs4 import BeautifulSoup

def fetch_body_text(url):
    """
    Fetch the text inside <p> tags of the specified URL.

    Args:
    - url (str): The URL to scrape.

    Returns:
    - str: The concatenated text of all <p> tags.
    """

    # Fetch the webpage content
    response = requests.get(url)
    
    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Parse the content with Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from all <p> tags and concatenate them
    paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
    body_text = " ".join(paragraphs)



    word_count = len(body_text.split())
    char_count = len(body_text)
    return body_text.strip(), word_count, char_count

    
    
    
# Example of usage:
# body_text = fetch_body_text("https://www.example.com")
# print(body_text)

