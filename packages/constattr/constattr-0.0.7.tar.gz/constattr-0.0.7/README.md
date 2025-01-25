# constattr

![test](https://github.com/diegojromerolopez/constattr/actions/workflows/test.yml/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/diegojromerolopez/constattr/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/constattr.svg)](https://pypi.python.org/pypi/constattr/)
[![PyPI version constattr](https://badge.fury.io/py/constattr.svg)](https://pypi.python.org/pypi/constattr/)
[![PyPI status](https://img.shields.io/pypi/status/constattr.svg)](https://pypi.python.org/pypi/constattr/)
[![PyPI download month](https://img.shields.io/pypi/dm/constattr.svg)](https://pypi.python.org/pypi/constattr/)
[![Maintainability](https://api.codeclimate.com/v1/badges/5317e9072a41570ae66e/maintainability)](https://codeclimate.com/github/diegojromerolopez/constattr/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5317e9072a41570ae66e/test_coverage)](https://codeclimate.com/github/diegojromerolopez/constattr/test_coverage)

Enforce your class constants in python.

> The only constant in life is change

*Heraclitus*

> Not anymore!

*Didacus I. Granatensis*

## Usage
Decorate your class with `constclassattrs` and when a class attribute that is uppercase
is re-assigned the exception `ConstantAssignmentError` will be raised.

## Example

```python
from constattr.decorators import constclassattrs


@constclassattrs
class Example1:
    MY_CONST1 = '1'
    MY_CONST2 = '2'


# This will raise the ConstAssignmentError exception
Example1.MY_CONST1 = 'new value for the constant'
```

## Limitations
If your class has a metaclass defined, it will work, but in case of conflict
the MRO in the metaclass will choose the [ConstantEnforcerMeta](/constattr/const_enforcer_meta.py)
class first.

## Dependencies
This package has no dependencies.

## License
[MIT](LICENSE) license, but if you need any other contact me.
