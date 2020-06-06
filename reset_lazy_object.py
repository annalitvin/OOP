import time


class timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start) * 1000
        print(self.message.format(elapsed_time))


class lazy_object:
    '''
    Class for deferred instantiation of objects.  Init is called
    only when the first attribute is either get or set.
    '''

    def __init__(self, callable, *args, **kw):
        '''
        callable -- Class of objeсt to be instantiated or functionnn to be called
        *args -- arguments to be used when instantiating object
        **kw  -- keywords to be used when instantiating object
        '''
        self.__dict__['callable'] = callable
        self.__dict__['args'] = args
        self.__dict__['kw'] = kw
        self.__dict__['obj'] = None

    def init_obj(self):
        '''
        Instantiate object if not already done
        '''

        if self.obj is None:
            self.__dict__['obj'] = self.callable(*self.args, **self.kw)

    def __getattr__(self, name):
        self.init_obj()
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        if name == 'reset' and value == 1:
            self.__dict__['obj'] = None
        else:
            self.init_obj()
            setattr(self.obj, name, value)

    def __len__(self):
        self.init_obj()
        return len(self.obj)

    def __getitem__(self, idx):
        self.init_obj()
        return self.obj[idx]


class A:

    def __init__(self, num_elem):
        self.attr1 = list(range(num_elem))


a = lazy_object(A, num_elem=10 ** 8)

with timer('Elapsed: {}ms'):
    type(a.attr1)

with timer('Elapsed: {}ms'):
    type(a.attr1)

a.reset = 1

with timer('Elapsed: {}ms'):
    type(a.attr1)

with timer('Elapsed: {}ms'):
    type(a.attr1)
