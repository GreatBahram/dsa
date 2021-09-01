# Week 3

## Paths in graphs 1

### Paths and distances

What is the minimum number of flight segments to get from Hamburg to Moscow?

<img src="assets/graph-01.png" style="zoom:50%"/>

<img src="assets/graph-02.png" style="zoom:50%"/>

Finding shortest path from a starting point

<img src="assets/graph-03.png" style="zoom:50%"/>

We can use a simpler representation to do this task, which is called distance layers:

<img src="assets/graph-04.png" style="zoom:50%"/>

### Breadth-first Search

We process the graph layer by layer.

* We can use BFS to find the shortest path when the graph is **undirected** and **unweighted**.
* The graph should be **unweighted** because BFS does not check the weight of an edge, it will only search for the minimum segment.

### Implementation and Analysis

<img src="assets/graph-05.png" style="zoom:50%"/>

<img src="assets/graph-06.png" style="zoom:50%"/>

### Proof of Correctness

<img src="assets/graph-07.png" style="zoom:50%"/>

### Shortest-path Tree

<img src="assets/graph-08.png" style="zoom:50%"/>

<img src="assets/graph-09.png" style="zoom:50%"/>

* prev array/map holds the data about the parent node of $u$.

<img src="assets/graph-10.png" style="zoom:50%"/>

<img src="assets/graph-11.png" style="zoom:50%"/>
