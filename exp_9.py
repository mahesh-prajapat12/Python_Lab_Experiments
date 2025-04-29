def test_memory_equality(val1, val2):
    # Get the memory addresses (IDs) of both values
    id_val1 = id(val1)
    id_val2 = id(val2)
    
    if id_val1 == id_val2:
        print(f"Both values ({val1} and {val2}) refer to the same memory location.")
    else:
        print(f"Values {val1} and {val2} are stored in different memory locations.")
    
# Example Test Cases
test_memory_equality(10, 10)  # Testing integers
test_memory_equality("hello", "hello")  # Testing strings
test_memory_equality(1000, 1000)  # Testing integers (larger numbers)
test_memory_equality(10, 10.0)  # Testing integer vs float
test_memory_equality("hello", "world")  # Testing different strings
