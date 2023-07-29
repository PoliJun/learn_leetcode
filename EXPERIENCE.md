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
