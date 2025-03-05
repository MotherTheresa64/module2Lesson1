# Lesson 1: Introduction to Python Sets

# Overview:
# Sets are a special collection data type in Python, used for storing unique items. They are unordered, mutable, 
# and automatically remove duplicate elements. Sets do not support indexing, so you cannot access items by index.
# Instead, you can loop through sets or check for membership.

# 1. Creating Sets:
# To create a set, use curly braces or the `set()` function.

# Example 1: Creating an empty set
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

# Example 2: Creating a set with values (duplicates are automatically removed)
new_set = {'one', 'two', 'three'}
print(new_set)  # Output: {'one', 'two', 'three'}

# 2. Working with Lists, Tuples, and Dictionaries:
# Sets are helpful for removing duplicates from other collections like lists, tuples, or dictionaries.

# Example: Converting a list to a set
alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)
print(set_list)  # Output: {'stuff', 'item', 'thing', 'oddity'}

# 3. Looping Over Sets:
# Since sets are unordered, you can't use indexing to access their elements.
# However, you can iterate over a set using a for loop.

# Example: Looping over a set
aset = {'apple', 'orange', 'banana'}
for fruit in aset:
    print(fruit)  # Order may vary

# 4. Set Methods:
# Python provides several useful methods to work with sets.

# Membership Checks:
# Use the `in` keyword to check if an element exists in a set.

my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
print('superman' in my_set)  # Output: True
print('spiderman' in my_set)  # Output: False

# Adding Items to a Set:
# You can add elements to a set using the `.add()` method.
my_set.add('green lantern')
print(my_set)  # Output: {'superman', 'batman', 'wonder woman', 'the flash', 'green lantern'}

# 5. Advanced Set Methods:
# Comparing sets or performing operations on them is easy in Python.

# Subset and Superset:
# - `issubset()`: Check if all elements of one set are in another.
# - `issuperset()`: Check if one set contains all elements of another.

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

# Set Operations:
# - Union: Combines all unique items from two sets.
# - Intersection: Returns only the items both sets have in common.
# - Difference: Returns the items in one set but not the other.
# - Symmetric Difference: Returns items unique to each set.

set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}

# Union
print(set3.union(set4))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set3.intersection(set4))  # Output: {3, 4}

# Difference
print(set3.difference(set4))  # Output: {1, 2}

# Symmetric Difference
print(set3.symmetric_difference(set4))  # Output: {1, 2, 5, 6}

# 6. Final Challenge - Email List Deduplication:
# We can use sets to handle tasks such as deduplicating email lists or finding common emails between two lists.

def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    # Remove duplicates and merge
    all_unique = set1.union(set2)
    print("All unique emails:", all_unique)

    # Common emails
    common_emails = set1.intersection(set2)
    print("Emails in both lists:", common_emails)

    # Emails unique to each list
    unique_emails = set1.symmetric_difference(set2)
    print("Emails unique to each list:", unique_emails)

# Example usage
email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)
