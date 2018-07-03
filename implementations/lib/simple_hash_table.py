"""A simple hash table implementation.

This is a very helpful way to describe the hash table properties in under 5 minutes.
"""

# Concepts in Hash Table
#   Hashing Function
#   Collisions
#       Linear Probing
#       Seperate Chaining

def hash_function(key):
    """Given a key, generate a hash value to be used as index."""
    return key%10

hash_table = [None]*10

def insert(key):
    index = hash_function(key)
    hash_table[index] = key

print ("\n Simple Hash Table w/ collisions \n")

# Inserts 10 at [0]
insert(10)
print(hash_table)

# Inserts 100 at [0]
insert(100)
print(hash_table)

# Because, both 10 and 100 result in the same hashed index

# Solution 1: Linear Probing

hash_table = [None]*10

def linear_probing(key):
    """Insert at the next available slot.
    
    Worstcase: O(n)
    """
    index = hash_function(key)
    if hash_table[index]:
        while hash_table[index]:
            index += 1
            if index > len(hash_table):
                raise KeyError("Out of bounds")
        hash_table[index] = key
    else:
        hash_table[index] = key

print ("\n Linear Probing \n")

# Inserts 10 at [0]
linear_probing(10)
print(hash_table)

# Inserts 100 at [1]
linear_probing(100)
print(hash_table)

print ("\n Seperate Chaining \n")

# Solution 2: Seperate Chaining

hash_table = [[]for _ in range(10)]

def seperate_chaining(key):
    """Make each slot a linkedlist and append to the list.
    
    Worstcase: O(n/k) -> O(n)
    n - total elements
    k - length of the hash_table (available indices)
    """
    index = hash_function(key)
    hash_table[index].append(key)

# Inserts 10 at [0][0]
seperate_chaining(10)
print(hash_table)

# Inserts 100 at [0][1]
seperate_chaining(100)
print(hash_table)

print ("\n \n")