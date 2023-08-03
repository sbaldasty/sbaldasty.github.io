---
title: Mocking mpyc for fast local testing
---

I am considering making a "mock" mpyc for quickly testing large jobs locally. Tentative goals and design decisions:

1. Define an alternative `mpyc.runtime` object (probably only adding members needed for my particular project, at least for now). A project could be switched between the real `mpc` and the mock one with a single `import` change.

2. `SecInt` factory creates public integers rather than secure ones. Redefine secure number operations on `mpc` to work with regular numbers. In instances where secure numbers override special behavior, these should hopefully just continue to work as intended - at least to the extent that mpyc mirrors their behavior. There could be exceptions, for instance `if_else` could branch on anything truthy.

3. The number of parties could be a settable field on the `mpc`. The program would always run as `pid` 0. The trickiest part is how `input` should work. If the program runs as one party, and there is a hard requirement that the contract of `input` not change, then how can the mock know what to return on behalf of all the other parties?

4. Because of the design of the mock object, parameters sent to `output` should already be public; `output` should therefore just return its input as a future for compatibility.
