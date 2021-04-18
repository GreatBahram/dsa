# Hashing

Convert an IP Address to 32-bit integer number:

```python
ip_address = "192.168.1.100"
def ip_to_int(ip_address):
    octeds = list(map(int, ip_address.split(".")))
    # return octeds[3] | octeds[2] << 8 | octeds[1] << 16 | octeds[0] << 24
    return octeds[0] * 2**24 + octeds[1] * 2 ** 16 + octeds[2] * 2 ** 8 + octeds[3]
```

A hash function receives an input and it generates a number between 0 and $$m - 1$$. So $$m$$ is the **cardinality** of the the hash-function, i.e. m is the number of elements that this set can hold.

## Chaining Technique

Hash tables in our case study has three important methods:

* HasKey
* Get
* Set

<img src="assets/hash-tables-01.png" style="zoom:30%"/>

<img src="assets/hash-tables-02.png" style="zoom:30%"/>

<img src="assets/hash-tables-03.png" style="zoom:30%"/>

Because collision can happen for two objects and as we use **chaining** technique, then the running time or operation in hash table depends on number of items exists in a retrieved list $$\Theta(c + 1)$$:

<img src="assets/hash-tables-04.png" style="zoom:50%"/>

A **set** is just a hash table which only holds keys not values, and has three methods: add, remove, find.

<img src="assets/hash-tables-06.png" style="zoom:40%"/>

<img src="assets/hash-tables-07.png" style="zoom:40%"/>

<img src="assets/hash-tables-08.png" style="zoom:40%"/>

<img src="assets/hash-tables-09.png" style="zoom:40%"/>

* Chaining is a technique to implement a hash table.
* Memory consumption is $$O(n + m)$$, $$n$$ is the number pairs inside the array.
* Operations work in $$O(c + 1)$$ where $$c$$ is the longest chain.
* How to make both $$c$$ and $$m$$ small?

## Hash functions

* Hash functions should be **deterministic**, this means we cannot use random values despite its good characteristics, such as uniformity.
* **Fast** to compute.
* **Distributes** keys **well** into different cells.
* **Few collisions**.

* $$\alpha$$ or *load factor* is $$\frac{n}{m}$$, which measures how filled up is our hash table.

* We want to have small $$m$$ to use less memory and small $$c$$ to have an efficient search.

<img src="assets/hash-functions-01.png" style="zoom:50%"/>

In order to prevent collisions we're gonna use this approach:

Similar to the quick sort pivot selection which was random, we desire to have randomness but we must be deterministic at the same time. So we define a set of hash functions which called **universal family** and we randomly choose one of them.

<img src="assets/hash-functions-02.png" style="zoom:30%"/>

How this new idea is going to help us? Well, we say the collisions are acceptable if the probability of the collision for two different values among hash functions  is below $$\frac{1}{m}$$, i.e. it means we don't have collisions in $$1-\frac{1}{m}$$.

* $$h$$ is chosen randomly from a universe family.

<img src="assets/hash-functions-03.png" style="zoom:25%"/>

Second problem is choosing a value for hash table size, we want to keep our hash table not too crowded as it impacts the performance of the hash table. and operations will happen in $$O(1 + a)$$.

<img src="assets/hash-functions-04.png" style="zoom:25%"/>

Making the hash table size static will severely impact the hash table performance. We need to use the same idea we had in the dynamic array, this time however, we're gonna double the hash table size whenever we hit the a certain $$a$$.

<img src="assets/hash-functions-05.png" style="zoom:25%"/>

In this case, we will double the hash table size and choose a new hash function which matches hash table cardinality and compute the hash of each value and then insert it inside the new hash table.

<img src="assets/hash-functions-06.png" style="zoom:30%"/>

* You should call `Rehash` after each operation with the hash table. Similarly to dynamic arrays, single rehashing takes $$O(n)$$ time, but the amortized running time of each operation with hash table is still $$O(1)$$ on average, because rehashing will be rare.

#### Hashing Integers

Now, we need to create a universal family hash functions, and inside it we will have a hash functions for most of important objects, such as integers and strings.

1. Choose prime number bigger than your data range, for example in our case we needed to save $$10^7$$, $$p=10\ 000\ 019 $$, $$m=10$$.

<img src="assets/hash-functions-08.png" style="zoom:50%"/>

The size of this hash family is $$p(p-1)$$, because a hash $p-1$ allowed values and $b$ has $p$ values, and they are independent.

