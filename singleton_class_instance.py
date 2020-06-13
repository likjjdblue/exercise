#!/usr/bin/env python3

def cache_cls_instance(cls):
    class singleton:
        def __init__(self, obj):
            self.obj = obj
            self.instance  = None

        def __call__(self, *args, **kwargs):
            if not self.instance:
                print ('NEW....')
                self.instance = self.obj(*args, **kwargs)
            else:
                print ('EXIST....')
            return self.instance

    cls.__new__ = singleton(cls.__new__)
    return cls


@cache_cls_instance
class Foo:
    def foo(self):
        print ('Foo')



a = Foo()
b = Foo()
print (a is b)
a.foo()