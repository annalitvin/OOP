class Descriptor:
    def __init__(self, name=None, default=None):
        self.name = name
        self.default = default

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, objtype):
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = self.default
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del self.__dict__[self.name]


class RangeDescriptor(Descriptor):
    def __init__(self, name, min_value, max_value):
        super().__init__(name)
        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, instance, value):
        if value not in range(self.min_value, self.max_value):
            raise ValueError(f"Invalid value! Value must be between {self.min_value} and {self.max_value}")
        super().__set__(instance, value)


class Typed(Descriptor):
    type_ = object
    extra_methods = []

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('Expected %s' % self.type_)
        super().__set__(instance, value)


class Numeric(Typed):
    extra_methods = ['gt', 'gte']

    def gt(instance_value, value):
        return instance_value > value

    def gte(instance_value, value):
        return instance_value >= value


class Integer(Numeric):
    type_ = int


class RangeInteger(Integer, RangeDescriptor):
    pass


class ModelMeta(type):

    def __new__(metacls, clsname, bases=None, clsdict=None):
        cls = super().__new__(metacls, clsname, bases, clsdict)
        extra_attrs = []
        for attr_name, attr_value in cls.__dict__.items():
            if isinstance(attr_value, Typed):
                extra_attrs += [
                    (attr_name, extra_method, getattr(attr_value.__class__, extra_method))
                    for extra_method in attr_value.extra_methods
                ]

        for attr, extra, func in extra_attrs:
            setattr(
                cls,
                f'{attr}__{extra}',
                lambda self, value, attr=attr, func=func: func(getattr(self, attr), value)
            )

        return cls


class Employee(metaclass=ModelMeta):
    kpi_score = RangeInteger(name='kpi_score', min_value=0, max_value=100)


if __name__ == "__main__":

    emp = Employee()
    print(dir(emp))

    emp.kpi_score = 1
    emp.kpi_score = 101
    print(emp.kpi_score__gte(8))
