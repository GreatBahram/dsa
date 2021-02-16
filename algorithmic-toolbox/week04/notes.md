Dividing and Conquer

The idea of divide and conquer is to split the main problem into some subproblems and solve them instead of a large problem. Break the problem into non-overlapping subproblems of the same type, and at the end combine different parts.

## Introduction

## Problems

### Polynomial Multiplication

#### Naive algorithm

<img src="assets/polynomial-multiplication-01.png" style="zoom:15%">

#### Naive divide and conquer algorithm

What if you divide a multiplication into four parallel parts:

<img src="assets/polynomial-multiplication-02.png" style="zoom:15%">

Example:

<img src="assets/polynomial-multiplication-03.png" style="zoom:15%">

Implementation:

<img src="assets/polynomial-multiplication-04.png" style="zoom:15%">

Time complexity of this algorithm is the same as the naive algorithm $$O(n^2)$$.

<img src="assets/polynomial-multiplication-05.png" style="zoom:25%">

#### Efficient divide and conquer algorithm

`Karatsuba` realized in a normal multiplication we have 4 multiplication:

<img src="assets/karatsuba-approach-01.png" style="zoom:20%">

He rewrited the formula to have fewer multiple operations:

<img src="assets/karatsuba-approach-02.png" style="zoom:20%">

For example: as it can be observed we have only 3 multiplication, instead of 4. This can reduce the time complexity of the algorithm significantly.

<img src="assets/karatsuba-approach-03.png" style="zoom:20%">

Time Complexity:

<img src="assets/karatsuba-approach-04.png" style="zoom:20%">

## Master Theorem

Master theorem helps us to identify the time complexity of a divide-and-conquer algorithm more easily, instead of creating the recurrence tree we can simply recognize it.

<img src="assets/master-theorem.png" style="zoom:20%">

## Sorting Problem

We want to sort data as it is an essential step of efficient algorithms and it also allows more efficient queries (like binary search).

### Selection Sort

Selection sorting algorithm is pretty straightforward, at $$i^{th}$$ step, it will find the $$i^{th}$$ minimum element and put it in the right place.



<img src="assets/sorting-problem/selection-sort-01.png" style="zoom:30%">

This is an example code about how to implement it:

<img src="assets/sorting-problem/selection-sort-02.png" style="zoom:30%">

The running time of selection sort is $$O(n^2)$$, as it has two for loop and it works like an arithmetic series, and the running time of this algorithm does not depend on the input data. It only depends on the size of the input data.

<img src="assets/sorting-problem/selection-sort-03.png" style="zoom:30%">

<img src="assets/sorting-problem/selection-sort-04.png" style="zoom:20%">

### Merge Sort

https://brilliant.org/wiki/merge/

<img src="assets/sorting-problem/merge-sort-01.png" style="zoom:20%">



Merge sort has two steps: merging and sorting. Merge sort focuses on how to merge two pre-sorted arrays such that the resulting array is also sorted.

<img src="assets/sorting-problem/merge-sort-02.png" style="zoom:20%">

The merge part works like this:

> 1. Create an empty list called the result list.   
> 2. Do the following until one of the input lists is empty: Remove the  first element of the list that has a lesser first element and append it  to the result list.   
> 3. When one of the lists is empty, append all elements of the other list to the result.

<img src="assets/sorting-problem/merge-sort-03.png" style="zoom:20%">

<img src="assets/sorting-problem/merge-sort-04.png" style="zoom:20%">

Merge sort runs in $$O(n\lg n)$$ time in its best case, worst case, and average case. That means that no matter what the input, merge sort will operate in $$O(n \lg n)$$ time. But it is not as space-efficient as other sorting algorithms, it uses a [space complexity](https://brilliant.org/wiki/space-complexity/) of $$O(n)$$.



<img src="assets/sorting-problem/merge-sort-05.png" style="zoom:20%">

#### Lower Bound

<img src="assets/sorting-problem/lower-bound01.png" style="zoom:30%">

<img src="assets/sorting-problem/lower-bound02.png" style="zoom:20%">

Here we are trying to prove that there is a Lower bound for comparison based algorithm and merge sort reaches that lower band, so it is efficient.

Any comparison algorithm can be expressed as a decision tree, in which leaves are the final sorted items. The number of leaves ($$l$$) in the tree must be at least $$n!$$ (the total number of permutations).

<img src="assets/sorting-problem/lower-bound03.png" style="zoom:30%">

 And we know the maximum number of leaves in the tree with depth $$d$$ is $$2^{d}$$. And $$2^d \ge l$$  or $$d \ge \lg_2 l$$.

<img src="assets/sorting-problem/lower-bound04.png" style="zoom:40%">

<img src="assets/sorting-problem/lower-bound05.png" style="zoom:30%">



### Counting Sort

Counting sort algorithm is a non-comparison algorithm and we want to show that in this case our lower bound might not apply.

* While any comparison based sorting algorithm requires $$\Omega(n \lg n)$$ comparisons, counting sort has a running time of $$\Theta(n)$$ when the length of the input list is not much smaller than the largest key value, $$k$$, in the list.

  <img src="assets/sorting-problem/counting-sort-01.png" style="zoom:50%">



<img src="assets/sorting-problem/counting-sort-02.png" style="zoom:20%">

<img src="assets/sorting-problem/counting-sort-03.png" style="zoom:20%">

<img src="assets/sorting-problem/counting-sort-04.png" style="zoom:25%">

https://brilliant.org/wiki/counting-sort/

https://codereview.stackexchange.com/questions/105490/counting-sort-in-python

Summary

<img src="assets/sorting-problem/merge-sort-07.png" style="zoom:20%">