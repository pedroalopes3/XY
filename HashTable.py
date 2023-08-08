# Create the hash table
def init_hash_table():
    hash_table = {}
    return hash_table


# Function to add a string to the hash table
def insert_string(s, hash_table):
    if not s:
        return  # Ignore empty strings

    first_char = s[0].upper()  # Get the first character of the string and convert to uppercase

    # If the first character is not already a key in the hash table, initialize an empty list
    if first_char not in hash_table:
        hash_table[first_char] = []

    # Append the string to the corresponding list in the hash table
    hash_table[first_char].append(s)


# Function to check if a string is already in the hash table
def is_string_in_hash_table(s, hash_table):
    first_char = s[0].upper()
    if first_char in hash_table and s in hash_table[first_char]:
        return True
    return False


# Function to remove a string from the hash table
def remove_string(s, hash_table):
    first_char = s[0].upper()

    # Check if the first character is a key in the hash table
    if first_char in hash_table:
        if s in hash_table[first_char]:
            hash_table[first_char].remove(s)
            if not hash_table[first_char]:  # If the list is empty after removing the string
                del hash_table[first_char]  # Remove the key from the hash table if the list is empty


"""
# Example usage:
insert_string("apple")
insert_string("banana")
insert_string("ant")
insert_string("zebra")

print(is_string_in_hash_table("apple"))  # Output: True
print(is_string_in_hash_table("banana"))  # Output: True
print(is_string_in_hash_table("orange"))  # Output: False
print(is_string_in_hash_table("ZEBRA"))  # Output: True
print(is_string_in_hash_table("watermelon"))  # Output: False
"""