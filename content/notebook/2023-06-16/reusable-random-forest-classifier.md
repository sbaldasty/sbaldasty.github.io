---
title: Random forest classifier
topics: [machine-learning, python]
---

I'm in search of a random forest classifier implementation in python that

- Allows for custom logic to choose features and splits during training
- Is installable via pip
- Supports persisting models, ideally in a standard format
- Has a permissive open source license

Here's what I've found so far and how they stack up:

- [scikit-learn](https://scikit-learn.org/stable/modules/classes.html) is the defacto standard. Even though it comes close, it does not allow for the custom feature and split selection logic that I need.
- [random-forest-mc](https://pypi.org/project/random-forest-mc/) is for multiple feature selection, which is not the use case I am looking for. I didn't go on to research whether it supports custom logic.
- [mlfromscratch](https://github.com/patrickloeber/MLfromscratch) has issues installing with pip, and doesn't seem to support the custom logic I need without modification.
- [RandomForests](https://github.com/mdh266/RandomForests/) is someone's personal project that may not have an open source license. The logic is again not something I can just plug in.
