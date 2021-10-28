import random
import timeit
from q1 import merge, insertion_sort, random_int_list
from typing import (
    Any,
    List,
)


def tim_sort(k: int, s: List[Any]) -> None:
    n = len(s)
    if n <= k:
        insertion_sort(s)
        return

    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]

    tim_sort(k=k, s=s1)
    tim_sort(k=k, s=s2)

    merge(s1, s2, s)


if __name__ == '__main__':
    rand_seed = random.randint(0, 100000)
    num_iterations = 1000

    print("N,k,runtime")
    for k in range(5, 51, 5):
        for size in range(10, 101, 10):
            tim_time = 0
            for t in range(num_iterations):
                tim_time += timeit.timeit(
                    f"tim_sort(k={k}, s=s)",
                    number=1,
                    setup=f'''
from __main__ import tim_sort, random_int_list
s = random_int_list(n={size}, seed={rand_seed})
                        '''
                )
            print(",".join([str(size), str(k), str(tim_time / num_iterations)]))