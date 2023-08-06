---
title: Python dataclass equality
topics: []
---

Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) create `__eq__` by default, which can cause infinitely recursive equality checks for data structures like graphs where instances of the dataclass reference each other circularly; using `eq=False` in the constructor prevents the automatic creation of `__eq__`.
