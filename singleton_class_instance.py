#!/usr/bin/env python3

def cache_cls_instance(cls):
    class singleton:
        def __init__(self, obj):
            self.obj = obj
            self.instance  = None

        def __call__(self, *args, **kwargs):
            if not self.instance:
                print ('NEW....')
                self.instance = self.obj(cls)
            else:
                print ('EXIST....')
            return self.instance

    cls.__new__ = singleton(cls.__new__)
    return cls


@cache_cls_instance
class Foo:
    def __init__(self, name):
        self.name = name

    def display(self):
        print (self.name)

    def bar(self,bar):
        self.name = bar


a = Foo(name = 'a')
b = Foo(name = 'b')
b.bar('c')
b.display()
print (a is b)

