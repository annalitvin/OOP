
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def is_point_inside_circle(self, point):

        if ((point.x - self.x) ** 2) + ((point.y - self.y) ** 2) < self.radius**2:
            return True
        else:
            return False


if __name__ == "__main__":

    circle = Circle(4, 5, 2)
    point = Point(5, 5)

    is_point_inside_circle = circle.is_point_inside_circle(point)
    print(is_point_inside_circle)
