# Wed Jul 26 16:17:34 CST 2023

## List and Set

The main difference between `vowels = ['a', 'e', 'i', 'o', 'u']` and `vowels = {'a', 'e', 'i', 'o', 'u'}` is that the first one creates a **list** and the second one creates a **set** in Python¹². A list and a set are both data structures that can store multiple values, but they have some important differences:

-   A list is an **ordered** collection of values, which means that the values are stored in a specific sequence and can be accessed by their indices¹². A set is an **unordered** collection of values, which means that the values are stored in no particular order and cannot be accessed by their indices¹².
-   A list can have **duplicate** values, which means that the same value can appear more than once in the list¹². A set can only have **unique** values, which means that there can be no duplicates in the set¹².
-   A list is **mutable**, which means that the values in the list can be changed, added, or removed after the list is created¹². A set is also **mutable**, which means that the values in the set can also be changed, added, or removed after the set is created¹².
-   A list can store any kind of values, including other lists or sets¹². A set can only store **hashable** values, which means that the values must be immutable and have a unique hash value¹³. For example, a list can store another list as a value, but a set cannot store another set as a value.

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

# Thu Jul 27 10:38:35 CST 2023

## `self` key word in python

-   introduce the self key word of python:
    > Sure. The `self` keyword in Python is used to refer to the current instance of a class. It is a special parameter that is passed to all methods of a class, and it can be used to access the attributes and methods of the current instance.
    >
    > For example, the following code defines a class called `Person`:
    >
    > ```python
    > class Person:
    >  def __init__(self, name, age):
    >    self.name = name
    >    self.age = age
    >
    >  def say_hello(self):
    >    print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))
    > ```
    >
    > The `__init__()` method is called when a new instance of the `Person` class is created. The `self` parameter is passed to the `__init__()` method, and it is used to initialize the attributes `name` and `age` of the new instance.
    >
    > The `say_hello()` method also takes the `self` parameter. This parameter is used to access the attributes `name` and `age` of the current instance.
    >
    > When the `say_hello()` method is called, the `self` parameter is bound to the current instance of the `Person` class. This means that the `self.name` and `self.age` attributes refer to the attributes of the current instance.
    >
    > The `self` keyword is a very important part of object-oriented programming in Python. It allows you to access the attributes and methods of the current instance, and it is essential for creating and using classes.
    >
    > Here are some additional things to keep in mind about the `self` keyword:
    >
    > -   The `self` keyword is always the first parameter of a method in a class.
    > -   The `self` keyword cannot be used as a variable name outside of a class.
    > -   The `self` keyword is a convention, and it is not a reserved word in Python. You can use another name if you want, but it is not recommended.
    >
    > I hope this helps! Let me know if you have any other questions.
-   can self be omitted in python?
    > No, `self` cannot be omitted in Python. It is a special keyword that is used to refer to the current instance of a class. If you omit `self`, the interpreter will not know which instance of the class you are referring to, and your code will not work.
    >
    > There are some people who argue that `self` is unnecessary and that you can just use the name of the class instead. However, this is not recommended, as it can make your code more difficult to read and understand.
    >
    > The `self` keyword is a very important part of object-oriented programming in Python. It allows you to access the attributes and methods of the current instance, and it is essential for creating and using classes.
    >
    > Here is an example of what happens when you try to omit `self`:
    >
    > ```python
    > class Person:
    >  def __init__(name, age):
    >    self.name = name
    >    self.age = age
    >
    >  def say_hello(name, age):
    >    print("Hello, my name is {} and I am {} years old.".format(name, age))
    > ```
    >
    > This code will not work, as the `say_hello()` method does not have a `self` parameter. The interpreter will not know which instance of the `Person` class to use, and the code will not compile.
    >
    > To fix this, you need to add the `self` parameter to the `say_hello()` method. The modified code would look like this:
    >
    > ```python
    > class Person:
    >  def __init__(self, name, age):
    >    self.name = name
    >    self.age = age
    >
    >  def say_hello(self):
    >    print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))
    > ```
    >
    > This code will work, as the `self` parameter is now used to refer to the current instance of the `Person` class.
    >
    > I hope this helps! Let me know if you have any other questions.

## `tuple` vs. `list`, in python

Tuples and lists are both sequences in Python, but they have some key differences. Tuples are immutable, while lists are mutable. This means that once a tuple is created, its elements cannot be changed, while the elements of a list can be changed.

