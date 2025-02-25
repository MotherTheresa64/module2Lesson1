# ## Exercise 1: Practice Creating Sets ------------------------->

# 1. Create a list of your favorite hobbies, making sure to repeat a few of them.
# 2. Convert the list into a set to automatically remove the duplicates.
# 3. Print both the original list and the set to compare.

hobbies = ["reading", "writing", "swimming", "reading", "cooking", "swimming", "hiking", "swimming"]
hobbies_set = set(hobbies)
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)

# ## Exercise 2: Loop Through a Set ------------------------->

# 1. Create a set of your top 5 favorite books or movies.
# 2. Write a for loop to print each item in the set.

favorite_movies = {"Inception", "The Matrix", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction"}
for movie in favorite_movies:
    print(movie)

# ## Exercise 3: Set Modification Practice ------------------------->

# 1. Create a set of at least 4 of your favorite foods.
# 2. Add one more food item to the set.
# 3. Write code to check if a specific food item is in the set, then print the result.

favorite_foods = {"pizza", "sushi", "tacos", "pasta"}
favorite_foods.add("burger")
food_to_check = "sushi"
if food_to_check in favorite_foods:
    print(f"Yes, {food_to_check} is in the set.")

# ## Exercise 4: Comparing Sets ------------------------->

# 1. Create two sets of your favorite sports or hobbies.
# 2. Check if one set is a subset of the other.
# 3. Check if one set is a superset of the other.

set1 = {"reading", "writing", "swimming"}
set2 = {"reading", "swimming", "hiking"}
print(set1.issubset(set2))  # Is set1 a subset of set2?
print(set1.issuperset(set2))  # Is set1 a superset of set2?


# ## Exercise 5: Working with Set Operations ------------------------->

# 1. Create two sets of your favorite vacation destinations.
# 2. Use union to find all the unique destinations.
# 3. Use intersection to find common destinations.
# 4. Use difference to find destinations unique to one of your sets.

vacation_set1 = {"Paris", "Tokyo", "Rome", "Bali"}
vacation_set2 = {"Tokyo", "Bali", "New York", "London"}
unique_destinations = vacation_set1.union(vacation_set2)
common_destinations = vacation_set1.intersection(vacation_set2)
unique_set1 = vacation_set1.difference(vacation_set2)

# ## Final Challenge: Email List Deduplication ------------------------->

# You have two email lists, but some people may be in both. Write a function to:
# 1. Remove duplicates.
# 2. Show which emails exist in both lists.
# 3. Show emails that are unique to each list.

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

email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)


