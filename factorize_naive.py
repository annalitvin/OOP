from functools import partial
from multiprocessing.pool import ThreadPool

from speed_test import timer


def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


def factorize_naive_run(n, drs={}):
    drs[n] = factorize_naive(n)
    return drs


### Single-threaded version
# result = {}
# input_data = [n for n in range(1000000)]
#
# # DATA_SIZE = len(data)
# #
# with timer('Elapsed: {}s'):
#     for n in input_data:
#         result[n] = factorize_naive(n)

### Multiprocess version

# workers = None
# input_data = [n for n in range(1000000)]
#
# with timer('Elapsed: {}s'):
#     with multiprocessing.Pool(workers) as pool:
#         pool.map(partial(factorize_naive_run), input_data)


### Thread version
# workers = None
# input_data = [n for n in range(1000000)]
#
# with timer('Elapsed: {}s'):
#     with ThreadPool(workers) as pool:
#         pool.map(partial(factorize_naive_run), input_data)
