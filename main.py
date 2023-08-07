import Graph
from Webpage import copy_text, find_links, unique_links
from Heap import init_list_elements, init_queue, update_element_by_string, add_element, enqueue, dequeue
from HashTable import init_hash_table, is_string_in_hash_table, insert_string


def add_subjects_to_queue(subjects, hash_table, Heap, elements):

    for i, subject in subjects:
        if is_string_in_hash_table(subject, hash_table):
            update_element_by_string(subject, i + 1, Heap)
        else:
            new_element = (1, i + 1, subject)
            insert_string(subject, hash_table)
            add_element(new_element, elements)
            enqueue(new_element, Heap)
    return 0


# inicialização da fila
elements = init_list_elements()
Heap = init_queue()
hash_table = init_hash_table()

prefix = "https://en.wikipedia.org/wiki/"
start = "Stock_market"
url = prefix + start

"""
# copia texto completo da pagina
text = copy_text(url)
"""

while url:

    # encontra link na pagina
    links = find_links(url)

    # elimina links repetidos
    links = unique_links(links)

    Subjects = [url.replace("https://en.wikipedia.org/wiki/", "") for link in links]

    add_subjects_to_queue(Subjects, hash_table, Heap, elements)

    next_subject = dequeue(Heap)

    url = prefix + next_subject[2]



















