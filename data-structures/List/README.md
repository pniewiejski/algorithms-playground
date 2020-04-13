# Linked list

Unlike arrays the order of linked list does not come from the placement in memory. Rather, it comes
from the fact that each element of the linked list points to the next element. In this sense, it is
a data structure that is a collection of nodes which are "linked together" into one structure.
Linked lists allow for efficient insertions and deletions. Compared to arrays, t is also much easier
to invert a linked list. A disadvantage, is the lookup time, which is linear (whereas for arrays
it's constant).

As was already pointed it is worth to stress out that consecutive nodes do not have to follow each
other in memory.

## Complexity

|          Operation          |                     Complexity                     |
| :-------------------------: | :------------------------------------------------: |
|          Indexing           |                       `O(n)`                       |
| Insert/delete at beginning  |                       `O(1)`                       |
| Insert/delete in the middle |                `search time + O(1)`                |
|    Insert/delete at end     | `O(n)` (if the last element is known it is `O(1)`) |

## Pros and cons

👍 Quick insertion and deletion operations.

👎 Linked lists use more memory than arrays, because of the necessity to store pointers.

👎 Because nodes are stored noncontiguously, it increases the time periods required to access
elements.
