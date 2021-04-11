# Priority Queue

A priority queue is a generalization of a queue where each element is assigned a priority and elements come out in order by priority.

Algorithms that use priority queue:

* Dijsktra's algorithm: finding a shortest path in graph
* Prim's algorithm: constructing a minimum spanning tree of a graph
* Huffman's algorithm: constructing an optimum prefix-free encoding of a string
* Heap sort: sorting a given sequence

Python libraries for priority queue:

[heapq](https://docs.python.org/3/library/heapq.html)

[Priority Queue](https://docs.python.org/3/library/queue.html#queue.PriorityQueue)

Analyzing the naive ideas:

1. Unsorted Array: in this implementation, it requires $$O(1)$$ to insert the item, but for retrieving the max element it takes $$O(n)$$.

2. Sorted Array:

   1. insertion: finding the right position using binary search $$O(\lg n)$$ and insertion (shift) itself takes $$O(n)$$.
   2. extraction the max element: $$O(1)$$

3. Sorted List (linked list):

   1. extraction: $$O(1)$$
   2. insertion: we cannot use binary search here! $$O(n)$$

   <img src="assets/priority-queue-01.png" style="zoom:30%"/>

## Priority Queue using heaps

Binary max heap: is a binary tree (binary means at most has two children) where the value of each node is at least the values of its children, i.e. it is $$>=$$ of its children.

### Heap operations

* **Finding the max value** requires no effort as it is the root of the tree $$O(1)$$.
* **Insert**: we cannot directly attach the new node to root, so we start with one of the leaves, and if the recently added node is larger than its root, we should fix this problem which is called **sift-up** process, *we swap the problematic node with its parent until the problem is satisfied*. At the worst case it requires $$O(tree\ height)$$.
* **Extract max**: we replace the root with any leaf, and then we have to make sure the new change does not the break the max-heap properties or we need to do a **sift-down** process. *We swap the problematic node with larger child until the heap property is satisfied*. The running time of this procedure is $$O(tree\ height)$$.
* **Change Priority**: Now that we have both sift-up and sift-down we can provide a simply method for change an existed node priority and fix the possible problems using sift-up and sift-down. Running time $$O(tree\ height)$$.
* **Remove**: change a given node priority to a large value such as $$+\infty$$ and then use the **extract max** method. running time: $$O(tree\ height)$$.

* As all operations on tree's height, we like to keep the tree **shallow** as much as possible.

How to keep a tree shallow?

* **Using a complete binary tree**. A binary tree is **complete** if all its level are filled except possibly the last one which is filled from *left to right*. 

* **Advantages** of **complete** binary trees?

  1. A complete binary tree with $$n$$ nodes has height at most $$O(\lg n)$$.
  2. It can be stored as an **array** (efficient), we need no pointers!

  <img src="assets/priority-queue-02.png" style="zoom:30%"/>

* Is there any **downside**? **Yes, we need to keep the tree complete**! What operations could modify the shape of the tree?

  * **Insert**: to solve the problem with the insert method, we should insert the element in the **left-most vacant position in the last level** and then sift-up.
  * **extract-max**: to extract the max value, replace the root by the last leaf and then do the sift-down process.

### Pseudo code (MaxHeap)

[Example code for MinHeap](https://www.educative.io/edpresso/heap-implementation-in-python)

<img src="assets/priority-queue-03.png" style="zoom:60%"/>

<img src="assets/priority-queue-04.png" style="zoom:50%"/>

<img src="assets/priority-queue-05.png" style="zoom:50%"/>

<img src="assets/priority-queue-06.png" style="zoom:50%"/>

<img src="assets/priority-queue-07.png" style="zoom:50%"/>

<img src="assets/priority-queue-08.png" style="zoom:50%"/>

<img src="assets/priority-queue-09.png" style="zoom:50%"/>

<img src="assets/priority-queue-10.png" style="zoom:60%"/>

## Priority Queue (Heap Sort)