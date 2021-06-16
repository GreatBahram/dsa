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

* **Delete**: removes node $N$ from the tree. Before you remove you should find the **closest** item which we expect it to be the leftmost node in the right subtree:

  <img src="assets/bst-14.png" style="zoom:50%">

<img src="assets/bst-13.png" style="zoom:50%">

### Runtime and time complexity

How long do Binary Search Tree operations take?

* Find $O(Depth)$

  <img src="assets/bst-15.png" style="zoom:50%">

  * But depth can be as bad as $n$.

    <img src="assets/bst-16.png" style="zoom:50%">

  * If we rearrange the tree with the same nodes, the depth can be smaller as well:

    <img src="assets/bst-17.png" style="zoom:50%">

* Our goal is the left and right subtrees to have approximately the same size (**Balance**). Suppose it is perfectly balanced:

  * each subtree half the size of its parent.
  * after $log_2(n)$ levels, subtree of size 1.
  * operations run in $O(\lg n)$ time.

- Problem: Insertions and deletions can destroy balance! So, somehow we need a way to fix this problem, like **rearrange tree to maintain balance**.
- Problem: How do we rearrange tee while maintaining order? Idea: **Rotations**

<img src="assets/bst-18.png" style="zoom:50%">

<img src="assets/bst-19.png" style="zoom:50%">

* **How to keep a tree balanced? AVL trees!**

## AVL Trees

If you have any problem with basic rotations, it is better to watch [this video](https://www.youtube.com/watch?v=u3OVSkuOdqI) before carrying on with the course's videos.

### Intro

We learned that in order to our search operations be fast we need to find a way to balance the tree. But before that we need a way to measure balance tree.

For that purpose we need to calculate the height of the tree:

<img src="assets/avl-01.png" style="zoom:50%">

The way we calculate the height of the tree:

<img src="assets/avl-02.png" style="zoom:50%">

* In order to reduce the computational cost we **save the height as an attribute on each node**:

<img src="assets/avl-03.png" style="zoom:70%">

<img src="assets/avl-04.png" style="zoom:50%">

* So our measure to understand whether the tree is balanced or not is the height of each subtree. We'd say the tree is balanced iff:

<img src="assets/avl-05.png" style="zoom:50%">

* In other words, the difference can be -1, 0, 1.
* Need to show that AVL property implies $Height=O(\lg(n))$. Alternatively, show that large height implies many nodes.

<img src="assets/avl-06.png" style="zoom:50%">

<img src="assets/avl-07.png" style="zoom:50%">

<img src="assets/avl-08.png" style="zoom:60%">

<img src="assets/avl-09.png" style="zoom:50%">

<img src="assets/avl-10.png" style="zoom:50%">

### AVL Trees Implementation

There two places that we need to take care of our balanced tree are:

* insertion
* deletion

We need a new insertion algorithm that involves rebalancing the tree to maintain the AVL property.

The basic idea of inserting is like this: 

* Firstly, we'd insert the node as before, then find that node in the tree and then run a rebalanced on the tree.

<img src="assets/avl-11.png" style="zoom:50%">

How do  we do the rebalancing? first if the $|N.left.height - N.right.height| <= 1$ , then it is fine and we don't need to do anything. but if it differs with more than one, the we'd do the rebalancing:

<img src="assets/avl-12.png" style="zoom:50%">

The `AdjuctHeight` function is pretty simple, we just calculate the height again:

<img src="assets/avl-13.png" style="zoom:50%">

Code for re-balance right:

<img src="assets/avl-24.png" style="zoom:30%">

**Delete** operation: before we delete it, we found its successor (next-larger), its successor probably isn't going to have a left child but it might have a right child. We take this successor and replace it with the node we are gonna to delete and the successor's right child replaces it. And we need to adjust the height of the successor parent to fix the height of the tree, because we either decrease or increase the successor's parent node.

<img src="assets/avl-14.png" style="zoom:50%">

New code for delete operation:

<img src="assets/avl-25.png" style="zoom:30%">

### New operations

Binary Search Trees have more interesting features such as you can recombine them, two new operations are:

* Merge: combine two binary search trees into a single one.
* Split: break one binary search tree into two

#### Merge

In general, to merge two sorted lists takes $O(n)$ time. However, when they are separated it is faster:

In merge operation we are given two roots $R_1, R_1$ with all keys in $R_1$'s tree smaller than those in $R_2$'s. What we should return is the root of a new tree with all the elements of both trees.

This problem was easy if we were given an extra node to add as root, in fact it takes $O(1)$:

<img src="assets/avl-26.png" style="zoom:40%">

<img src="assets/avl-27.png" style="zoom:35%">

But since no one is going to give that extra node, what we can do is to find the largest element say in left tree and delete it from left-tree and use it as the extra node:

* Remember, we modified the find function to return the best position that we can insert a new node.

<img src="assets/avl-28.png" style="zoom:30%">

* If we don't care about balancing that's it and we don't need to do anything else.

* Instead of re-balancing the whole tree, we go down side of the larger tree until we merge it with subtree of same height.

So, overall, the merge operation works like this:

<img src="assets/avl-29.png" style="zoom:35%">

Otherwise, what happens let's say if $R_1$ is bigger than $R_2$, we want to merge it with $R_1$ right child with $R_2$:

<img src="assets/avl-30.png" style="zoom:30%">

So the amount of time it takes isn't the depth of the tree, it is the number of step that we need to take:

 <img src="assets/avl-31.png" style="zoom:30%">

#### Split

Split breaks one tree into two:

<img src="assets/avl-32.png" style="zoom:30%">

<img src="assets/avl-33.png" style="zoom:30%">

All we have to do is find all subtrees that are less than x and bigger than x, and merge them together and return two tress at the end:

<img src="assets/avl-34.png" style="zoom:30%">

<img src="assets/avl-35.png" style="zoom:30%">

* But if we used the `AVLMergeWithRoot` it would make sure the tree is balanced as well  and we time complexity is $(\lg n)$