---
title: One hot encoding
topics: [machine-learning, python]
---

Here is a way to one hot encode every column in a pandas dataframe, inspired by a discussion on [Stack Overflow](https://stackoverflow.com/questions/37292872/how-can-i-one-hot-encode-in-python). The one hot encoding is in a new dataframe.

```
pd.concat([pd.get_dummies(df[[column]]) for column in df], axis=1)
```

