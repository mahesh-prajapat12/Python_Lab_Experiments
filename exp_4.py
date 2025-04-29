# Program to implement Lists and Tuples in Python

# --- LIST Example ---
print("=== List Example ===")
# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing elements
print("Original List:", my_list)
print("First element:", my_list[0])

# Modifying list
my_list.append(60)
print("After append(60):", my_list)

my_list[1] = 25
print("After updating second element:", my_list)

# Removing an item
my_list.remove(30)
print("After removing 30:", my_list)


# --- TUPLE Example ---
print("\n=== Tuple Example ===")
# Creating a tuple
my_tuple = (100, 200, 300, 400)

# Accessing elements
print("Original Tuple:", my_tuple)
print("First element:", my_tuple[0])

# Tuples are immutable, so the following line would cause an error:
# my_tuple[1] = 250  # Uncommenting this will raise TypeError

# Tuple operations
print("Length of tuple:", len(my_tuple))
print("Does 200 exist in tuple?", 200 in my_tuple)
