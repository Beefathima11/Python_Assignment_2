import random
random_list = [random.randint(1, 100) for _ in range(5)]
print("List of 5 random numbers:", random_list)

new_values = [101, 102, 103]
random_list.extend(new_values)
print("Updated list after adding 3 new values:", random_list)

print("Elements in the list:")
for element in random_list:
    print(element)

    person = {
        "name": "John",
        "age": 25,
        "address": "New York"
    }
    print("\nDictionary:", person)

    person["phone"] = "1234567890"
    print("Updated dictionary:", person)

    my_set = {1, 2, 3, 4, 5}
    print("\nSet:", my_set)

    my_set.add(6)
    print("Set after adding 6:", my_set)

    my_set.remove(3)
    print("Set after removing 3:", my_set)

    my_tuple = (1, 2, 3, 4)
    print("\nTuple:", my_tuple)

print("Length of the tuple:", len(my_tuple))
