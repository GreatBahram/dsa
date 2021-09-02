# Paths in Graphs 2

## Fastest Route

What is the problem?

<img src="assets/graph-01.png" style="zoom:50%"/>

We are looking for the shortest path, not the minimum number of segments which we solved this using BFS, but looking for a shortest sum of the weights.

In the below case, our BFS algorithm fails to find the optimal solution:

<img src="assets/graph-02.png" style="zoom:50%"/>

### Naive Algorithm

Here we assume we have a upper bound on actual distance from $S$ to $v$ and when we go further we check if going from S to v using another edge such as $u$ if this new path is shorter than our current way, then we'd update the distance array.

* Basically, we are checking whether it is possible to improve our current estimation or not.

<img src="assets/graph-03.png" style="zoom:50%"/>

<img src="assets/graph-04.png" style="zoom:50%"/>

<img src="assets/graph-05.png" style="zoom:50%"/>

**Dijkstra's algorithm**

* We maintain a set $R$ of vertices for which $dist$ is already set correctly ("known region").
* The first vertex added to $R$ is $S$.
* On each iteration we take a vertex outside of $R$ with minimal dist-value, add it to $R$, and relax all outgoing edges.

<img src="assets/graph-06.png" style="zoom:50%"/>

* Running time of this algorithm depends on what data structure you're going to use for the $H$, it would be $|V^2|$ if you go for a simple array.
* Dijkstra can find the minimum time to get from work to home.
* It works for any graph with **non-negative** edge weights. Because in every round Dijkstra will settle a node, finalize a node if you later find a negative weighed edge, this could lead to a shorter path to that settled node.
* Works in $O(|V|^2)$ or $O((|V| + |E|) log (|V|))$ (priority-queue) depending on the implementation. In the worst case $|E|=|V^2|$, so it becomes $O(|V| +|V^2| \lg{|V|})$ which equals $O(|V^2| \lg{|V|})$. In the best case there is no edges so overall cost would be $O(|V|\lg{|V|})$.
* While Dijkstra's algorithm **may fail** to find optimal path on certain graphs with negative weights, having a **negative cycle** is a bigger problem for **any** shortest path graph.
* It works for both **directed** and **undirected** graphs.

## Currency Exchange

In this part we are going to learn how to find the shortest path even if some of the edge weights can be negative.

<img src="assets/graph-07.png" style="zoom:50%"/>

Triangle arbitrage illustrates the fact that sometimes it is possible to make three trades ($USD \rightarrow EURO, EURO \rightarrow POUND, POUND \rightarrow USD$) so that you make some profit.

<img src="assets/graph-08.png" style="zoom:50%"/>

<img src="assets/graph-09.png" style="zoom:50%"/>

There might exist an infinite number of conversions:

<img src="assets/graph-10.png" style="zoom:50%"/>

<img src="assets/graph-11.png" style="zoom:50%"/>

This problem is not compatible with the shortest path one, how to reduce to shortest paths:

* replace products with **sum** by taking logarithms of weights.
* in the shortest path problem we want to minimize the distance while here we want to maximize so we **negate** weights to solve minimization instead of maximization.

**Taking the logarithm**

<img src="assets/graph-12.png" style="zoom:50%"/>

**Negation**

<img src="assets/graph-13.png" style="zoom:50%"/>

**All together**

<img src="assets/graph-14.png" style="zoom:50%"/>

<img src="assets/graph-15.png" style="zoom:50%"/>

Did we solve the problem? No, this does not exactly work.

<img src="assets/graph-16.png" style="zoom:50%"/>

Dijkstra's algorithm will pick 5 for S-A, while S-B-A is a better path. This example can also happen in currency exchange example:

<img src="assets/graph-17.png" style="zoom:50%"/>

If we take -logarithm from these vertices, it is still beneficial to go from $RUR \rightarrow EURO, EURO \rightarrow USD$, don't forget we are minimizing the currency exchange.

<img src="assets/graph-18.png" style="zoom:50%"/>



There might exist a negative weight cycle:

<img src="assets/graph-19.png" style="zoom:50%"/>

### Bellman-Ford algorithm

which is an algorithm for shortest path when edges can have negative weights.

Its benefit over Dijkstra's algorithm it works even for negative edge weights, it is a bit **slower** than Dijkstra, but covers everything.

* This algorithm assumes there **are not** negative weight cycles in $G$, otherwise it **may not** return correct distances for some of the node.

<img src="assets/graph-20.png" style="zoom:50%"/>

<img src="assets/graph-21.png" style="zoom:50%"/>

How to deal with negative cycles in graphs

* Detect and find the cycle if you know there is one.

We did $|V| - 1$ iteration in Bellman-Ford algorithm, so if you run one more iteration and the distances change then we realize that there is a negative weight cycle.

<img src="assets/graph-22.png" style="zoom:50%"/>

<img src="assets/graph-23.png" style="zoom:50%"/>

This proof says even if there is a cycle (non-negative) more iteration does not result in changing distances. Because it is positive and we are looking for shortest path and that cycle can be removed.

​																	<img src="assets/graph-24.png" style="zoom:50%"/>

Second proof says imagine there is a negative cycle but it won't result in relaxation (contradiction):

<img src="assets/graph-25.png" style="zoom:50%"/>

This summation says it is positive while we know that this is a negative cycle, so this is a contradiction.

If we know there is a negative cycle, we want to find it, at least one of them:

<img src="assets/graph-26.png" style="zoom:50%"/>

<img src="assets/graph-27.png" style="zoom:50%"/>

### Infinite Arbitrage

<img src="assets/graph-28.png" style="zoom:50%"/>

<img src="assets/graph-29.png" style="zoom:50%"/>

<img src="assets/graph-30.png" style="zoom:50%"/>

How to detect infinite Arbitrage

<img src="assets/graph-31.png" style="zoom:50%"/>

<img src="assets/graph-32.png" style="zoom:50%"/>
