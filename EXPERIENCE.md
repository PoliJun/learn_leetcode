**YOU MUST READ THE CODE OF ANSWER LINE BY LINE**

# Wed Jul 26 10:43:51 CST 2023

## Steps to solve a problem

1. Guess:
    > For example:
    > _Container With Most Water_ problem, need to traverse the array, then you should consider _two pointers_.
2. Analysis the instructions:
    > Choose an already known mature algorithms as a paradim. Then optimize this problem.
3. Analyze the algorithm's _time complexity_ and _space complexity_

## Two aspects to analysis the problem:

1. paradim
2. instructions

## Sliding Window

This algorithm's point is to find out the condition where to do the left += 1.

## stack

-   When to consider this algorithm?
    > when traverse an array with single direction, and pop the last element when meet some conditions.

# Sat Jul 29 16:50:52 CST 2023

## deque() in python:

`933. Number of Recent Calls` and `643. Maximum Average Subarray I` both uses sliding window.
but `933` uses deque(which is a biderectional queue), `643` uses flow control.
This is because queue is a data structure, it is used to store the data, then manipulate the data.
We also can use deque in `643`, but we need to cal the sum Ο(n) every move forward and extra space to store the numbers. But we don't need a copy of the data in `643`.

Data structure and Algorithms are bounded together all the time. We need design the order of instructions, which is the algorithms, and we design the data structure, in which we can easily choose a paradim of algorithms to design an optimal solution.

# Sun Jul 30 15:08:42 CST 2023

## When consider `queue`?

> Queue is an efficient data structure that can help us find the next closest opponent senator as well as the next eligible voter. It also helps us in simulating the voting process from left to right. Also, it is easier to keep track of rounds of voting by assuming the index increase by NNN after each round.

## 2095. Delete the Middle Node of a Linked List

### **Why we initialize `fast = head.next.next` at the begining?**

The reason for this is that we want to deleted the middle node instead of finding it. Therefore, we are actually looking for the predecessor of the middle node, not the middle node itself, or rather, this is like moving slow backward one node after the iteration stops.

Certainly, we can't move a pointer backward on a singly linked list, thus we can show this one less step on slow by letting fast moves forward one more step (by two nodes, of course). Hence, slow will also point to the predecessor node of the middle node (rather than the middle node) at the end of the iteration.

### 328. Odd Even Linked List

**intuition**  
Put the odd nodes in a linked list and the even nodes in another. Then link the evenList to the tail of the oddList.

# Wed Aug 2 14:50:31 CST 2023

## Which approach to choose, BFS or DFS ?

    The problem is to return a list of last elements from all levels,
    so it's the way more natural to implement BFS here.

    Time complexity is the same O(N)\mathcal{O}(N)O(N)
    both for DFS and BFS since one has to visit all nodes.

    Space complexity is O(H)\mathcal{O}(H)O(H) for DFS and
    O(D)\mathcal{O}(D)O(D) for BFS, where HHH is a tree height,
    and DDD is a tree diameter. They both result in
    O(N)\mathcal{O}(N)O(N) space in the worst-case scenarios:
    skewed tree for DFS and complete tree for BFS.

# Sun Aug 6 16:59:51 CST 2023

## DFS or BFS?

Deciding whether to use Depth-First Search (DFS) or Breadth-First Search (BFS) depends on the specific requirements and characteristics of the graph and the problem you are trying to solve. Both DFS and BFS are essential graph traversal algorithms, but they have distinct strengths and use cases:

1. Depth-First Search (DFS):

    - DFS explores as far as possible along each branch before backtracking.
    - It uses a stack (either explicit or recursive) to keep track of nodes to visit.
    - DFS is generally more memory-efficient than BFS because it only needs to store information about the current path.
    - It is often used in problems that require exploring all possible paths or to find a single path from a start node to a target node.
    - DFS is also well-suited for problems like cycle detection, topological sorting, and connected component analysis.

2. Breadth-First Search (BFS):
    - BFS explores all nodes at the current depth level before moving to the next depth level.
    - It uses a queue to keep track of nodes to visit in a level-by-level manner.
    - BFS is typically used to find the shortest path in unweighted graphs since it guarantees the shortest path to any reachable node.
    - It can be useful in problems where you want to explore the neighbors of a node before going deeper into the graph or when you need to find the shortest path.

Here are some considerations to help you choose between DFS and BFS:

-   **Shortest path**: If you need to find the shortest path between two nodes in an unweighted graph, BFS is the better choice due to its level-order traversal.

-   **Memory efficiency**: If you are dealing with a very large graph and memory is a concern, DFS might be preferred because it uses less memory compared to BFS.

-   **Completeness**: If you need to explore all possible paths in the graph or find all connected components, DFS is more appropriate as it ensures that all nodes are visited.

-   **Topological sorting**: If you have a directed acyclic graph (DAG) and need to find a linear ordering of its nodes, then DFS is commonly used for topological sorting.

-   **Cycle detection**: If you want to check whether a graph contains cycles, DFS is often the go-to algorithm.

Ultimately, your choice between DFS and BFS should be guided by the specific problem requirements and the properties of the graph you are dealing with. In some cases, you may even combine both algorithms to achieve the desired results.

# Wed Aug 9 17:50:37 CST 2023

**YOU MUST READ THE CODE OF ANSWER LINE BY LINE**

# Sat Aug 12 12:48:24 CST 2023

## Bottom-Up Solution

