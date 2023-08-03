---
title: Floating point division in mpyc
---

The most straightforward way around not being able to divide by a secure integer was to use floating point division, since the documentation explicitly claimed support for secure divisors. However the documentation also warned that floating point arithmetic operations could be prohibitively slow, and this proved to be the case.

Also after switching the division to `SecFlt`, I had to switch everything else as well because there doesn't seem to be a way to convert between secure floats and secure integers, or even integers of different sizes for that matter. Even the results of comparisons were secure floats instead of bits.
