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
    heapq.heappush(priority_queue, (custom_priority(item), item))

# Function to remove and return the most priority element from the priority queue
def dequeue(priority_queue):
    if not priority_queue:
        raise IndexError("Priority queue is empty.")
    return heapq.heappop(priority_queue)[1]

# Example usage:
for element in elements:
    enqueue(element)

while priority_queue:
    element = dequeue()
    print(element)

def init_list_elements():
    elements = []
    return elements

def insert in queue


