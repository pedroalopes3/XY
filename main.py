import Graph
import Heap
from Webpage import copy_text, find_links, unique_links

prefix = "https://en.wikipedia.org/wiki/"
start = "Stock_market"
url = prefix + start

# copia texto completo da pagina
text = copy_text(url)

# encontra link na pagina
links = find_links(url)

# elimina links repetidos
links = unique_links(links)

# Print the new list with repeated entries eliminated
for link in links:
    print(link)

