# Dividing and Conquer

The idea of divide and conquer is to split the main problem into some **separate** subproblems and solve them instead of a large problem. Another way to way to say it, break the problem into

1.  **non-overlapping subproblems** of the same type
2.  and at the end **combine different parts**.

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

For example: as it can be observed we have only **3 multiplication, instead of 4**. This can reduce the time complexity of the algorithm significantly.

<img src="assets/karatsuba-approach-03.png" style="zoom:20%">

Time Complexity:

<img src="assets/karatsuba-approach-04.png" style="zoom:20%">

## Master Theorem

Master theorem helps us to identify the time complexity of a divide-and-conquer algorithms more easily, instead of creating the recurrence tree we  can simply recognize it.

<img src="assets/master-theorem.png" style="zoom:20%">

## Sorting Problem

We want to sort data as it is an essential step of efficient algorithms and it also allows more efficient queries (like binary search). There are two different sorting algorithms:

1. comparison-based algorithm: Comparison sorts cannot be faster than $$O(n \log n)$$. A lower bound for an algorithm is the *worst-case* running time of the *best* possible algorithm for a given problem.
2. Non-comparison (integer) sorting: Integer sorts do not make comparisons, so they are not bounded by $$\Omega(n\log n)$$.

### Selection Sort

Selection sorting algorithm is pretty straightforward, at $$i^{th}$$ step, it will find the $$i^{th}$$ minimum element and put it in its final position.



<img src="assets/sorting-problem/selection-sort-01.png" style="zoom:30%">

This is an example code about how to implement it:

<img src="assets/sorting-problem/selection-sort-02.png" style="zoom:30%">

The running time of selection sort is $$O(n^2)$$, as it has two for loop and it works like an arithmetic series, and the running time of this algorithm does not depend on the input data. It only depends on the size of the input data.

* Running time of this algorithm does not depend on the input data, it does not change if the data is already sorted.
* As $$i$$ grows, the number of iterations of the inner loop decreases, j iterates from $$i+1$$ to $$n$$.
* A more accurate estimate for the total number of iterations of the inner loop is: $$(n - 1) + (n - 2) + \dots + 1$$ 

<img src="assets/sorting-problem/selection-sort-03.png" style="zoom:30%">

<img src="assets/sorting-problem/selection-sort-04.png" style="zoom:20%">

### Merge Sort

https://brilliant.org/wiki/merge/

<img src="assets/sorting-problem/merge-sort-01.png" style="zoom:20%">



Merge sort has two steps: merging and sorting. Merge sort focuses on how to merge two xpre-sorted arrays such that the resulting array is also sorted.

<img src="assets/sorting-problem/merge-sort-02.png" style="zoom:20%">

The merge part works like this:

> 1. Create an empty list called the result list.   
> 2. Do the following until one of the input lists is empty: Remove the  first element of the list that has a lesser first element and append it  to the result list.   
> 3. When one of the lists is empty, append all elements of the other list to the result.

<img src="assets/sorting-problem/merge-sort-03.png" style="zoom:20%">

<img src="assets/sorting-problem/merge-sort-04.png" style="zoom:20%">

* Merge sort runs in $$O(n\lg n)$$ time in its best case, worst case, and average case. 

This means that no matter what the input is, merge sort will operate in $$O(n \lg n)$$ time. But **it's not as space-efficient as other sorting algorithms**, it uses  a [space complexity](https://brilliant.org/wiki/space-complexity/) of $$O(n)$$.



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

Counting sort algorithm is a **non-comparison algorithm** and we want to show that in this case our lower bound might not apply.

* **While any comparison based sorting algorithm requires $$\Omega(n \lg n)$$ comparisons**, counting sort has a running time of $$\Theta(n)$$ when the length of the input list is not much smaller than the largest key value, $$k$$, in the list.

  <img src="assets/sorting-problem/counting-sort-01.png" style="zoom:50%">



<img src="assets/sorting-problem/counting-sort-02.png" style="zoom:20%">

<img src="assets/sorting-problem/counting-sort-03.png" style="zoom:20%">

<img src="assets/sorting-problem/counting-sort-04.png" style="zoom:25%">

