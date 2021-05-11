# Week 5

## Binary Search Trees

### Intro

Problems that we can solve using binary search trees:

* Dictionary Search: find all words that start with some given string.
* Date ranges: find all emails received in a given period.
* Closest height: find the person in your class whose height is closet to yours.

Local search is something that all of these problems have in common, operations that wee need are `RangeSearch` and `NearestNeighbors` and we also need `insert` and `delete` operations to keep it dynamic.

<img src="assets/BST-01.png" style="zoom:50%">

* None of the existing data structures work for us (hash table, unsorted array), but sorted arrays can search efficiently but not update.

<img src="assets/bst-08.png" style="zoom:50%">

### Basic operations

<img src="assets/BST-02.png" style="zoom:30%">

* Search tree helps us to work exactly like binary search. In search trees the left subtree has smaller keys, while the right subtree has bigger keys.

Basic operations:

* **Find**: if the item is not present in the tree, we can find a proper place to insert this item in the tree.

  <img src="assets/BST-03.png" style="zoom:20%">

<img src="assets/BST-04.png" style="zoom:50%">

<img src="assets/bst-09.png" style="zoom:50%">

* **Next** Element or adjacent node: given a node N in a binary search tree, would like to find adjacent element; if you have right child then go and find the leftmost item, which is closer to N than any item. If it has no right child, then you go up, and up until you find the bigger ancestor which is bigger than $N$. 

<img src="assets/bst-05.png" style="zoom:25%">

<img src="assets/bst-06.png" style="zoom:25%">

<img src="assets/bst-07.png" style="zoom:25%">

​	<img src="assets/bst-20.png" style="zoom:25%">

<img src="assets/bst-21.png" style="zoom:25%">	



* **Search**, `RangeSearch(x, y)`: a list of nodes with key between $x$ and $y$.

  <img src="assets/bst-10.png" style="zoom:50%">

  <img src="assets/bst-11.png" style="zoom:50%">

* **Insert**: adds node with key $k$ to the tree. Here, we can use a modified version of **find** function to find the appropriate place to put the key.

* **Delete**: removes node $N$ from the tree. Before you remove you should find the closest item which we expect to be the leftmost node in the right subtree:

  <img src="assets/bst-14.png" style="zoom:50%">

  <img src="assets/bst-11.png" style="zoom:50%">

<img src="assets/bst-13.png" style="zoom:50%">

### Runtime and time complexity

How long do Binary Search Tree operations take?

* Find $O(Depth)$

  <img src="assets/bst-15.png" style="zoom:50%">

  * But depth can be as bad as $n$.

    <img src="assets/bst-16.png" style="zoom:50%">

  * If we rearrange the tree with the same nodes, the depth can be smaller as well:

    <img src="assets/bst-17.png" style="zoom:50%">

* Our goal is to want left and right subtrees to have approximately the same size (**Balance**). Suppose it is perfectly balanced:

  * each subtree half the size of its parent.
  * after $log_2(n)$ levels, subtree of size 1.
  * operations run in $O(\lg n)$ time.

- Problem: Insertions and deletions can destroy balance! So, somehow we need a way to fix this problem, like **rearrange tree to maintain balance**.
- Problem: How do we rearrange tee while maintaining order? Idea: **Rotations**

<img src="assets/bst-18.png" style="zoom:50%">

<img src="assets/bst-19.png" style="zoom:50%">

* **How to keep a tree balanced? AVL trees!**

## AVL Trees