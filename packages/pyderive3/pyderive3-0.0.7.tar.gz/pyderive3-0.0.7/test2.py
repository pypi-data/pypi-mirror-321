import timeit

import dataclasses
import pyderive
import pydantic
from pyderive.extensions import validate

def test_std_dataclass():

    @dataclasses.dataclass
    class Foo:
        a: int
        b: str
    foo = Foo(1, 'a')

def test_new_dataclass():

    @pyderive.dataclass
    class Foo:
        a: int
        b: str
    foo = Foo(1, 'a')

def test_dantic_model():

    class Foo(pydantic.BaseModel):
        a: int
        b: str
    foo = Foo(a=1, b='a')

def test_new_model():

    class Foo(validate.BaseModel):
        a: int
        b: str
    foo = Foo(a=1, b='a')

# n = 10000
# std = timeit.timeit(test_std_dataclass, number=n)
# print('std', std)
# new = timeit.timeit(test_new_dataclass, number=n)
# print('new', new)

n = 10000
std = timeit.timeit(test_dantic_model, number=n)
print('dantic', std)
new = timeit.timeit(test_new_model, number=n)
print('new', new)

