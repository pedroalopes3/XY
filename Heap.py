import heapq

"""
# Example elements: (first_int, second_int, string_value)
elements = [(3, 5, "A"), (1, 2, "B"), (2, 1, "C"), (3, 1, "D")]
"""

# Custom comparison function to determine priority
def custom_priority(item):
    return (-item[0], item[1])

# Create an empty list to serve as the min-heap
def init_queue():
    priority_queue = []
    return priority_queue

# Function to add elements to the priority queue
def enqueue(item,priority_queue):
    heapq.heappush(priority_queue, item)

# Function to remove and return the most priority element from the priority queue
def dequeue(priority_queue):
    if not priority_queue:
        raise IndexError("Priority queue is empty.")
    return heapq.heappop(priority_queue)


# Function to update the integers in an element based on the string component
def update_element_by_string(old_string, new_second_int, priority_queue):
    # Find the old element based on the string
    i = 0

    for element in priority_queue:
        """ 
        print("\n")
        print(element)
        """
        if element[2] == old_string:
            break
        i = i + 1
    else:
        raise ValueError(f"Element with string '{old_string}' not found in the priority queue.")

    # Remove the old element
    old_element = priority_queue.pop(i)

    # Update the integers in the element
    if new_second_int < old_element[1]:
        updated_element = (old_element[0] + 1, new_second_int, old_element[2])
    else:
        updated_element = (old_element[0] + 1, old_element[1], old_element[2])

    # Add the updated element back to the priority queue
    enqueue(updated_element, priority_queue)


# Function to add elements to the priority queue
def add_element(new_element, elements):
    elements.append(new_element)


"""
# Example usage:
for element in elements:
    enqueue(element)

while priority_queue:
    element = dequeue()
    print(element)
"""

# create a elements list
def init_list_elements():
    elements = []
    return elements



