# Lesson 1: Introduction to Python Sets

## Overview
In this lesson, we will explore Python sets, a collection data type that is ideal for storing unique items. Sets are unordered, mutable collections that automatically remove duplicate items. We'll cover how to create sets, manipulate them, and use key set methods such as membership checks, adding elements, and performing set operations like union, intersection, and difference.

## Key Concepts
1. **Creating Sets**
   - **Empty Set:** Created with the `set()` function.
   - **Set with Values:** Created using curly braces, e.g., `{'one', 'two', 'three'}`.
   - **Removing Duplicates:** Sets automatically remove duplicates from data structures like lists.

2. **Working with Lists, Tuples, and Dictionaries**
   - Convert lists, tuples, or dictionaries into sets to remove duplicates or manipulate their elements efficiently.

3. **Membership Check**
   - You can quickly check if an item exists in a set using the `in` keyword.

4. **Adding Items to a Set**
   - Sets are mutable, so you can add elements using the `.add()` method.

5. **Set Operations**
   - **Union:** Combines all unique elements from two sets.
   - **Intersection:** Returns elements that are common to both sets.
   - **Difference:** Returns elements found in one set but not the other.
   - **Symmetric Difference:** Returns items that are unique to each set.

6. **Advanced Set Methods**
   - **Subset & Superset Checks:** Using `issubset()` and `issuperset()` methods to compare sets.

## File Summaries

1. **notes.py**
   Contains summarized notes for the lesson, covering how to create sets, remove duplicates, perform set operations, and loop through sets.

2. **lessonOneProject.py**
   - **Engage and Apply Exercise:** 
     Create a list of your favorite hobbies, convert it into a set to remove duplicates, and compare the original list with the set.
   - **Final Challenge:**
     Write a function to deduplicate two email lists, show which emails exist in both lists, and show the emails that are unique to each list.
