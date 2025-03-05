# Lesson 1: Python Sets - Engage & Apply + Final Challenge

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Pre-provided Exercise: Create a set from a list with duplicates, convert it to a set, and print both the list and the set.
# This demonstrates how sets automatically remove duplicates.

# List with duplicate items
hobbies = ['reading', 'gaming', 'hiking', 'gaming', 'swimming', 'hiking']

# Convert the list into a set to remove duplicates
hobbies_set = set(hobbies)

# Print the original list and the resulting set
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)

# ===========================
# engage and apply ---------> Exercise 2 pre-provided
# ===========================

# Pre-provided Exercise: Loop through a set of your favorite books or movies.
# Since sets are unordered, the order of output may vary each time you run the code.

favorite_movies = {'Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Gladiator'}

# Loop through the set and print each movie
for movie in favorite_movies:
    print(movie)

# ===========================
# engage and apply ---------> Exercise 3 My Version Created
# ===========================

# My Version: Create a set of your favorite foods, add a new food item, and check if a specific food is in the set.

foods = {'pizza', 'sushi', 'pasta', 'ice cream'}

# Add a new food item to the set
foods.add('burger')

# Check if 'pasta' is in the set and print the result
print('pasta' in foods)  # Expected Output: True

# Print the modified set
print(foods)

# ===========================
# engage and apply ---------> Exercise 4 pre-provided
# ===========================

# Pre-provided Exercise: Compare two sets to check if one is a subset or superset of the other.

set1 = {'basketball', 'soccer', 'tennis'}
set2 = {'basketball', 'soccer'}

# Check if set2 is a subset of set1
print(set2.issubset(set1))  # Expected Output: True

# Check if set1 is a superset of set2
print(set1.issuperset(set2))  # Expected Output: True

# ===========================
# engage and apply ---------> Exercise 5 My Version Created
# ===========================

# My Version: Create two sets of your favorite vacation destinations and perform union, intersection, and difference operations.

set1 = {'Paris', 'Tokyo', 'New York'}
set2 = {'London', 'Paris', 'Rome'}

# Union: Combine all unique destinations from both sets
print("All Unique Destinations:", set1.union(set2))  # Expected Output: {'Paris', 'Tokyo', 'New York', 'London', 'Rome'}

# Intersection: Find common destinations
print("Common Destinations:", set1.intersection(set2))  # Expected Output: {'Paris'}

# Difference: Find destinations unique to set1
print("Destinations in set1:", set1.difference(set2))  # Expected Output: {'New York', 'Tokyo'}

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Pre-provided Final Challenge: Clean and deduplicate two email lists, remove duplicates, find common emails, 
# and show unique emails from each list.

def clean_email_lists(list1, list2):
    # Convert both lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    
    # All unique emails (union of both sets)
    all_unique = set1.union(set2)
    print("All Unique Emails:", all_unique)
    
    # Common emails (intersection of both sets)
    common_emails = set1.intersection(set2)
    print("Emails in both lists:", common_emails)
    
    # Emails unique to each list (symmetric difference)
    unique_emails = set1.symmetric_difference(set2)
    print("Emails Unique to Each List:", unique_emails)

# Example email lists
email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

# Call the function with the example email lists
clean_email_lists(email_list1, email_list2)

# ===========================
# final challenge ---------> My Version Created
# ===========================

# My Version: Create two email lists, clean them, and find unique and common emails between the lists.

email_list1 = ['alice@example.com', 'bob@example.com', 'alice@example.com', 'charlie@example.com']
email_list2 = ['bob@example.com', 'david@example.com', 'alice@example.com', 'emily@example.com']

# Call the function with the new email lists
clean_email_lists(email_list1, email_list2)
