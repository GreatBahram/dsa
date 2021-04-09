## Priority Queue

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

