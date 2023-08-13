---
title: Python random number generator
topics: [python]
---

Python uses `random.seed` to set a random seed, but does not appear to offer a random number generator object that can be seeded (ie. there is only a _global_ seed). This may make reproducibility challenging in some circumstances.
