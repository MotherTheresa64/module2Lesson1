# Lesson 1: Sets

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Pre-provided Exercise: Create a list with multiple items, convert it to a set, and 
# automatically remove duplicates. Print both the list and the resulting set.

alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)  # Converting list to a set
print("Original List:", alist)
print("Set with Duplicates Removed:", set_list)

# ===========================
# engage and apply ---------> Exercise 1 My Version Created
# ===========================

# My Version: Create a list with multiple hobbies, some repeated, 
# convert it to a set to remove duplicates, and print the original and the resulting set.

hobbies = ['coding', 'traveling', 'photography', 'traveling', 'reading', 'photography']
hobbies_set = set(hobbies)
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)

# ===========================
# engage and apply ---------> Exercise 2 pre-provided
# ===========================

# Pre-provided Exercise: Create a set of fruit names and loop through the set to print each element.

aset = {'apple', 'orange', 'banana'}
for fruit in aset:
    print(fruit)

# ===========================
# engage and apply ---------> Exercise 2 My Version Created
# ===========================

# My Version: Create a set of favorite books, loop through the set, 
# and print each book name.

favorite_books = {'1984', 'Brave New World', 'Fahrenheit 451', 'The Catcher in the Rye', 'To Kill a Mockingbird'}
for book in favorite_books:
    print(book)

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Pre-provided Final Challenge: Create a set with at least 6 elements, 
# add an element, check for membership, and perform set operations like union, intersection, and difference.

my_set = {'superman', 'batman', 'wonder woman', 'the flash', 'green lantern'}

# Add a new element to the set
my_set.add('aquaman')
print("Updated Set:", my_set)

# Membership check
print('superman' in my_set)  # Output: True
print('spiderman' in my_set)  # Output: False

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print("Union:", set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print("Intersection:", set1.intersection(set2))  # Output: {3, 4}

# Difference
print("Difference:", set1.difference(set2))  # Output: {1, 2}

# ===========================
# final challenge ---------> My Version Created
# ===========================

# My Version: Create a set of favorite foods, 
# add a food item, check for membership, and perform set operations like union, intersection, and difference.

foods = {'pizza', 'sushi', 'pasta', 'ice cream'}

# Add a new item to the set
foods.add('burger')
print("Updated Set:", foods)

# Membership check
print('pasta' in foods)  # Output: True
print('salad' in foods)  # Output: False

# Set Operations
set1 = {'pizza', 'sushi', 'burger'}
set2 = {'burger', 'pasta', 'ice cream'}

# Union
print("Union:", set1.union(set2))  # Output: {'pizza', 'sushi', 'burger', 'pasta', 'ice cream'}

# Intersection
print("Intersection:", set1.intersection(set2))  # Output: {'burger'}

# Difference
print("Difference:", set1.difference(set2))  # Output: {'pizza', 'sushi'}
