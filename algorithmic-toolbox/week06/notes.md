# Dynamic Programming II

## Problems

### Knapsack

As you might remember we solved knapsack problem using Greedy approach in the past, it was an optimal solution when you could choose fractionally from items. But when we are dealing with zero/one Knapsack, it cannot find the optimal solution.

[Bottom up solution](https://www.youtube.com/watch?v=8LusJS5-AGo), [top-down solution](https://www.youtube.com/watch?v=xOlhR_2QCXY).

#### Knapsack With Repetitions

#### Knapsack without Repetitions

The i-th value is either used or not, and we calculate both cases at each step.
$$
max\{value(W - w_i, i - 1), value(W, i - 1)\}
$$

### Placing Parentheses