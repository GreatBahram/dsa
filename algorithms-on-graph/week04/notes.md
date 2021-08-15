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
* It can also find the fastest route from work to home. Works for any graph with **non-negative** edge weights.
* Works in $O(|V|^2)$ or $O((|V| + |E|) log (|V|))$ (priority-queue) depending on the implementation.

## Currency Exchange