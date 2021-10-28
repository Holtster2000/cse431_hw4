import timeit
import random
from typing import (
    Any,
    List,
    Optional
)


def random_int_list(
        n: int,
        min_val: int = 0,
        max_val: int = 1000,
        seed: Optional[int] = None) -> List[int]:
    if seed:
        random.seed(seed)
    return [random.randint(min_val, max_val) for _ in range(n)]


# Used in merge_sort()
def merge(s1: List[Any], s2: List[Any], s: List[Any]) -> None:
    i = j = 0

    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


# implementation based on CSE 331 lectures
def merge_sort(s: List[Any]) -> None:
    n = len(s)
    if n < 2:
        return

    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)


# Used in insertion_sort()
def exchange(s: List[Any], i: int, j: int) -> None:
    s[i], s[j] = s[j], s[i]


# implementation based on CSE 331 lectures
def insertion_sort(s: List[Any]) -> None:
    n = len(s)
    for i in range(1, n):
        j = i
        while (j > 0) and (s[j] < s[j-1]):
            exchange(s, j, j-1)
            j -= 1


if __name__ == '__main__':
    rand_seed = random.randint(0, 100000)
    num_iterations = 100
    print("N,merge,insertion")
    for size in [5, 10, 25, 50, 100, 500, 1000]:
        merge_time = 0
        for t in range(num_iterations):
            merge_time += timeit.timeit(
                f"merge_sort(s)",
                number=1,
                setup=f'''
from __main__ import merge_sort, random_int_list
s = random_int_list(n={size}, seed={rand_seed})
                '''
            )

        insertion_time = 0
        for t in range(num_iterations):
            insertion_time += timeit.timeit(
                f"insertion_sort(s)",
                number=1,
                setup=f'''
from __main__ import insertion_sort, random_int_list
s = random_int_list(n={size}, seed={rand_seed})
                '''
            )
        print(",".join([str(size), str(merge_time/num_iterations), str(insertion_time/num_iterations)]))
