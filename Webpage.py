import requests
from bs4 import BeautifulSoup
import re


# copia texto completo da pagina
def copy_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        page_text = soup.get_text()
        return page_text
    except requests.exceptions.RequestException as e:
        print("Error: Coundn't copy text ", e)

# encontra links na pagina
def find_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", href=re.compile(r"^/wiki/[^:]+$"))

        buffer = []
        # Extract and print links of the form "https://en.wikipedia.org/wiki/(...)"
        for link in links:
            href = link.get("href")
            if href.startswith("/wiki/"):
                buffer.append(f"https://en.wikipedia.org{href}")
        return buffer

    except requests.exceptions.RequestException as e:
        print("Error: find links", e)

# elimina links repetidos
def unique_links(links):

    # Initialize a new list to store unique entries
    unique_links1 = []

    # Loop through the original list and add unique entries to the new list
    for link in links:
        if link not in unique_links1:
            unique_links1.append(link)
    return unique_links1
