# Lesson 1: Introduction to Python Sets

# Overview:
# In this lesson, we explore Python sets, a collection data type that stores unique elements. 
# Sets are unordered, meaning their elements do not have a defined order, and they automatically 
# remove duplicate items. Sets are particularly useful when we need to eliminate duplicates 
# and perform set operations like union, intersection, and difference.

# Key Concepts:

# 1. **Creating a Set**:
# Sets can be created in several ways:
# - Using curly braces {} with comma-separated values:
my_set = {1, 2, 3, 4}
# - Using the set() constructor to create an empty set or convert other iterables:
empty_set = set()  # Creates an empty set
list_set = set([1, 2, 2, 3])  # Converts a list to a set and removes duplicates
print(list_set)  # Output: {1, 2, 3}

# 2. **Adding and Removing Items**:
# Sets allow you to add elements using the .add() method and remove them using .remove() or .discard().
my_set.add(5)  # Adds 5 to the set
print(my_set)  # Output: {1, 2, 3, 4, 5}

# The .remove() method will raise a KeyError if the item is not found, while .discard() won't.
my_set.remove(3)  # Removes 3 from the set
print(my_set)  # Output: {1, 2, 4, 5}

# 3. **Set Operations**:
# Sets support several useful operations like union, intersection, and difference.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: Combines two sets and removes duplicates.
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Returns the elements that are common in both sets.
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}

# Difference: Returns elements that are in set1 but not in set2.
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# 4. **Membership Test**:
# You can check if an element exists in a set using the 'in' keyword:
print(3 in set1)  # Output: True
print(7 in set1)  # Output: False

# 5. **Set Methods**:
# Sets come with useful methods such as .add(), .remove(), .discard(), .pop(), .clear(), .copy(), etc.
# - .pop() removes and returns an arbitrary element (since sets are unordered).
# - .clear() removes all elements from the set.
# - .copy() creates a shallow copy of the set.

# 6. **Set Comprehension**:
# Similar to list comprehension, you can create sets using a set comprehension:
squared_set = {x ** 2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}

# 7. **Frozen Sets**:
# A frozen set is an immutable version of a set. You cannot add or remove elements from a frozen set.
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})

# Final Challenge:
# The final challenge helps reinforce your understanding of sets by requiring you to:
# - Create sets, add elements, check for membership, and perform set operations like union, intersection, and difference.
# - You will also practice using some of the useful set methods like .add(), .remove(), and .pop().
