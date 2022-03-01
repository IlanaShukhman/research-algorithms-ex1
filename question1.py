from typing import *

def safe_call(f: Callable[[any], any],**kwargs):
    try:
        for x in kwargs:
            if x in f.__annotations__ and f.__annotations__[x] != type(kwargs[x]):
                raise Exception("wrong arguments")
    except Exception:
        print("Wrong arguments!")
    else:
        return f(**kwargs)


def func(x:int, y:float, z):
    return x+y+z

if __name__ == '__main__':
    print(safe_call(func, y=5.0, x=2, z=7))
    print(safe_call(func, x=5, y="abc", z=7))