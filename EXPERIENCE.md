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