Another difference between tuples and lists is that tuples are typically faster than lists. This is because tuples are stored in a single memory block, while lists are stored in two memory blocks. The first memory block contains the information about the list, such as its length and its type. The second memory block contains the actual elements of the list.

Here is a table that summarizes the key differences between tuples and lists:

| Feature      | Tuple                                                       | List                                                           |
| ------------ | ----------------------------------------------------------- | -------------------------------------------------------------- |
| Mutability   | Immutable                                                   | Mutable                                                        |
| Speed        | Faster                                                      | Slower                                                         |
| Memory usage | Less memory                                                 | More memory                                                    |
| Use cases    | Constants, keys in dictionaries, return values of functions | Dynamic data structures, storing lists of data that may change |

Here are some examples of when to use tuples and lists:

-   Use tuples to store constants, such as the coordinates of a point on a map.
-   Use tuples as keys in dictionaries, since tuples are immutable, they cannot be changed, which makes them a good choice for keys.
-   Use tuples as return values of functions, since tuples are immutable, they can be safely returned from functions without worrying about the caller changing the values of the tuple.
-   Use lists to store dynamic data structures, such as a list of names or a list of scores.
-   Use lists to store lists of data that may change, since lists are mutable, they can be easily changed.

Ultimately, the best way to decide whether to use a tuple or a list is to consider the specific situation. If you need a data structure that is immutable and fast, then use a tuple. If you need a data structure that is mutable and can store dynamic data, then use a list.

# Thu Jul 27 22:24:00 CST 2023

## data types in python

In Python, data types are used to define the type of data that can be stored in variables. Python is a dynamically typed language, which means that the data type of a variable is determined at runtime based on the value assigned to it. Here are some common data types in Python:

1. Numeric Types:

    - `int`: Integers (whole numbers) like -5, 0, 100.
    - `float`: Floating-point numbers with decimal points like 3.14, -2.5.

2. String Type:

    - `str`: Sequence of characters enclosed in single quotes ('...') or double quotes ("...").

3. Boolean Type:

    - `bool`: Represents True or False.

4. Sequence Types:

    - `list`: Ordered collection of elements, mutable (can be modified).
    - `tuple`: Ordered collection of elements, immutable (cannot be modified).
    - `range`: Represents an immutable sequence of numbers, often used for loops.

5. Set Types:

    - `set`: Unordered collection of unique elements, mutable (can be modified).
    - `frozenset`: Unordered collection of unique elements, immutable (cannot be modified).

6. Mapping Type:

    - `dict`: Collection of key-value pairs, where keys are unique and immutable.

7. None Type:
    - `None`: Represents the absence of a value or a null value in Python.

Python automatically converts data types as needed, allowing you to perform operations on different data types without explicit type conversions.

Example:

```python
# Numeric Types
x = 42           # int
y = 3.14         # float

# String Type
name = 'John'    # str

# Boolean Type
is_student = True  # bool

# List
numbers = [1, 2, 3, 4]  # list

# Tuple
point = (10, 20)  # tuple

# Set
unique_numbers = {1, 2, 3, 4}  # set

# Dictionary
person = {'name': 'Alice', 'age': 30, 'is_student': False}  # dict

# None Type
result = None  # NoneType
```

Remember that Python is not statically typed like some other languages, so variables can change their data type during runtime based on the values assigned to them.

# Sun Jul 30 14:58:52 CST 2023

## `bisect` — Array bisection algorithm

