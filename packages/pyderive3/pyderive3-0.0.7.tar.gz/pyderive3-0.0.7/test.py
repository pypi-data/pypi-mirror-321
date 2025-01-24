
# a = 'ayylmao'
# t = f'{a if a is not None else ""}'
# print(t)

from typing import List, Literal, Optional, Union

from pyderive import DataClassLike
from pyderive.dataclasses import dataclass, fields
from pyderive.extensions.serde import Serde
from pyderive.extensions.validate import BaseModel
from pyderive.extensions.validate.validators import type_validator

# from pydantic import BaseModel

TrustedHeader = Literal[
    'True-Connecting-IP',
    'CF-Connecting-IP',
    'CF-Connecting-Ipv4',
    'CF-Connecting-Ipv6',
    'X-Real-IP',
    'X-Client-IP',
    'X-Forwarded-For',
    'Forwarded',
]

Test2 = Union[Literal['A'], Literal['B']]

@dataclass
class A:
    pass

print(isinstance(A, DataClassLike))

print(fields(A))

class Test(BaseModel, Serde, hide_repr = 'null'):
    a: TrustedHeader
    b: Test2

t = Test.parse_obj({'a': 'X-Real-IP', 'b': 'B', 'c': 1}, allow_unknown=True)
print(t)

r = t.to_xml()
print(r)
