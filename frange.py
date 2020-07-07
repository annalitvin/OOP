

def frange(start, stop=None, step=1.0):

    print("--------------------------")
    print(f'start={start}, stop={stop}, step={step}')

    if stop is None:
        stop = start
        start = 0

    if (start < stop and step < 0) or (start > stop and step > 0):
        raise ValueError("Start less than stop and step less than 0 "
                         "or Start more than stop and step more than 0")

    if step == 0:
        raise ValueError("Step is not equal 0")

    current_item = float(start)
    count = 0

    if start > stop and step < 0:
        while current_item > stop:
            count += 1
            yield current_item
            # разрешаем неточность при сложении чисел с плавающей точкой путем пошагового вычисления
            # (start + count * step), при этом не накапливая суммы для каждого шага
            current_item = float(start + count * step)
    else:
        while current_item < stop:
            count += 1
            yield current_item
            current_item = float(start + count * step)


if __name__ == "__main__":

    for i in frange(7):
        print(i)

    for i in frange(2, 8, 2.5):
        print(i)

    for i in frange(5, 2, -4.5):
        print(i)

    for i in frange(1, 3.5):
        print(i)

    for i in frange(-1, -5, -1.2):
        print(i)
