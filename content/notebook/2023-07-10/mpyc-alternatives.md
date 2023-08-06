---
title: Alternatives to mpyc
topics: []
---

Alternatively there is a collection of Rust MPC libraries called [Swanky](https://github.com/GaloisInc/swanky/) and an older unmaintained Java library called [SCAPI](https://github.com/ddunwoody/scapi) to consider. Most likely an MPC problem rather than a mpyc problem, I'm using this library like a black box and some operations under the hood just may not compose. If possible it would be good to have a library that communicated effectively through its API what operations could not succeed but not pursuing this now.
