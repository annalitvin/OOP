
def once(f):
    def main(*args, **kwargs):
        result = f(*args, **kwargs)

        def wrapper():
            return result

        return wrapper
    return main


@once
def get_logger():
    return [1, 2, 3] * 2


if __name__ == "__main__":
    assert id(get_logger()) == id(get_logger()), "Not equal"
    print('SUCCESS!')
