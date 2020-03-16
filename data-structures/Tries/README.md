# Tries

Trie or a _prefix tree_ is a data structure that allows us to store a _set_ or an _associative
array_. With tries keys are usually strings.

> Unlike a binary search tree, no node in the tree stores the key associated with that node;
> instead, its position in the tree defines the key with which it is associated. All the descendants
> of a node have a common prefix of the string associated with that node, and the root is associated
> with the empty string.
>
> _[~Wikipedia - Tries](https://en.wikipedia.org/wiki/Trie)_

The name _trie_ comes from the word _retrieval_.

We could think of tries as storing letters of the alphabet in nodes and in order to **retrieve**
words one has to traverse down the tree.

Keep in mind that the size of the trie will the depend on the size of the "alphabet".

> Where _hash map_ were a combination of arrays and linked lists, _tries_ are a combination of
> arrays and pointers.

## Applications

- Autocomplete / predictive text (eg. on smartphone keyboard). Here we take advantage of tries'
  quick search, insert and delete operations.

- We can use trie as a replacement for a _hash map_. There are a couple of advantages of tries over
  hash maps:

  👌 Lookup is faster in the pessimistic case. A hash map with many collisions has a lookup time of
  `O(n)` (`n` being the number of entries), whereas trie has a lookup time of `O(m)`, where `m` is
  the length of the search string 👌 No collisions. 👌 No need for hash functions, which could be
  expensive to compute. However, there are also some disadvantages that we have to keep in mind. 👎
  Sometimes trie can take up more space than a hash map would 👎 Floating point key can lead to long
  chains & prefixes that are kinda useless 👎 Lookup time can be slower compared to a hash map
  (especially if we're dealing with a slow random-access read, like when reading from a hard drive.)

## Pros and cons

When compared to _hash maps_, tries have a few advantages:

👌 Lookup is faster in the pessimistic case. A hash map with many collisions has a lookup time of
`O(n)` (`n` being the number of entries), whereas trie has a lookup time of `O(m)`, where `m` is the
length of the search string

👌 No collisions.

👌 No need for hash functions, which could be expensive to compute.

However, there are also some disadvantages that we have to keep in mind.

👎 Sometimes trie can take up more space than a hash map would

👎 Floating point key can lead to long chains & prefixes that are kinda useless

👎 Lookup time can be slower compared to a hash map (especially if we're dealing with a slow
random-access read, like when reading from a hard drive.)

# Complexity

**Time complexity of creation of a trie is** `O(m + n)`, where `n` is the total number of words and
`m` is the length of the longest word.

Time complexity of **search**, **insert** and **delete** operations is `O(k * n)`, where `n` is the
total number of words and `k` is the length of word.

Notice that time of these operations depend on the word's length. So a shorter word will be searched
for (or inserted , or removed) faster than a longer word.

## Other sources 📚

- [Trying to understand tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
- [Harvard CS50](https://www.youtube.com/watch?v=TRg9DQFu0kU)
