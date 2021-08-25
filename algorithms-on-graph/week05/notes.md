## Minimum Spanning Trees

We are looking for a subset of the edges of a connected that **connects all** the vertices together, **without any cycles** and with the **minimum** possible total edge weight.

The word tree at minimum spanning tree refers to the fact, each solution of the minimum spanning tree is going to build a tree.

Properties of Trees:

1. A tree is an undirected graph that is connected and acyclic.
2. A tree on $n$ vertices has $n-1$ edges.
3. Any connected undirected graph $G(V, E)$ with $|E|=|V|-1$ is a tree.
4. An undirected graph is a tree iff there is a unique path between any pair of its vertices.

#### Greedy Algorithms

At the end of this week, we will introduced to two efficient greedy algorithms for the minimum spanning tree problem.

The main idea behind Kruskal and Prim algorithms:

<img src="assets/mst-01.png" style="zoom:50%"/>

Example: Using the same graph for both of these algorithms and compare the results:

<img src="assets/mst-03.png" style="zoom:50%"/>

#### Kruskal's Algorithm

<img src="assets/mst-04.png" style="zoom:50%"/>

Implementation details

1. use disjoint sets data structure
2. initially, each vertex lies in a separate set
3. each set is the set of vertices of a connected component
4. to check whether the current edge $\{u,v\}$ produces a cycle, we check whether $u$ and $v$ belong to the same set.

<img src="assets/mst-05.png" style="zoom:50%"/>

<img src="assets/mst-06.png" style="zoom:50%"/>

[What is the maximum number of edges in a graph](https://stackoverflow.com/questions/5058406/what-is-the-maximum-number-of-edges-in-a-directed-graph-with-n-nodes) (both directed and undirected).

* Sorted edges:

  $O(|E| \lg{|E|})$ = $O(|E| \lg{|V^2|})$, we used $|V^2|$ because that's the maximum number of edges inside a graph; $O(2|E| \lg{|V|})$ = $O(|E|\lg{|V|})$.

* Processing edges:

  $2|E|.T(Find) + |V| . T(Union)$; we have $2|E|$ as we used two find operation for both edges.

* if we use some sophisticated heuristics such as path compression and etc, the processing edges step will turn into $\lg^*$, but the as the sorted edges takes $O(|E| \lg{|V|}), it will dominate the second section.

#### Prim Algorithm
