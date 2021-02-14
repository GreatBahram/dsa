# Dividing and Conquer

The idea of divide and conquer is to split the main problem into some subproblems and solve them instead of a large problem. Break the problem into non-overlapping subproblems of the same type, and at the end combine different parts.

## Introduction

## Problems

### Polynomial Multiplication

#### Naive algorithm

<img src="assets/polynomial-multiplication-01.png" style="zoom:15%">

#### Naive divide and conquer algorithm

What if you divide a multiplication into four parallel parts:

<img src="assets/polynomial-multiplication-02.png" style="zoom:15%">

Example:

<img src="assets/polynomial-multiplication-03.png" style="zoom:15%">

Implementation:

<img src="assets/polynomial-multiplication-04.png" style="zoom:15%">

Time complexity of this algorithm is the same as the naive algorithm **O(n^2)**.

<img src="assets/polynomial-multiplication-05.png" style="zoom:25%">

#### Efficient divide and conquer algorithm