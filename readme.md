## find common sequence

[![Run Tests](https://github.com/mfa/longest-common-sequence/actions/workflows/tests.yaml/badge.svg)](https://github.com/mfa/longest-common-sequence/actions/workflows/tests.yaml)

deployed: https://lcs.madflex.de/


### problem definition

We have a set of strings and want to find common strings of them,
but we have a second set that should not match the found common strings.
The result is a string that is found in the first set, but not in any of the strings in the second set.

#### Example

set1: (positive set)
```
this dummy example.
example this
this example
```

common strings: ``this``, ``example``

set2: (negative set)
```
this foo
another not relevant string
```

resulting strings (positive for set1, negative for set2): ``example``


### local setup

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```


### tests

```
pip install -r requirements.txt
pip install pytest pyyaml
python -m pytest
```
