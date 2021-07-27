# Graph Basics

Graphs are abstractions to represent connection between objects. You can represent many things using graphs:

* Network Connection
* Maps
* Social Networks

**Definition**

An undirected Graph is a collection of $V$ of vertices, and a collection of $E$ of edges each of which connects a pair vertices.

<img src="assets/graph-01.png" style="zoom:50%"/>

* We could have multiple edges between same vertices or a loop connects a vertex to itself. If a graph has neither is called **simple graph**.

**Graph Representation**

So far, we said a graph is consisted of a bunch of vertices (nodes), and also a couple of edges which connect these vertices. There are many ways to represent graphs and different ways have different computation cost.

**Edge List**: we store a list of edges

<img src="assets/graph-02.png" style="zoom:50%"/>

**Adjacency Matrix**: Entries 1 if there is an edge, 0 if there is not.

<img src="assets/graph-03.png" style="zoom:50%"/>

**Adjacency List**: For each vertix, store a list of adjacent vertices.

<img src="assets/graph-04.png" style="zoom:50%"/>

**Summary**

Different operations are faster in different representations.

<img src="assets/graph-05.png" style="zoom:50%"/>

* For many problems, want **adjacency list**.

**Graph algorithms runtime**

* Runtime depends on $|V|$ and $|E|$, $(|V| + |E|)$ is considered linear time.
* So, it really depends on the density of graph

<img src="assets/graph-06.png" style="zoom:50%"/>

<img src="assets/graph-07.png" style="zoom:50%"/>