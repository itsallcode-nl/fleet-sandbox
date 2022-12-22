import struct

@struct.dataclass
class Something:
    a: str

# this will cause an "unexpected argument" warning
s = Something(a='asd')