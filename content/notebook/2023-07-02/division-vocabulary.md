---
title: Division vocabulary
---

As a [refresher](https://www.hmhco.com/blog/teaching-dividend-divisor-and-quotient-in-division) in `a / b = c`, `a` is the **dividend**, `b` is the **divisor**, and `c` is the **quotient**. In secure integer division in mpyc, the divisor has to be public. Probably not a theoretical limitation? The mpyc [documentation](https://mpyc.readthedocs.io/en/latest/mpyc.html#module-mpyc.runtime) claims to support divison of two secure floats. And while undocumented, division with a secure integer divisor appears to work, but only when the dividend splits evenly.
