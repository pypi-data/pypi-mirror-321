# Pollution Checker

A Python library for detecting class pollution vulnerabilities in Python libraries. This tool helps identify different types of class pollution vulnerabilities and scope.

## Installation

```bash
pip install pollution_checker
```

## Usage

```python
from pollution_checker import PollutionChecker

# Example tested function
def nested_set_attr(obj, attr_dict):
    # Ignore the vulnerable code
    ...
    pass

# Create a destination object
obj = object()
# Create a checker instance
checker = PollutionChecker(dst_obj=obj,func=nested_set_attr)
# Run the check: the arguments should remain same as the ones in the tested function
result = checker.func(obj, "PAYLOADS")
```

## Features

The library checks for various types of class pollution:
1. Attr/Item Get, Attr/Item Set
2. Attr/Item Get, Attribute Set Only
3. (TODO) Attr/Item Get, Item Set Only
4. Attribute Get Only, Attr/Item Set
5. Attribute Set/Get Only

## License

[MIT](https://choosealicense.com/licenses/mit/)
