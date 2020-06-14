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


'''@cache_cls_instance
class Foo:
    def __init__(self, name):
        self.name = name

    def display(self):
        print (self.name)

    def bar(self,bar):
        self.name = bar'''



def limit_instance_number(cls_name = None, *, num = 1):
    '''
    Example 1:
    @limit_instance_number
    def FOO:
       pass

    Example 2:
    @limit_instance_number()
    def FOO:
       pass

    Example 3:
    @limit_instance_number(num = 3)
    def FOO:
       pass

    :param cls_name:
    :param num:
    :return:
    '''
    def wrapper(cls):
        class singleton:
            current_instance_number = 0
            def __init__(self, obj):
                self.obj = obj

            def __call__(self, *args, **kwargs):
                tmpObj = None
                if singleton.current_instance_number < num:
                    tmpObj=self.obj.__new__(cls)
                    singleton.current_instance_number += 1

                return tmpObj
        cls.__new__ = singleton(cls.__new__)
        return cls

    if not cls_name:
        return wrapper
    else:
        return wrapper(cls_name)






@limit_instance_number(num = 2)
class Foo:
    def __init__(self, name):
        self.name = name

    def display(self):
        print (self.name)

    def bar(self,bar):
        self.name = bar


a = Foo('a')
b = Foo('b')
b.bar('B')
a.display()


print (a)
print (b)
