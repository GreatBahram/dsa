# Week 5

## Binary Search Trees

### Intro

Problems that we can solve using binary search trees:

* Dictionary Search: find all words that start with some given string.
* Date ranges: find all emails received in a given period.
* Closest height: find the person in your class whose height is closet to yours.

Local search is something that all of these problems have in common, operations that wee need are `RangeSearch` and `NearestNeighbors` and we also need `insert` and `delete` operations to keep it dynamic.

* None of the existing data structures work for us, but sorted arrays can search efficiently but not update.

### Basic operations

* Find: if the item is not present in the tree, we can find a proper place to insert this item in the tree.
* Next Element or adjacent node: given a node N in a binary search tree, would like to find adjacent element; if you have right child then go and find the leftmost item, which is closer to N than any item. If it has no right child, then you go up, and up until you find the bigger ancestor which is bigger than $N$. 
* Search, `RangeSearch(x, y)`: a list of nodes with key between $x$ and $y$.
* Insert: adds node with key $k$ to the tree. Here, we can use a modified version of insert to find the appropriate place to put the key.
* Delete: removes node $N$ from the tree.

### Runtime and time complexity

How long do Binary Search Tree operations take?

* Find $O(Depth)$

  PICTURE

  * But depth can be as bad as $n$.
  * If we rearrange the tree with the same nodes, the depth can be smaller as well:

  PICTURE

* Our goal is to want left and right subtrees to have approximately the same size (**Balance**). Suppose it is perfectly balanced:

  * each subtree half the size of its parent.
  * after $log_2(n)$ levels, subtree of size 1.
  * operations run in $O(\lg n)$ time.

- Problem: Insertions and deletions can destroy balance! So, somehow we need a way to fix this problem, like **rearrange tree to maintain balance**.
- Problem: How do we rearrange tee while maintaining order? Idea: **Rotations**

PICTURE

## AVL Trees