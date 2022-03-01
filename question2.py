from typing import Union, List, Tuple, Dict, Set
import copy
from collections import OrderedDict

def sort_rec(x: Union[List, Tuple, Dict, Set]):
    if isinstance(x , Dict):
        new_obj = {}
        for key in sorted(x):
            new_obj[key] = sort_rec(x[key])
        return new_obj

    elif isinstance(x, List) or isinstance(x, Tuple):
        new_obj = [0] * len(x)
        try:
            new_obj = sorted(x)
        except:
            for i in range(len(x)):
                new_obj[i] = str(sort_rec(x[i]))
            return sorted(new_obj)
        else:
            return new_obj

    elif isinstance(x, Set):
        new_obj = [0] * len(x)
        try:
            new_obj = sorted(x)
        except:
            i = 0
            for obj in x:
                new_obj[i] = str(obj)
                i = i + 1
            return sorted(new_obj)
        return new_obj
    else:
        return x


def print_sorted(x: Union[List, Tuple, Dict, Set]):
    if x is None:
        return
    if isinstance(x, Dict):
        new_obj = {}
        for key in x:
            new_obj[key] = sort_rec(x[key])
        for key in sorted(new_obj):
            print("{", key, ":", new_obj[key], end= "}, ")

    elif isinstance(x, List):
        new_obj = [0]*len(x)
        for i in range(len(x)):
            new_obj[i] = str(sort_rec(x[i]))
        new_obj_sorted = sorted(new_obj)
        for i in range(len(new_obj_sorted)):
            print(new_obj_sorted[i], end= ", ")

    elif isinstance(x, Tuple):
        new_obj = [0] * len(x)
        for i in range(len(x)):
            new_obj[i] = str(sort_rec(x[i]))
        new_obj_sorted = sorted(new_obj)
        for i in range(len(new_obj_sorted)):
            print(new_obj_sorted[i], end=", ")

    elif isinstance(x, Set):
        print("{",end=" ")
        new_obj = [0] * len(x)
        i = 0
        for obj in x:
            new_obj[i] = str(obj)
            i = i+1
        new_obj_sorted = sorted(new_obj)
        for i in range(len(new_obj_sorted)):
            print(new_obj_sorted[i], end=", ")
        print("}")
    print()

if __name__ == '__main__':

    #simple tests - one layer
    print_sorted([1, [1,5,3], 2])
    print_sorted({'d':5,'c':3})

    print_sorted((1,4,2))
    my_set = {4,5,2}
    print_sorted(my_set)
    print_sorted(None)

    #two layers
    print_sorted({'a':4, 'c':7, 'b':[1,5,3,2]})
    print_sorted([1, [1, 4,2], 8, 3])
    print_sorted((1, [1, 4, 2], 8, 3))


    #three layers
    print_sorted({'a': 4, 'c': 7, 'b': [1, (2,1), 3, 2]})
    print_sorted([1, [1, 4, 2, 5, 2, {'g': 2, 'd': [15, 17, 12, 2], 'f': 13}], (5, 8 , 6, 8, 3), 3])