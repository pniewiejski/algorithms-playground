# Hash table

- [Read more on Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [Simple implementation in Python](./simple_hash_map.py)

Hash table (or _hash map_) is a data structure that implements an associative array abstract data
type, meaning that it is a structure which maps _keys_ to _values_.

Hash table will employ a special **hash function** which it will use to compute an index. This index
(also known as _the hash code_) allows us to access the appropriate "slot" where the _value_ is
stored.

In an ideal case a **hash function** will assign each key a different index. In the real world there
is a possibility that a **collision** will occur. When implementing a hash table we need to
accommodate for such a case.

The greatest benefit of using hash tables is that, when working correctly, a hash table should have
a constant lookup time. This means that a time complexity of a lookup is `O(1)`. In a pessimistic
condition a lookup time can become linear - `O(n)`.

There are lots and lots of use cases for hash maps. To name just a few examples:

- Looking for duplicates.
- Hash maps are ofter used to implement caches. Thinks for instance about the way Redis works.
- Associative arrays
- Languages like Python, Ruby or JavaScript use hash maps to represent objects

## Choosing the hash function 🤔

- A good hash function will result in a uniform spread of values in the array.
- On the other hand, a poorly constructed hash function will result in writing items in groups and
  lots of collisions.

We want to have a hash function that will provide a uniform distribution of hash values.

## Resizing

For any hash table we can define a **load factor**, which is a ratio between the number of all
_slots_ (_buckets_) `k` and the number of occupied entries in the table `n`.
![\text{load factor}=\frac{n}{k}](https://render.githubusercontent.com/render/math?math=%5Ctext%7Bload%20factor%7D%3D%5Cfrac%7Bn%7D%7Bk%7D)

As the load factor grows, the hash table will become slower. The constant lookup time depends on
keeping the load factor beneath a certain value. Usually we do not want the load factor to be
greater than `0.7`.

To keep the load factor small, hash table can be resized. This process is sometimes called
_rehashing_. Rehashing consists of increasing the size of underlying data structure and mapping
existing entries to new _slots_. There is a number of strategies that could be followed.
[Read more here.](https://en.wikipedia.org/wiki/Hash_table#Dynamic_resizing)

## Downsides 👎

- They become inefficient when there is a lot of collisions.
  [Check out this paper](https://www.eng.tau.ac.il/~yash/C2_039_Wool.pdf), where weakness of The
  Linux Routing Table, which uses hash table, is described.
- Although hash maps have a low time complexity, cost of a single operation can be quite high.
- We can enumerate entries in a hash table efficiently (constant const per entry) only in a
  sudo-random order. There is no efficient way to locate an entry whose key is _"nearest"_ to a
  given key. If we wanted to list entries in some specific order, we would need an additional
  sorting step.
- Because a hash function computation can be quite costly, hash tables may not be the best choice if
  the number of entries is small.
