import Graph
import Heap
from Webpage import copy_text, find_links, unique_links
from Heap import init_list_elements, init_queue
from HashTable import init_hash_table, is_string_in_hash_table, insert_string

prefix = "https://en.wikipedia.org/wiki/"
start = "Stock_market"
url = prefix + start

# copia texto completo da pagina
text = copy_text(url)

# encontra link na pagina
links = find_links(url)

# elimina links repetidos
links = unique_links(links)



"""
# Print the new list with repeated entries eliminated
for link in links:
    print(link)
"""
# retira o prefixo "https://en.wikipedia.org/wiki/" nos links
Subjects = [url.replace("https://en.wikipedia.org/wiki/", "") for link in links]


elements = init_list_elements()
Heap = init_queue()
hash_table = init_hash_table()
for subject in Subjects:
    if is_string_in_hash_table(subject,hash_table):

    else:
        insert_string(subject,hash_table)


fila = init_list_elements()
for link in links:




