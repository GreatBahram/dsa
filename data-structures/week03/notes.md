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

## Heap Sort

We will use binary heap to design heap sort algorithm which is fast and efficient sorting algorithm. **We can use priority queue to handle the heap sort algorithm** such as following:

<img src="assets/heap-sort-01.png" style="zoom:60%"/>

* The resulting algorithm is comparison-based and has running time $$O(n \lg n)$$.
* **Heap sort is a natural generalization of selection sort**: instead of simply scanning test rest of the array to find maximum value, use a smart data structure.
* **Problem**: We are using **additional space** to store the priority queue.

*In-place heap sort algorithm is possible*. For this, we will first turn a give array into a heap by permuting its elements.

Turn an array into a heap:

<img src="assets/heap-sort-02.png" style="zoom:50%"/>

* We repair the heap property going from bottom to top, running time: $$O(n \lg n)$$.

In-place Heap Sort (change the array into an increasing order):

<img src="assets/heap-sort-03.png" style="zoom:60%"/>

* It is in-place, we don't need additional space.
* It is efficient, even in the worst-case is $$O(n \lg n)$$.

#### Building a Heap running time

* The running time of `BuildHeap` is $$O(n \lg n)$$ since we call `SiftDown` for $$O(n)$$ nodes or more specifically: $$O(\frac{n}{2}.\lg n)$$.
* If a node is already close to the leaves the sifting it down is fast. And we have many such nodes! The question is was our estimation of the running time of `BuildHeap` too pessimistic?

<img src="assets/heap-sort-04.png" style="zoom:50%"/>

<img src="assets/heap-sort-05.png" style="zoom:60%"/>

* This new insight does not change the running time of heap sort, as we have to do $$n - 1$$ `extract_max` operations. However, this helps to solve another problem faster, k largest or k smallest, this problem can be solved in $$O(n)$$ if $$k \leq \frac{n}{\lg n}$$. Because we first have to create a heap in $$O(n)$$ then we need to do k extract_max method:

  <img src="assets/heap-sort-06.png" style="zoom:60%"/>

Running time: $$O(n + k \lg n)$$, if $$k \leq \frac{n}{\lg n}$$ then the running time is $$O(n)$$.

<img src="assets/heap-sort-07.png" style="zoom:50%"/>

For implementing a binary heap using zero-based array we can use the following formula:

<img src="assets/heap-sort-08.png" style="zoom:70%"/>

Binary Min-Heap can be used when we want to extract an item with minimum priority not its maximum:

<img src="assets/heap-sort-09.png" style="zoom:50%"/>

## Disjoint Sets (Union-Find)

* Understanding the problem from the course is a bit challenging, you can read a more simpler introduction on [Hackerearth](https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/).
* Union-Find data structure is useful in Graphs for performing various 
  operations like **connecting nodes**, **finding connected components**.

You have a set of elements S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}. Here you have 10 elements (N = 10 ).We can use  an array **Arr ** to manage  the connectivity of elements. Arr[ ] indexed by elements of set, having size of N (as N elements in set) and can be used to manage 
the above operations.

```c
void initialize(int Arr[ ], int N)
{
    for(int i = 0;i<N;i++)
    Arr[ i ] = i ;
}

//finding root of an element. This is influenced with the height of the tree
int root(int Arr[ ],int i)
{
    while(Arr[ i ] != i)  //chase parent of current element until it reaches root.
    {
     i = Arr[ i ];
    }
    return i;
}
/*modified union function where we connect the elements by changing the root of one of the element */

int union(int Arr[ ] ,int A ,int B)
{
    int root_A = root(Arr, A);       
    int root_B = root(Arr, B);  
    Arr[ root_A ] = root_B ;  // which one to hang? as we want to keep the tree
    // as shallow as we can, we must hang the shorter
}

bool find(int A,int B)
{
    if( root(A)==root(B) )  //if A and B have same root,means they are connected.
    	return true;
    else
    	return false;
}
```

<img src="assets/disjoint-sets-02.png" style="zoom:50%"/>

**Union by Rank**

The process of connecting the the tree with less nodes to the larger one is called **weighted_union** operation.

Initially the size of each subset will be one as each subset will  have only one element and we can initialize it in the initialize  function discussed above, size[ ] array will keep track of size of each subset:

```c
//modified initialize function:
void initialize( int Arr[ ], int N)
{
    for(int i = 0; i < N; i++)
    {
        Arr[i] = i ;
        size[i] = 1;
	}
}
```

**root()** and **find()** function will be same as above. Union function will be modified as we will connect two subsets according to the number of elements in subset.

```c
void weighted-union(int Arr[ ],int size[ ],int A,int B)
{
    int root_A = root(A);
    int root_B = root(B);
    if(size[root_A] < size[root_B ])
    {
        Arr[ root_A ] = Arr[root_B];
        size[root_B] += size[root_A];
	}
    else
    {
        Arr[ root_B ] = Arr[root_A];
        size[root_A] += size[root_B];
    }
}
```

Now, the height of any tree in our forest is at most $$\lg n$$, this will immediately implies that any operation is computed at $$\lg n$$.

<img src="assets/disjoint-sets-03.png" style="zoom:50%"/>

The union by size/rank heuristic guarantees that union and find methods work in time $$O(\lg n)$$.

**Path compression**

Another improvement is to save the parent when we find it, or other way to say it is to attach each node to its root.

<img src="assets/disjoint-sets-04.png" style="zoom:50%"/>

```c
// path compression
int root (int Arr[ ] ,int i)
{
    while(Arr[i] != i)
    {
        Arr[i] = Arr[Arr[i]]; 
		i = Arr[i]; 
    }
	return i;
}
```

When we use **weighted-union** with **path compression** it takes $$\lg^* n$$ for each union find operation,where $$n$$ is the number of elements in the set.

* $$\lg^* n$$ is the **iterated logarithmic** function which computes the number of times you have to take log of N till the value of $$n$$ is less or equal than 1.
* $$\lg^* n$$ is much better than $$\lg n$$, as its value reaches at most up to 5 in the real world.



<img src="assets/disjoint-sets-05.png" style="zoom:50%"/>

<img src="assets/disjoint-sets-06.png" style="zoom:30%"/>



<img src="assets/disjoint-sets-07.png" style="zoom:50%"/>

* When using path comprehension, $$rank[i]$$ is no longer equal to the height of the subtree rooted at $$i​$$, i.e. path comprehension decreases the height of each tree.