# Wed Jul 26 16:17:34 CST 2023
## List and Set
The main difference between `vowels = ['a', 'e', 'i', 'o', 'u']` and `vowels = {'a', 'e', 'i', 'o', 'u'}` is that the first one creates a **list** and the second one creates a **set** in Python¹². A list and a set are both data structures that can store multiple values, but they have some important differences:

- A list is an **ordered** collection of values, which means that the values are stored in a specific sequence and can be accessed by their indices¹². A set is an **unordered** collection of values, which means that the values are stored in no particular order and cannot be accessed by their indices¹².
- A list can have **duplicate** values, which means that the same value can appear more than once in the list¹². A set can only have **unique** values, which means that there can be no duplicates in the set¹².
- A list is **mutable**, which means that the values in the list can be changed, added, or removed after the list is created¹². A set is also **mutable**, which means that the values in the set can also be changed, added, or removed after the set is created¹².
- A list can store any kind of values, including other lists or sets¹². A set can only store **hashable** values, which means that the values must be immutable and have a unique hash value¹³. For example, a list can store another list as a value, but a set cannot store another set as a value.

Some examples of how to create and use lists and sets are:

```python
# create a list of vowels with square brackets
vowels_list = ['a', 'e', 'i', 'o', 'u']

# access the first element of the list by its index
print(vowels_list[0]) # a

# append a new element to the end of the list
vowels_list.append('y')
print(vowels_list) # ['a', 'e', 'i', 'o', 'u', 'y']

# create a set of vowels with curly braces
vowels_set = {'a', 'e', 'i', 'o', 'u'}

# check if an element is in the set with the in operator
print('a' in vowels_set) # True

# add a new element to the set with the add method
vowels_set.add('y')
print(vowels_set) # {'a', 'e', 'i', 'o', 'u', 'y'}
```

Source: Conversation with Bing, 7/26/2023
(1) Python Set VS List – Sets and Lists in Python .... https://www.freecodecamp.org/news/python-set-vs-list/.
(2) What is the difference between sets and lists in Python?. https://stackoverflow.com/questions/12354515/what-is-the-difference-between-sets-and-lists-in-python.
(3) Python Sets Tutorial: Set Operations & Sets vs Lists | DataCamp. https://www.datacamp.com/tutorial/sets-in-python.
