# Directed Graphs

Sometimes we want the edges of a graph to have a direction.

A **directed graph** is a graph where each edge has a start and end vertex. Directed graphs might be used to represent:

* Streets with one-way roads
* Links between webpages
* Followers on social network
* Dependencies between tasks

<img src="assets/graph-01.png" style="zoom:30%"/>

We can do them in some order but not any order. One of the things we'd like to do is to find the ordering of the tasks:

<img src="assets/graph-02.png" style="zoom:30%"/>

So if we have one of these dependency graphs, we like to linearly order the vertices to respect these dependencies.

* is it always possible to do this? No! If your graph $G$ has any cycle, it cannot be linearly ordered. What this means, in order to be linearly orderable you need to have a **D**irected **A**cyclic **G**raph (DAG), which has no cycle.
* But is this sufficient?   

<img src="assets/graph-03.png" style="zoom:40%"/>

<img src="assets/graph-04.png" style="zoom:35%"/>

Basic idea on how to produce a linearly ordered:

<img src="assets/graph-05.png" style="zoom:35%"/>

Before we get there, there is a question, how do we know that there is a sink? For DAG at least there is an easy way to do this:

Follow path as far as possible, $v_1 \rightarrow v_2 \rightarrow \dots \rightarrow v_n$. Eventually either:

* Cannot extend (found sink)
* Repeat a vertex (have a cycle)

<img src="assets/graph-06.png" style="zoom:30%"/>

<img src="assets/graph-07.png" style="zoom:40%"/>

* But, here we are doing something **ineffectively**:
* * Retrace same path every time
* Instead only back up (go back) as far as necessary: we could back up only one step along the path and keep going from there. That's what we are going to do, and this is just DFS! We are sorting vertices based in postorder!

<img src="assets/graph-08.png" style="zoom:35%"/>

## Strongly Connected Components

Two vertices $v$, $w$ in a directed graph are *connected* if you can reach $v$ from $w$ and can reach $w$ from $v$.

* A directed graph can be partitioned into *strongly connected components* where two vertices are connected if and only if they are in the same component.

<img src="assets/graph-09.png" style="zoom:30%"/>

<img src="assets/graph-10.png" style="zoom:30%"/>

* The meta-graph of a graph $G$ is always a DAG.

<img src="assets/graph-11.png" style="zoom:30%"/>

**Computing Strongly connected components** (`SCC`)

* How do we find the strongly components of  graph $G$:

<img src="assets/graph-12.png" style="zoom:30%"/>

What's the idea behind this algorithm: if you take a vertex $v$ and run the explore algorithm you'll find everything that you can reach from $v$, and this includes components of $v$ but you might find vertices from other connected components as well.

* However, there is a case that this does not happen:

<img src="assets/graph-13.png" style="zoom:30%"/>

So you pass a sink node, you would get the exact connect components which is itself. So need a way to find a sink SCC.

<img src="assets/graph-14.png" style="zoom:30%"/>

So, according to the above theorem the vertex with the largest postorder number is in a **source** component!

But we wanted a **sink** component! There is a trick for doing this:

<img src="assets/graph-15.png" style="zoom:30%"/>

<img src="assets/graph-16.png" style="zoom:40%"/>

So, in order to find a sink component of $G$ you run DFS on the reverse graph of $G$ (or $G^R$). And Take the vertex with the largest postorder.

* The vertex with the largest postorder number in $G^R$ is in a sink SCC of $G$.

<img src="assets/graph-17.png" style="zoom:40%"/>

This algorithm is a little bit expensive as we run the DFS algorithm repeatedly on the reverse graph, and it turns out it is unnecessary according to the Theorem we introduced above:

<img src="assets/graph-18.png" style="zoom:30%"/>

<img src="assets/graph-19.png" style="zoom:30%"/>

<img src="assets/graph-20.png" style="zoom:40%"/>