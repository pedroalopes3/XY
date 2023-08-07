
from Webpage import copy_text, find_links, unique_links
from Heap import init_list_elements, init_queue, update_element_by_string, add_element, enqueue, dequeue
from HashTable import init_hash_table, is_string_in_hash_table, insert_string
from Graph import graph


def add_subjects_to_queue(subjects, hash_table, Heap, elements, graph, current_subject):

    i = 0
    for subject in subjects:
        if is_string_in_hash_table(subject, hash_table):
            update_element_by_string(subject, i + 1, Heap)
            graph.add_edge(subject, current_subject, weight=1)
        else:
            new_element = (1, i + 1, subject)
            insert_string(subject, hash_table)
            graph.add_node(subject)
            graph.add_edge(subject,current_subject, weight=1)
            add_element(new_element, elements)
            enqueue(new_element, Heap)
    i = i + 1
    return 0


# inicialização da fila
elements = init_list_elements()
Heap = init_queue()
hash_table = init_hash_table()

Graph = graph()

prefix = "https://en.wikipedia.org/wiki/"
Current_subject = "Stock_market"
url = prefix + Current_subject

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

    add_subjects_to_queue(Subjects, hash_table, Heap, elements,Graph, Current_subject)

    next_subject = dequeue(Heap)

    Current_subject = next_subject[2]

    url = prefix + Current_subject


graph.plot_graph()



















