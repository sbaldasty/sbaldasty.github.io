---
title: Inline block elements
topics: []
---

I noticed the margins of my paragraphs extended out beyond their enclosing div, instead of the div enlarging to contain them. Changing the `display` property of the enclosing div to `inline-block` [resolved the issue](https://stackoverflow.com/questions/45610135/code-element-with-padding-extends-outside-its-container) (I'm surprised I never knew this behavior of `block`).