https://brilliant.org/wiki/counting-sort/

https://codereview.stackexchange.com/questions/105490/counting-sort-in-python

<img src="assets/sorting-problem/merge-sort-07.png" style="zoom:20%">

### Quick Sort

* Comparison based
* running time: $$O(n \lg n)$$, (on average)
* efficient in practice

It will pick a pivot and it will arrange items in way that at the end of each iteration pivot will be placed in its final position, and all the elements before it are lower or equal to the pivot and all of items on the right are bigger. 

<img src="assets/sorting-problem/quick-sort-01.png" style="zoom:40%" alt="How quick sort works">

What's remain to be done, is the left and right side of the pivot item. We could do by two recursive calls.

<img src="assets/sorting-problem/quick-sort-02.png" style="zoom:20%" alt="How quick sort works">

<img src="assets/sorting-problem/quick-sort-03.png" style="zoom:15%" alt="How quick sort works">

But, how does the  partition function work?

<img src="assets/sorting-problem/quick-sort-04.png" style="zoom:15%" alt="How quick sort works">

**Worst case scenario**

If we in each iteration choose the minimum element then we compare this element with all other element, image we're doing this for all iteration (this case is called **unbalanced partition**):
$$
T(n) = n + T(n-1): \\
T(n) = n + n -1 + n-2 + \dots = \Theta(n^2)
$$
**Unbalanced partition**, with any degree, always leads to $$\Theta(n^2)$$ running time. But if we could somehow find a partition that split the array into two halves (**balanced partition**):
$$
T(n) = 2T(\frac{n}{2}) + n \\
T(n) = \Theta(n \lg n)
$$
Balanced partitions are better, as they reduce the number of comparisons.

So, finding a good pivot is the most important aspect of quick sort (even if this pivot does not split it equivalently it is still $$\Theta(n \lg n)$$). From the mathematical point of view, this element should the the **median** of the array. But what if we choose the pivot randomly:

<img src="assets/sorting-problem/quick-sort-05.png" style="zoom:.2" alt="Random pivot">

* Why random pivot?

Imagine we have an array of items called A, and each element is unique inside the list, if we sort this array, then we expect the $$\frac{n}{2}$$ of item be placed in the center of the sorted array, the remaining $$2\frac{n}{4}$$ be smaller and greater, respectively of the centered items. **So half of the elements of A guarantees a balanced partition.**

##### Equal elements

If we have some repetition inside our list, then when we pick a pivot all other repeated one will be sorted as well, and we should take this into consideration to don't use any of repeated ones again. As result, quick sort is not as fast as merge sort on a dataset with <u>a few unique elements</u>. On this case the running time is $$\Theta(n^2)$$. This is true even for pre-sorted arrays.

To handle equal elements we could change our partition algorithm to split the data after choosing a pivot into three region.

<img src="assets/sorting-problem/quick-sort-06.png" style="zoom:60%" alt="How quick sort works">

<img src="assets/sorting-problem/quick-sort-07.png" style="zoom:70%" alt="How quick sort works">

With this simple modification, `Partition3`, quick sorting algorithm is now faster than merge sort on dataset with few unique elements.

<img src="assets/sorting-problem/quick-sort-08.png" style="zoom:70%">

* Up to now, we only implemented this algorithm **recursively** and it might use too much of <u>stack resources</u>, **it uses $$O(n)$$ additional memory**. One way to remedy this is to reduce the recursive calls to one and in this case uses **no more than $$O(\log n)$$ additional memory**. In the below implementation we decreased one recursive call.

<img src="assets/sorting-problem/quick-sort-09.png" style="zoom:60%">

In the above implementation we don't care about which side is shorter, while we could know this and this  the option will be used to decide which side first should be sort:

<img src="assets/sorting-problem/quick-sort-10.png" style="zoom:60%">

* And finally, as we don't have control over to the pivot selection in this approach, as it is randomized, we can go for another approach which is more deterministic. For instance, we can use the **median-of-medians** algorithm to always choose the median of dataset. Or a simple approach as choosing the leftmost or the rightmost element.

https://stackabuse.com/quicksort-in-python/

https://brilliant.org/wiki/quick-sort/  