Bottom-up dynamic programming is also known as tabulation and is done iteratively. Dynamic programming is based on the concept of overlapping subproblems and optimal substructure. This is when the solution to a problem can be constructed from solutions to similar and smaller subproblems. Solving a smaller version of the problem can be easier and faster, thus if we break up the problem into smaller subproblems, solving them can lead us to the final solution easier and faster.

## Top-Down

Bottom-up dynamic programming is named as such because we start from the bottom (in this case, the bottom of the staircase) and iteratively work our way to the top. Top-down dynamic programming starts at the top and works its way down to the base cases. Typically, this is implemented through recursion, and then made efficient using memoization. Memoization refers to storing the results of expensive function calls in order to avoid duplicate computations - we'll soon see why this is important for this problem. If you're new to recursion, check out the recursion explore card.
![top_down](/img/top_down.png)

## house robber

Leet Code: [house_robber](https://leetcode.com/problems/house-robber/)

As we mentioned above, the easiest approach here is to try all possible combinations of house choices and then use the combination that gives the maximum amount of money to the robber. We do this because there is no plausible greedy strategy that we can use to decide if the robber should rob a particular house or not.

We rely on our good friend recursion whenever we have choices involved in solving a problem. Technically, a robber can come back and rob a house that they previously rejected. However, since we are trying all options, we will not go back and rob an unrobbed house since that scenario will be covered in a different recursive path.

# Sun Aug 13 15:00:47 CST 2023

## recurrsion runtime error

![](img/Screen%20Shot%202023-08-13%20at%2014.59.55.png)

You can't do `buy = recurrsion() + i`

## plus 1 to count

[leetcode Edit Distance](https://leetcode.com/problems/edit-distance/)

```py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        @cache
        def recur(word1, word2, index1, index2):

            if index1 == 0:
                return index2
            if index2 == 0:
                return index1
            if word1[index1-1] == word2[index2-1]:
                return recur(word1, word2, index1-1, index2-1)
            else:
                insert = recur(word1, word2, index1, index2-1)
                delete = recur(word1, word2, index1-1, index2)
                replace = recur(word1, word2, index1-1, index2-1)
                return min(insert, delete, replace) + 1

        return recur(word1, word2, n1, n2)
```

**Bing Answer:**  
[1]: https://en.wikipedia.org/wiki/Edit_distance ""
[2]: https://www.geeksforgeeks.org/edit-distance-dp-5/ ""
[3]: https://en.wikipedia.org/wiki/Levenshtein_distance ""
[4]: https://bdebo.medium.com/edit-distance-643a4bcfaa09 ""

Hi, this is Bing. I'm glad you're interested in the edit distance problem. 😊

The edit distance problem is a way of measuring how similar two strings are by counting the minimum number of operations needed to transform one string into another. The operations can be insertion, deletion, or substitution of a single character. [^1^][1]

The reason why we add 1 in the recursive function is to account for the cost of performing one of these operations. For example, if we want to transform "cat" into "cut", we need to substitute "a" with "u", which has a cost of 1. So, the edit distance is the minimum cost of transforming the rest of the string ("c" and "t") plus 1.

Similarly, if we want to transform "cat" into "cats", we need to insert "s" at the end, which also has a cost of 1. So, the edit distance is the minimum cost of transforming the rest of the string ("cat") plus 1.

The base cases of the recursive function are when one of the strings is empty. In that case, the edit distance is equal to the length of the other string, because we need to either insert or delete all the characters in that string.

I hope this explanation helps you understand the logic behind the recursive solution. If you want to learn more about the edit distance problem and its applications, you can check out these links: [Wikipedia article](https://en.wikipedia.org/wiki/Edit_distance), [GeeksforGeeks tutorial](https://www.geeksforgeeks.org/edit-distance-dp-5/), [Medium article](https://bdebo.medium.com/edit-distance-643a4bcfaa09). Have a nice day! 😊

## `&` operator to check 0 or 1

    To obtain the least significant bit of P, we can use bitwise AND operator P & 1

# Wed Aug 16 09:37:33 CST 2023

## Trie

### How to implement

1. Two class: TrieNode and Trie.

2. TrieNode has two attributes: a children:Dict{char: TrieNode,,,} and a is_end: bool

    > Use the dictionary to hashmap the children Node.

    > ```py
    > class Trie:
    >     def __init__(self):
    >         self.root = TrieNode()
    > ```

3. methods:
    - search(word: String)
    - insert(word: String)
    - startWith(prefix: String)
      curr = self.root
      loop: `for c in word` to check if it is a key in curr.children[c]

# Fri Aug 18 23:22:48 CST 2023

# Intervals -> Greedy

**Algorithms:**
Greedy problems usually look like
"Find minimum number of something to do something" or
"Find maximum number of something to fit in some conditions",
and typically propose an unsorted input.

    The idea of greedy algorithm is to pick the locally
    optimal move at each step, that will lead to the globally optimal solution.

The standard solution has O(Nlog⁡N)\mathcal{O}(N \log N)O(NlogN) time complexity and consists of two parts:

    Figure out how to sort the input data (O(Nlog⁡N)\mathcal{O}(N \log N)O(NlogN) time).
    That could be done directly by a sorting or indirectly by a heap usage.
    Typically sort is better than the heap usage because of gain in space.

    Parse the sorted input to have a solution (O(N)\mathcal{O}(N)O(N) time).

Please notice that in case of well-sorted input one doesn't need the first
part and the greedy solution could have O(N)\mathcal{O}(N)O(N) time complexity,

# Monotonic Stack

**A monotonic stack is simply a stack where the elements are always in sorted order.**