**Read the documentation: [docs](https://docs.python.org/3/library/bisect.html)**

**introduce ` bisect.bisect_left()` of python by gpt-3.5**

> `bisect.bisect_left()` is a function in Python's built-in `bisect` module that provides a way to perform binary search on a sorted sequence. It helps find the insertion point for a target element in the sequence while maintaining the sequence's sorted order.
>
> Here's the general syntax of `bisect.bisect_left()`:
>
> ```python
> import bisect
>
> index = bisect.bisect_left(sorted_sequence, target[, lo[, hi]])
> ```
>
> Parameters:
>
> -   `sorted_sequence`: This is the sorted list or sequence in which you want to find the insertion point for the target element.
> -   `target`: This is the element you want to find the insertion point for.
> -   `lo` (optional): It specifies the lower bound index from which the search begins. By default, `lo` is set to 0.
> -   `hi` (optional): It specifies the upper bound index at which the search ends. By default, `hi` is set to the length of the `sorted_sequence`.
>
> Return value:
>
> -   The function returns the index where the target element should be inserted in order to maintain the sorted order of the sequence.
>
> It's essential to note that `bisect.bisect_left()` returns the leftmost insertion point, meaning if there are duplicate elements equal to the target, it will return the index where the target should be inserted before those duplicates.
>
> Example:
>
> ```python
> import bisect
>
> numbers = [1, 3, 5, 7, 9]
>
> # Find the insertion point for target value 4
> index = bisect.bisect_left(numbers, 4)
> print(index)  # Output: 2 (since 4 should be inserted at index 2 to maintain sorted order)
> ```
>
> In this example, the target value is 4, and the function returns 2 because inserting 4 at index 2 in the `numbers` list will keep the list sorted.
>
> `bisect.bisect_left()` is useful when you have a sorted dataset and need to quickly find the insertion point for new elements to maintain the sorted order efficiently.

# Mon Jul 31 15:46:12 CST 2023

## introduce "binary tree - DFS"

**From GPT-3.5:**  
**Binary Tree - Depth-First Search (DFS)**

A binary tree is a hierarchical data structure that consists of nodes connected by edges. Each node in a binary tree can have at most two children, known as the left child and the right child. The topmost node in the tree is called the root.

Depth-First Search (DFS) is one of the fundamental tree traversal algorithms used to visit and explore all the nodes in a binary tree. DFS explores as far as possible along each branch before backtracking. It prioritizes exploring the depth of a tree before exploring its breadth.

There are three common variants of DFS for binary trees:

1. **In-Order DFS:** In this variant, we first visit the left subtree recursively, then the current node, and finally the right subtree recursively. For a binary search tree, the in-order DFS visits the nodes in ascending order, hence its name "in-order."

2. **Pre-Order DFS:** In this variant, we first visit the current node, then the left subtree recursively, and finally the right subtree recursively.

3. **Post-Order DFS:** In this variant, we first visit the left subtree recursively, then the right subtree recursively, and finally the current node.

Each variant of DFS has its own specific use cases. For instance, in-order DFS is useful when you want to visit the nodes in a sorted order, pre-order DFS can be used to create a copy of the tree, and post-order DFS is often used to delete the tree.

DFS can be implemented using both recursion and iteration (using a stack). Recursive DFS is straightforward to implement and can be intuitive for smaller trees. However, for larger trees, it may lead to stack overflow due to excessive recursion. Iterative DFS using a stack can be more efficient and is recommended for larger trees.

Overall, DFS is a powerful algorithm to traverse binary trees and can be applied in various scenarios, such as searching for a specific node, checking for the existence of a node, performing tree-based calculations, and more.

# Tue Aug 1 20:56:09 CST 2023

## Introduce `nonlocal` key word in python

[1]: https://stackoverflow.com/questions/1261875/what-does-nonlocal-do-in-python-3 "What does \"nonlocal\" do in Python 3? - Stack Overflow"
[2]: https://www.w3schools.com/python/ref_keyword_nonlocal.asp "Python nonlocal Keyword - W3Schools"
[3]: https://pythontic.com/concepts/keywords/nonlocal "The nonlocal keyword in Python | Pythontic.com"
[4]: https://www.includehelp.com/python/nonlocal-keyword-with-example.aspx "nonlocal keyword with example in Python - Includehelp.com"
[5]: https://www.delftstack.com/howto/python/nonlocal-python/ "The nonlocal Keyword in Python | Delft Stack"

The `nonlocal` keyword in Python is used to modify a variable that is defined in an outer function scope, but not in the global scope. It allows a nested function to access and change a variable that belongs to its enclosing function.

For example, consider this function that defines a nested function and a variable x:

```python
def outer ():
  x = 0 # x is defined in the outer function scope
  def inner ():
    x = 1 # x is defined in the inner function scope
    print (x) # prints 1
  inner ()
  print (x) # prints 0
```

In this case, the inner function creates a new local variable x that shadows the outer variable x. Therefore, changing the inner x does not affect the outer x.

However, if we use the `nonlocal` keyword inside the inner function, we can tell Python that we want to refer to the outer x, not the local one:

```python
def outer ():
  x = 0 # x is defined in the outer function scope
  def inner ():
    nonlocal x # x is declared as nonlocal
    x = 1 # x is modified in the outer function scope
    print (x) # prints 1
  inner ()
  print (x) # prints 1
```

In this case, the inner function modifies the outer variable x, and both functions print the same value.

The `nonlocal` keyword can only be used inside a nested function. It cannot be used in the global scope or in a class. It can also be used with multiple variables, separated by commas.

The `nonlocal` keyword is useful when we want to create closures or decorators that can modify the state of an outer function. It can also help us avoid using global variables that can cause unwanted side effects.

For more information on `nonlocal` and its usage, you can refer to these sources:

[^1^][1]: [What does "nonlocal" do in Python 3? - Stack Overflow](https://stackoverflow.com/questions/1261875/what-does-nonlocal-do-in-python-3)
[^2^][2]: [Python nonlocal Keyword - W3Schools](https://www.w3schools.com/python/ref_keyword_nonlocal.asp)
[^3^][3]: [The nonlocal keyword in Python | Pythontic.com](https://pythontic.com/concepts/keywords/nonlocal)
[^4^][4]: [nonlocal keyword with example in Python - Includehelp.com](https://www.includehelp.com/python/nonlocal-keyword-with-example.aspx)
[^5^][5]: [The nonlocal Keyword in Python | Delft Stack](https://www.delftstack.com/howto/python/nonlocal-python/)

## Introduce `defaultdict()` in Python

[1]: https://www.geeksforgeeks.org/defaultdict-in-python/ "Defaultdict in Python - GeeksforGeeks"
[2]: https://realpython.com/python-defaultdict/ "Using the Python defaultdict Type for Handling Missing Keys"
[3]: https://www.interviewkickstart.com/learn/defaultdict-in-python "What is Defaultdict in Python | Interviewkickstart"
[4]: https://datagy.io/python-defaultdict/ "Python Defaultdict: Overview and Examples • datagy"
[5]: https://geekflare.com/defaultdict-in-python/ "How and When Should You Use Defaultdict in Python?"

The `defaultdict()` function in Python is a factory function that returns a subclass of the built-in `dict` class. The `defaultdict` class behaves like a regular dictionary, but it can handle missing keys more gracefully. It does so by providing a default value for any key that is not present in the dictionary.

The `defaultdict()` function takes a single argument, which is a callable object (such as a function, a class, or a lambda expression) that returns the default value for the missing keys. This argument is called the `default_factory`. For example, you can create a `defaultdict` object with an integer as the default value:

```python
from collections import defaultdict
d = defaultdict(int) # int is the default_factory
```

Now, if you try to access or modify a key that does not exist in `d`, the `defaultdict` object will automatically create that key and assign it the default value returned by the `default_factory`. In this case, the default value is 0:

```python
print(d["a"]) # prints 0
d["b"] += 1 # creates key "b" and assigns it 1
print(d["b"]) # prints 1
```

You can also use other types or functions as the `default_factory`. For example, you can use `list` to create a `defaultdict` object with an empty list as the default value:

```python
from collections import defaultdict
d = defaultdict(list) # list is the default_factory
```

Now, if you try to access or modify a key that does not exist in `d`, the `defaultdict` object will automatically create that key and assign it an empty list:

```python
print(d["a"]) # prints []
d["b"].append(1) # creates key "b" and appends 1 to its list
print(d["b"]) # prints [1]
```

The `defaultdict()` function is useful when you want to avoid raising a `KeyError` when working with dictionaries. It can also help you simplify your code and avoid using methods like `.setdefault()` or `.get()` to handle missing keys. It can also be used for various tasks such as grouping, counting, or accumulating values.
d

## variable's scope of `while`, `if`, and `for` in python is different from other languages

[1]: https://stackoverflow.com/questions/36858963/python-access-variable-in-while-loop "Python access variable in while loop - Stack Overflow"
[2]: https://stackoverflow.com/questions/3611760/scoping-in-python-for-loops "scope - Scoping in Python 'for' loops - Stack Overflow"
[3]: https://www.geeksforgeeks.org/python-while-loop/ "Python While Loop - GeeksforGeeks"
[4]: https://open.oregonstate.education/computationalbiology/chapter/variables-and-scope/ "Variables and Scope – A Primer for Computational Biology"
[5]: https://www.educative.io/courses/python-ftw-under-the-hood/N8RW8508RkL "Loop Variables Leaking Out! - Python FTW: Under the Hood - Educative"

The `node` variable can be accessed outside of the inner while loop because Python does not create a new scope for variables declared in if-statements, for-loop blocks, and while-loop blocks[^1^][4]. The variables defined in these blocks are not local variables, and they stay in scope outside of the block[^2^][3] [^3^][5]. This is different from some other languages, where variables declared in a loop are local to the loop and are destroyed when the loop exits[^4^][2]. In Python, you can use the `global` keyword to specify that a variable is assigned at the global scope[^5^][1], but there is no keyword to make a variable local to a loop.

# Thu Aug 3 14:05:06 CST 2023

## `heapq.heappop()` in Python

[1]: https://docs.python.org/3/library/heapq.html "heapq — Heap queue algorithm — Python 3.11.4 documentation"
[2]: https://realpython.com/python-heapq-module/ "The Python heapq Module: Using Heaps and Priority Queues"
[3]: https://medium.com/plain-simple-software/python-heapq-use-cases-and-time-complexity-ee7cbb60420f "Python HeapQ Use Cases and Time Complexity - Medium"
[4]: https://towardsdatascience.com/introduction-to-python-heapq-module-53534feda625 "Introduction to Python Heapq Module - Towards Data Science"

The `heapq.heappop()` function in Python is used to pop and return the smallest item from a heap, maintaining the heap invariant[^1^][1]. A heap is a data structure that represents a priority queue, where the item with the highest priority (or the lowest value) is always at the root[^2^][2]. The heapq module implements heaps using lists, where the first element of the list is the root, and the rest of the elements follow the heap property[^3^][3].

The `heapq.heappop()` function takes a list as an argument and returns the first element of the list, which is the smallest item in the heap. It also modifies the list in-place, so that it remains a valid heap after removing the smallest item. The time complexity of this operation is O(log n), where n is the size of the heap[^4^][4]. For example:

```py
import heapq

# create a min heap from a list of numbers
nums = [5, 7, 9, 1, 3]
heapq.heapify(nums)

# pop and return the smallest item from the heap
print(heapq.heappop(nums)) # 1

# the list is modified in-place
print(nums) # [3, 5, 9, 7]
```

## explain `pairs.sort(key = lambda x: -x[1])`

This is a Python code that sorts a list of pairs (tuples of two elements) in descending order by their second element. Here is how it works:

-   `pairs` is the name of the list of pairs, such as `[(1, 2), (3, 4), (5, 6)]`.
-   `sort` is a method of the list class that sorts the list in place, meaning it modifies the original list without returning a new one.
-   `key` is a parameter of the sort method that specifies a function to be applied to each element of the list before comparing them for sorting. The function should return a value that can be compared, such as a number or a string.
-   `lambda x: -x[1]` is an anonymous function (also called a lambda expression) that takes one argument `x` and returns the negative value of its second element. For example, if `x` is `(1, 2)`, then `-x[1]` is `-2`.
-   By using this function as the key, the sort method will sort the pairs by their second element in reverse order, because the negative value reverses the comparison. For example, if the list is `[(1, 2), (3, 4), (5, 6)]`, then after sorting it will be `[(5, 6), (3, 4), (1, 2)]`, because `-6 < -4 < -2`.

## In JavaScript, object keys are always converted to strings

In JavaScript, object keys are always converted to strings, regardless of whether they are specified as strings or integers. This is because JavaScript objects are implemented as hash tables, and hash tables in JavaScript can only have string keys.

When you use a non-string value as a key in an object literal or when adding properties dynamically to an object, JavaScript automatically converts the key to its string representation. For example:

```js
const obj = {};

obj[42] = "forty-two";
console.log(obj); // { "42": "forty-two" }
```

In this example, `42` is used as a key, but when the object is printed, it shows the key as `"42"` (a string representation of the number 42).

Similarly, when you use dot notation or square bracket notation to access a property in an object, JavaScript internally converts the property name to a string before performing the access:

```js
const obj = {
    42: "forty-two",
};

console.log(obj[42]); // "forty-two"
console.log(obj["42"]); // "forty-two"
```

As you can see, both `obj[42]` and `obj["42"]` yield the same result because JavaScript internally converts the key to a string before looking up the property.

Keep in mind that this automatic conversion of keys to strings can lead to unexpected behavior if you have keys that are not intended to be strings. If you need to work with keys of different types, you may want to handle the conversion explicitly using `String(key)` to ensure consistent behavior.
