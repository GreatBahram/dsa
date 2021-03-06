# Week 1

## Arrays and Linked Lists

### Array

There are two ways to store arrays in memory, namely **row-major** and **column-major** (the first index changes rapidly).

Array's items can be accessed in $$O(1)$$ using the following formula:

$$array\_addr + element\_size * (i - start\_index)$$

<img src="assets/array-01.png" style="zoom:30%"/>

### Linked lists

Arrays have the following limitations:

1. The size of the arrays is fixed.
2.  Inserting at the beginning or middle of the array is expensive.

Advantages of Linked lists over arrays:

* Dynamic size
* Ease of insertion/deletion

Drawbacks:

* Random access is not allowed. You should access them sequentially.
* Extra memory for pointers

Each node in a list consists of at least two parts:

1. Data
2. Pointer

<img src="assets/singly-linked-list.png" style="zoom:20%"/>

#### Doubly-Linked-list

We can solve previous $$O(n)$$ operations using two pointers, so each node contains:

1. Key
2. next Pointer
3. previous Pointer

Before adding the tail pointer all front actions were cheap but the operations that were dealing with the tail were pretty expensive. After adding tail everything was except for Pop back which takes $$O(n)$$. When we switch to doubly-linked-list popback and add_before operations become $$O(1)$$.

<img src="assets/doubly-linked-list.png" style="zoom:30%"/>

[Link to this week slides](https://d3c33hcgiwev3.cloudfront.net/_52e80f34296ebf21912ca201cabebef8_05_1_arrays_and_lists.pdf?Expires=1617321600&Signature=Hcrvg9eeJCR59NdOPpeBxtQ0deBwASOWxYA4fnbFxEA~2jdtlkZDDXO5DTfb7FhJdLM8UsCXrVJJZnfuKW1~oPGIjHNi9nl27VXC3nkmPVtQBjVi~vtUui8EP2vHhLoGZ5woyTYbcZfwqLDofEjFFbrJfqUkeUNS36ShwDAAoro_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

## Stacks and Queues

Stack (LIFO) can be implemented with either an array or a linked-list (You simply push-front for each item, and for popping you do pop-front). The array might have a fixed-size limitation, on the other hand, with linked-list you're free to add as many as you want.

```python
class Stack:
    def push(self, item):
        pass
    
    def pop(self):
        pass
    
    @property
    def top(self):
        pass
    
    @property
    def is_empty(self):
        pass
```

Queue (FIFO)

Queues can be implemented with either a **linked-list** (with tail pointer) (Enqueue: `List.PushBack`, Dequeue: `PopFront`)or an **array**. Remember, each queue operation should be $$O(1)$$.

https://www.codesdope.com/course/data-structures-queue/

```python
class Queue:
    def enqueue(self, item):
        """Add a given item into the container."""

    def dequeue(self):
        """Remove and return the least recently-dded key."""
	@property
	def is_empty(self) -> bool:
        pass
```

## Trees

A Tree is:

* empty, or
* a node with:
  * a key, and
  * a list of child trees.

A Node in tree contains:

* Key
* Children: List of children nodes
* (Optional) parent

For binary tree: node contains:

* key
* left
* right
* (optional) parent

```python
def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.left), height(tree.right))


def size(tree):
    """How many nodes are in a given tree."""
    if tree is None:
        return 0
    return 1 + size(tree.left) + size(tree.right)
```

* The **depth** of a node is the number of edges from the node to the tree's root node. A root node will have a depth of 0 (or 1 depending on our definition).
* The **height** of a node is the number of edges on the *longest path* from the node to a leaf.
  A leaf node will have a height of 0.

https://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height

### Tree Traversal

There are two main ways to traverse a tree:

1. Depth-first: We completely traverse one sub-tree before exploring a sibling sub-tree.

   ```python
   def inorder_traversal(tree: Tree):
       """It only makes sense in binary search tree."""
       if len(tree) < 1:
           return None
       inorder_traversal(tree.left)
       print(tree.key)
       inorder_traversal(tree.right)
   
   
   def preorder_traversal(tree):
       """
       Preorder and Postorder make sense for any
       kind of trees.
       """
       if len(tree) < 1:
           return None
       print(tree.key)
       preorder_traversal(tree.left)
       preorder_traversal(tree.right)
   
   
   def postorder_traversal(tree):
       """
       Post order traversal can be used to evaluate a arithmetic expression.
       Because in a post-order traversal we evaluate all children fully before
       evaluating a node itself.
       """
       if len(tree) < 1:
           return None
       postorder_traversal(tree.left)
       postorder_traversal(tree.right)
       print(tree.key)
   ```

2. Breadth-first: we traverse all nodes at the one level before progressing to the next level. We'd use a **queue** instead of a **stack**.

   ```python
   def level_traversal(tree):
       q = Queue()
       q.enqueue(tree)
       while not q.empty():
           node = q.dequeue()
           print(node)
           if node.left:
               q.enqueue(node.left)
           if node.right:
               q.enqueue(node.right)
   ```

* When working with a tree, recursive algorithms are common.

## Problems

- Check brackets in the code: Stack exercise.
- Tree height: testing our understanding of tree.
- Network packet processing simulation: using queue or dequeue sometimes saves your ass immensely.
- Stack with maximum: using auxiliary data structure is perhaps better than some stupid ideas.
- Maximum in Sliding Window: You should appreciate dequeue more than you think.
