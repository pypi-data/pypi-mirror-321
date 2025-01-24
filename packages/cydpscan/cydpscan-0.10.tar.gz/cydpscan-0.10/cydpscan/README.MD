# Very fast dbscan 2d / 3d for Python - written in Cython/C++

Python wrapper for https://github.com/Eleobert/dbscan

```pip install cydpscan```

Cython and a C++ 20 compiler must be installed! The module will be compiled the first time you import it!

```py
from cydpscan import calculate_dbscan_2d, calculate_dbscan_3d
import random
from pprint import pprint

mylist = []
for q in range(1000000):
    mylist.append((random.randint(0, 10000), random.randint(0, 10000)))

result = calculate_dbscan_2d(mylist, eps=0.1, min_pts=3)
pprint(result)

mylist2 = []
for q in range(1000000):
    mylist2.append(
        (random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
    )

result2 = calculate_dbscan_3d(mylist2, eps=0.1, min_pts=3)
pprint(result2)

```