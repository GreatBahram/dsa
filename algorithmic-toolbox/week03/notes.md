# Greedy Algorithms

Greedy algorithms are *greedy*. They don't look into the future to choose the *global optimal solution*. They are only interested in **optimal solution locally**.

Some of these algorithms are:

* Largest number
* Minimum refill problem.

## Main ingredients

At each iteration, we are solving one step of the problem, this approach is called *subproblem*.

Another important term is the **safe move**. We call a **greedy** choice a **safe move** if it is consistent with some optimal solution.

General Strategy:

1. Make a greedy choice
2. Prove that it is a safe move
3. Reduce the problem to a subproblem.
4. Solve the subproblem.

## Useful links

[Greedy Algorithms In Python](https://skerritt.blog/greedy-algorithms/)