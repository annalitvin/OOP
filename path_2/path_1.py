from functools import wraps, lru_cache

#Python3.2+
# @lru_cache(maxsize=32)
# def get_logger():
#     return [1, 2, 3] * 2


#Python2

def once(f):

    memo = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args not in memo:
            result = f(*args, **kwargs)
            memo[args] = result
            return result

    return wrapper


@once
def get_logger():
    return [1, 2, 3] * 2


if __name__ == "__main__":
    logger = get_logger()

    assert id(get_logger()) == id(get_logger()), "Not equal"
    print('SUCCESS!')