<img src="assets/hash-functions-09.png" style="zoom:50%"/>

In summary:

<img src="assets/hash-functions-10.png" style="zoom:50%"/>

#### Hash strings

For our use case, phone book, we need to implement a map from users to phone numbers. We need a hash function defined on names.

<img src="assets/hash-functions-11.png" style="zoom:50%"/>

<img src="assets/hash-functions-12.png" style="zoom:50%"/>

<img src="assets/hash-functions-13.png" style="zoom:50%"/>

<img src="assets/hash-functions-14.png" style="zoom:50%"/>

* The size this hash function is $p-1$ as x could have $p-1$ values.

Implementation:

<img src="assets/hash-functions-15.png" style="zoom:50%"/>

For any $a,b$ and $p$ the following properties of module arithmetics are true:

1. $(a + b)\ mod\ p) mod\ p = (a + b) mod\ p$
2. $$(a\ mod\ p) b\ mod\ p = ab\ mod\ p$$

<img src="assets/hash-functions-16.png" style="zoom:70%"/>

Efficiency of our algorithm:

<img src="assets/hash-functions-17.png" style="zoom:70%"/>

Hash strings - cardinality

All hash functions in the family have a cardinality of $$P$$, where $P$ is very big prime number, and what we want is the cardinality of hash functions to be the same size as the size of our hash table.

How to fix this?

First we design a complex transformation from strings to numbers, from 0 to $m - 1$, so we select the cardinality of $m$, we want a function from strings to numbers, from 0 to $m-1$.

To do that, we first apply our random hash function from *polynomial family* to strings, and we get some integer number modulo $P$ and then we can apply a random hash function from the universal family for integers less than $P$ and we get a number between $0$ and $m-1$.

To wrap it up, you first apply a random hash function from polynomial family to the string, and you get a number module P, then you apply another hash function to convert this number into a number between 0 and $m-1$. The second hash function for converting the number from first stage is selected from universal family of integers.

* Choose cardinality $m$ and prime number $p > m$. Choose a random hash function $h$ from the polynomial hash family $P_p$. Choose a random hash function $h_{int}$ from the universal family $H_p$ for integers between 0 and $p - 1$. Then use hash function $h_m(x)=h_{int}(h(x))$.

<img src="assets/hash-functions-18.png" style="zoom:30%"/>

<img src="assets/hash-functions-19.png" style="zoom:30%"/>

* So if choose $p> mL$ then this would a really good universal hash function.

<img src="assets/hash-functions-20.png" style="zoom:25%"/>

## Searching Patterns 

### Finding pattern in Text

We have a text (T) and a pattern (P), our goal is to find all positions that match the pattern.

 <img src="assets/pattern-matching-naive-01.png" style="zoom:50%"/>

 <img src="assets/pattern-matching-naive-02.png" style="zoom:50%"/>

 <img src="assets/pattern-matching-naive-03.png" style="zoom:50%"/>

 <img src="assets/pattern-matching-naive-04.png" style="zoom:50%"/>

 <img src="assets/pattern-matching-naive-05.png" style="zoom:50%"/>

### Rabin-Karp's Algorithm 

We need to compare $P$ with all substrings $S$ of $T$ of length $|P$|. The idea is that we can make the previous algorithm faster using hashing algorithm. if $h(P) \neq h(S)$, then definitely $P \neq S$. However, if $h(P) = h(S)$, call `AreEqual(P, S)` to make sure. We hope this would happen rarely, the collision, in fact we can somehow increase this odd, by choosing a large prime number (`PolyHash`). if $P \neq S$, the probability $Pr[h(P) = h(S)]$ is at most $\frac{|P|}{p}$ for polynomial hashing.

<img src="assets/pattern-matching-naive-06.png" style="zoom:50%"/>

   False alarms: False alarm is the event when $P$ is compared with $T[i..i+|P|-1]$, but $P \neq T[i..i+|P| -1]$. The probability of "false alarm" is at most $\frac{|P|}{p}$, the total number of false alarm will be $(|T|-|P|+1)\frac{|P|}{p}$, which can be made small by select $p>>|T||P|$.

<img src="assets/pattern-matching-naive-07.png" style="zoom:30%"/>

<img src="assets/pattern-matching-naive-08.png" style="zoom:30%"/>

<img src="assets/pattern-matching-naive-09.png" style="zoom:30%"/>

<img src="assets/pattern-matching-naive-10.png" style="zoom:50%"/>

* Save as our naive algorithm but can be improved, using precomputed hash.