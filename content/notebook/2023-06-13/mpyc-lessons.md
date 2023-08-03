---
title: Lessons learned about mpyc
---

`mpyc.argmax` returns both the index of the highest argument (in position 0) and the value of the highest argument (in position 1).

Logical operators return 0 or 1 rather than `True` or `False`.

You can get bitwise operators with something like `mpc.and_(x >= 0, x < 10)`.
