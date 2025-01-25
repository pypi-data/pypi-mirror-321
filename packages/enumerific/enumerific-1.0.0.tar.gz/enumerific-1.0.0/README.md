# Enumerific Enums

The `enumerific` library provides several useful extensions to the Python built-in `enums` library.

### Requirements

The Enumerific library has been tested with Python 3.9, 3.10, 3.11, 3.12 and 3.13 but may work with some earlier versions such as 3.8, but has not been tested against this version or any earlier. The library is not compatible with Python 2.* or earlier.

### Installation

The Enumerific library is available from PyPi, so may be added to a project's dependencies via its `requirements.txt` file or similar by referencing the Enumerific library's name, `enumerific`, or the library may be installed directly into your local runtime environment using `pip install` by entering the following command, and following any prompts:

	$ pip install enumerific

### Usage

To use the Enumerific library, simply import the library and use it like you would the built-in `enum` library as a drop-in replacement:

```
import enumerific

class MyEnum(enumerific.Enum):
  Option1 = "ABC"
  Option2 = "DEF"

val = MyEnum.Option1
```

You can also import the `Enum` class directly from the `enumerific` library and use it directly:

```
from enumerific import Enum

class MyEnum(Enum):
  Option1 = "ABC"
  ...
```

The Enumerific library's own `Enum` class is a subclass of the built-in `enum.Enum` class, so all of the built-in functionality of `enum.Enum` is available, as well as several additional class methods:

* `reconcile(value: object, default: Enum = None, raises: bool = False) -> Enum` – The `reconcile` method allows for an enumeration's value or an enumeration option's name to be reconciled against a matching enumeration option. If the provided value can be matched against one of the enumeration's available options, that option will be returned, otherwise there are two possible behaviours: if the `raises` keyword argument has been set to or left as `False` (its default), the value assigned to the `default` keyword argument will be returned, which may be `None` if no default value has been specified; if the `raises` argument has been set to `True` an `EnumValueError` exception will be raised as an alert that the provided value could not be matched. One can also provide an enumeration option as the input value to the `reconcile` method, and these will be validated and returned as-is.
* `validate(value: object) -> bool` – The `validate` method takes the same range of input values as the `reconcile` method, and returns `True` when the provided value can be reconciled against an enumeration option, or `False` otherwise.
* `options() -> list[Enum]` – The `options` method provides easy access to the list of the enumeration's available options.

The benefits of being able to validate and reconcile various input values against an enumeration, include allowing for a controlled vocabulary of options to be checked against, and the ability to convert enumeration values into their corresponding enumeration option. This can be especially useful when working with input data where you need to convert those values to their corresponding enumeration options, and to be able to do so without maintaining boilerplate code to perform the matching and assignment.

Some examples of use include the following code samples, where each make use of the example `MyEnum` class, defined as follows:

```
from enumerific import Enum

class MyEnum(Enum):
  Option1 = "ABC"
  Option2 = "DEF"
```

#### Example 1: Reconciling a Value

```
# Given a string value in this case
value = "ABC"

# Reconcile it to the associated enumeration option
value = MyEnum.reconcile(value)

assert value == MyEnum.Option1  # asserts successfully
assert value is MyEnum.Option1  # asserts successfully as enums are singletons
```

#### Example 2: Reconciling an Enumeration Option Name

```
# Given a string value in this case
value = "Option1"

# Reconcile it to the associated enumeration option
value = MyEnum.reconcile(value)

assert value == MyEnum.Option1  # asserts successfully
assert value is MyEnum.Option1  # asserts successfully as enums are singletons
```

#### Example 3: Validating a Value

```
# The value can be an enumeration option's name, its value, or the enumeration option
value = "Option1"
value = "ABC"
value = MyEnum.Option1

if MyEnum.validate(value) is True:
    # do something if the value could be validated
else:
    # do something else if the value could not be validated
```

#### Example 4: Iterating Over Enumeration Options

```
for option in MyEnum.options():
    # do something with each option
    print(option.name, option.value)
```

### Unit Tests

The Enumerific library includes a suite of comprehensive unit tests which ensure that the library functionality operates as expected. The unit tests were developed with and are run via `pytest`.

To ensure that the unit tests are run within a predictable runtime environment where all of the necessary dependencies are available, a [Docker](https://www.docker.com) image is created within which the tests are run. To run the unit tests, ensure Docker and Docker Compose is [installed](https://docs.docker.com/engine/install/), and perform the following commands, which will build the Docker image via `docker compose build` and then run the tests via `docker compose run` – the output of running the tests will be displayed:

```
$ docker compose build
$ docker compose run tests
```

To run the unit tests with optional command line arguments being passed to `pytest`, append the relevant arguments to the `docker compose run tests` command, as follows, for example passing `-vv` to enable verbose output:

```
$ docker compose run tests -vv
```

See the documentation for [PyTest](https://docs.pytest.org/en/latest/) regarding available optional command line arguments.

### Copyright & License Information

Copyright © 2024–2025 Daniel Sissman; Licensed under the MIT License.