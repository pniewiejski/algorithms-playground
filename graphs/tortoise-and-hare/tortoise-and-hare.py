# This example is inspired by the Wikipedia's one
# https://en.wikipedia.org/wiki/Cycle_detection 

_x0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
_f = [6, 6, 0, 1, 4, 3, 3, 4, 0]


def get_value_at(x):
    return _f[x]


def tortoise_and_hare(x0, f):
    # We want to find x_i == x_2i
    # Hare is moving twice as fast as tortoise
    # With every iteration the distance between them increases by one.

    # At some point both hare and tortoise 
    # are going to be in the cycle

    # expression f(x) the element of _f for x from _x
    # this basically comes down to reading a value under "pointer"
    tortoise = f(x0)
    hare = f(f(x0))

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Find the begining of the cycle
    # `u` will denote a position of the first duplicate 
    u = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)  # Hare and tortoise move at same speed!
        u += 1

        # Find the length of the shortest cycle starting from `x_u`
    # Hare moves one step at a time while tortoise is still.
    # Increment `l` until `u` is found.
    l = 1
    hare = f(hare)
    while tortoise != hare:
        hare = f(hare)
        l += 1

    return l, u


if __name__ == "__main__":
    cycle_len, cycle_position = tortoise_and_hare(0, get_value_at)
    print("Cycle begins at: {}, and is of length: {}".format(cycle_position, cycle_len))
