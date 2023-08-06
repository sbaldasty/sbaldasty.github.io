---
title: Composing maximum and division in mpyc
topics: []
---

Integer division `c = a // mpc.max(x, y)` ran into problems. It worked fine when the federation contained just one party. What I appeared to see initially was success when `a` was evenly divisible and wildly outlandish `c` (including negative numbers) when it was not. That might have been an overflow issue. Subsequently what I see is

```
secint = mpc.SecInt(64)
mpc.run(mpc.start())
a = secint(12)
x = secint(1)
y = secint(2)
b = mpc.max(x, y)
q = a // b
e = mpc.output(q)
mpc.run(mpc.shutdown())
print(e)
```

Fails with this error:

```
IndexError: list index out of range
Traceback (enclosing MPyC coroutine call):
  File "/home/sbaldasty/.venv/lib/python3.11/site-packages/mpyc/runtime.py", line 3206, in random_bits
    r2s = await self.output(r2s, threshold=2*t)
```

Yet this variation using integer multiplication succeeds:

```
secint = mpc.SecInt(64)
mpc.run(mpc.start())
a = secint(12)
x = secint(1)
y = secint(2)
b = mpc.max(x, y)
q = a * b
e = mpc.output(q)
mpc.run(mpc.shutdown())
print(e)
```

As does this variation that does not use the `max` function (even though the type of `b` was still a secure integer when it was assigned via `max`).

```
secint = mpc.SecInt(64)
mpc.run(mpc.start())
a = secint(12)
b = secint(2)
q = a // b
e = mpc.output(q)
mpc.run(mpc.shutdown())
print(e)
```
