
from Webpage import copy_text, find_links, unique_links
from Heap import init_list_elements, init_queue, update_element_by_string, add_element, enqueue, dequeue
from HashTable import init_hash_table, is_string_in_hash_table, insert_string, remove_string
from Graph import graph


def add_subjects_to_queue(subjects, hash_table, Heap, elements, graph, current_subject, seen):

    i = 0
    for subject in subjects:
        if is_string_in_hash_table(subject, hash_table):
            print()
            update_element_by_string(subject, i + 1, Heap)
            graph.add_edge(subject, current_subject, weight=1)
        else:
            new_element = (1, i + 1, subject)
            if is_string_in_hash_table(subject, seen):
                continue
            else:
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
Seen = init_hash_table()

Graph = graph()

prefix = "https://en.wikipedia.org/wiki/"
Current_subject = "Stock_market"
url = prefix + Current_subject

"""
# copia texto completo da pagina
text = copy_text(url)
"""

while url:

    print("\n|||||||||||||||||||||||||| " + Current_subject + " ||||||||||||||||||||||||||" )

    insert_string(Current_subject, Seen)

    # encontra link na pagina
    links = find_links(url)

    # elimina links repetidos
    links = unique_links(links)

    Subjects = [link.replace("https://en.wikipedia.org/wiki/", "") for link in links]

    """
    for subject in Subjects:
        print(subject)
    """

    add_subjects_to_queue(Subjects, hash_table, Heap, elements,Graph, Current_subject, Seen)

    next_subject = dequeue(Heap)

    Current_subject = next_subject[2]

    remove_string(Current_subject, hash_table)

    url = prefix + Current_subject

    print(Heap)


graph.plot_graph()



















