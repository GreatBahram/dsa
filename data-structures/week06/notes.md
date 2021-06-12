Until now, we talk about how to keep our tree balanced in order to have operations in $O(\lg n)$. But it turns out, there are wide range of data structures that do this in a different way, such as red-black tree, and splay trees.

Problem: What if we have some element that we frequently search for them:

<img src="assets/splay-01.png" style="zoom:50%">

For example, if we search for 1, 5, 7 items more so often, then it is better to use the unbalanced tree.

* So the idea is that we want common nodes near root. don't know which those node will be.
* what if we bring the queried node to the root:

<img src="assets/splay-02.png" style="zoom:50%">

There are three scenarios:

The first one is zig-zig when the node and its parent and its grand-parent are on the same side:

<img src="assets/splay-03.png" style="zoom:50%">Another case is when the parent and the grand parent are on the opposite side:

<img src="assets/splay-04.png" style="zoom:50%">

Last case when a node only has a parent, there is no grand parent:

<img src="assets/splay-05.png" style="zoom:50%">

We add a new operation to the binary search trees, which is called splay operation which tries to bring a node to the root of the tree. We keeps splay until the the node is root.

<img src="assets/splay-06.png" style="zoom:50%">