
from Webpage import copy_text, find_links, unique_links
from Heap import init_list_elements, init_queue, update_element_by_string, add_element, enqueue, dequeue
from HashTable import init_hash_table, is_string_in_hash_table, insert_string, remove_string
from Graph import WeightedGraph


def add_subjects_to_queue(subjects, hash_table, Heap, elements, graph, current_subject, seen, mode):

    if mode == 1:
        i = 0
        for subject in subjects:
            if is_string_in_hash_table(subject, hash_table):
                update_element_by_string(subject, i + 1, Heap)
                graph.add_edge(subject, current_subject, weight=1)
            else:
                new_element = (1, i + 1, subject)
                if is_string_in_hash_table(subject, seen):
                    continue
                else:
                    insert_string(subject, hash_table)
                    graph.add_node(subject)
                    graph.add_edge(subject, current_subject, weight=1)
                    add_element(new_element, elements)
                    enqueue(new_element, Heap)
            i = i + 1
        return 0

    if mode == 2:
        i = 0
        for subject in subjects:
            if is_string_in_hash_table(subject, hash_table):
                continue
            else:
                new_element = (1, i + 1, subject)
                if is_string_in_hash_table(subject, seen):
                    continue
                else:
                    insert_string(subject, hash_table)
                    graph.add_node(subject)
                    graph.add_edge(subject, current_subject, weight=1)
                    add_element(new_element, elements)
                    enqueue(new_element, Heap)
                    break
            i = i + 1
        for subject in subjects:
            if is_string_in_hash_table(subject, seen):
                if subject == current_subject or subject == "Main_Page" or current_subject == "Main_Page":
                    continue
                else:
                    graph.add_edge(subject, current_subject, weight=1)
        return 0


# inicialização da fila
elements = init_list_elements()
Heap = init_queue()
hash_table = init_hash_table()
Seen = init_hash_table()

Graph = WeightedGraph()

prefix = "https://en.wikipedia.org/wiki/"
Current_subject = "Stock_market"
url = prefix + Current_subject


"""
mode:
1 - verifica todos os links nao visto na pagina
2 - vai apenas ao primeiro nao visto na pagina
"""
mode = 2


"""
# copia texto completo da pagina
text = copy_text(url)
"""

count = 0
while url and (count < 100):

    print("\n||||||||||||||||||||||||| " + str(count) + " | " + Current_subject + " ||||||||||||||||||||||||||" )

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

    add_subjects_to_queue(Subjects, hash_table, Heap, elements,Graph, Current_subject, Seen, mode)

    next_subject = dequeue(Heap)

    Current_subject = next_subject[2]

    remove_string(Current_subject, hash_table)

    url = prefix + Current_subject

    count = count + 1

Graph.plot_graph()



















