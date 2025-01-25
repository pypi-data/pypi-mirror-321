from typing import List
from struct import unpack
import ctypes
from z3 import LShR

def ror8(x, n):
    n &= 7
    if isinstance(x, int):
        return ((x >> n) | (x << (8 - n))) & 0xFF
    else:
        return (LShR(x, n) | (x << (8 - n))) & 0xFF
    
def rol8(x, n):
    n &= 7
    if isinstance(x, int):
        return ((x << n) | (x >> (8 - n))) & 0xFF
    else:
        return (LShR(x, 8 - n) | (x << n)) & 0xFF

def rol16(x, n):
    n &= 15
    if isinstance(x, int):
        return ((x << n) | (x >> (16 - n))) & 0xFFFF
    else:
        return (LShR(x, 16 - n) | (x << n)) & 0xFFFF

def ror16(x, n):
    n &= 15
    if isinstance(x, int):
        return ((x >> n) | (x << (16 - n))) & 0xFFFF
    else:
        return (LShR(x, n) | (x << (16 - n))) & 0xFFFF

def rol32(x, n):
    n &= 31
    if isinstance(x, int):
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF
    else:
        return ((x << n) | LShR(x, 32 - n)) & 0xFFFFFFFF

def ror32(x, n):
    n &= 31
    if isinstance(x, int):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
    else:
        return ((x << (32 - n)) | LShR(x, n)) & 0xFFFFFFFF

def rol64(x, n):
    n &= 63
    if isinstance(x, int):
        return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF
    else:
        return ((x << n) | LShR(x, 64 - n)) & 0xFFFFFFFFFFFFFFFF

def ror64(x, n):
    n &= 63
    if isinstance(x, int):
        return ((x >> n) | (x << (64 - n))) & 0xFFFFFFFFFFFFFFFF
    else:
        return ((x << (64 - n)) | LShR(x, n)) & 0xFFFFFFFFFFFFFFFF

def byte2dword(x: List[int], endian='little'):
    if len(x) % 4 != 0:
        if type(x) == bytes:
            x += b'\x00' * (4 - (len(x) % 4))
        else:
            x += [0] * (4 - (len(x) % 4))
    packing = '>I' if endian == 'big' else '<I' if endian == 'little' else None
    if not packing: raise "Endian Error"
    return [v[0] for v in (unpack(packing, bytes(x[i:i+4])) for i in range(0, len(x), 4))]

def dword2byte(x: List[int]):
    result = []
    if type(x) == int:
        for j in range(4):
            result.append((x >> j*8) & 0xff)
        return bytes(result)
    for i in range(len(x)):
        for j in range(4):
            result.append((x[i] >> j*8) & 0xff)
    return bytes(result)

def byte2word(x: List[int], endian='little'):
    if len(x) % 2 != 0:
        if type(x) == bytes:
            x += b'\x00' * (2 - (len(x) % 2))
        else:
            x += [0] * (2 - (len(x) % 2))
    packing = '>H' if endian == 'big' else '<H' if endian == 'little' else None
    if not packing: raise "Endian Error"
    return [v[0] for v in (unpack('<H', bytes(x[i:i+2])) for i in range(0, len(x), 2))]

def word2byte(x: List[int]):
    result = []
    if type(x) == int:
        for j in range(2):
            result.append((x >> j*8) & 0xff)
        return bytes(result)
    for i in range(len(x)):
        for j in range(2):
            result.append((x[i] >> j*8) & 0xff)
    return bytes(result)


def byte2qword(x: List[int], endian='little'):
    if len(x) % 8 != 0:
        if type(x) == bytes:
            x += b'\x00' * (8 - (len(x) % 8))
        else:
            x += [0] * (8 - (len(x) % 8))

    packing = '>Q' if endian == 'big' else '<Q' if endian == 'little' else None
    if not packing: raise "Endian Error"
    return [v[0] for v in (unpack(packing, bytes(x[i:i+8])) for i in range(0, len(x), 8))]

def qword2byte(x: List[int]):
    result = []
    if type(x) == int:
        for j in range(8):
            result.append((x >> j*8) & 0xff)
        return bytes(result)
    for i in range(len(x)):
        for j in range(8):
            result.append((x[i] >> j*8) & 0xff)
    return result

def u82byte(x: List[int]) -> bytes:
    return bytes([i & 0xff for i in x])


# pack to tuple [(),(),(),...], each tuple len is `crows`
def pack_dword(x: List[int], crows: int = 2, padding: bool = False):
    if len(x) % crows != 0:
        if not padding:
            raise Exception('pack_dword expected length is the crows\' integer multiples. Or enables padding.')
        x += [0] * (crows - (len(x) % crows))
    for i in range(0, len(x), crows):
        yield tuple(x[i:i+crows])

# flat [(), (), ()]
def unpack_dword(x: List[tuple]):
    result = []
    for i in x:
        result += list(i)
    return result

def bswap32(x: List[int]):
    y = dword2byte(x)
    r = b''
    for i in range(0, len(y), 4):
        r += y[i:i+4][::-1]
    return byte2dword(r)
        

import struct
import sys

# long_to_bytes
def l2b(n, blocksize=0):
    """Convert a positive integer to a byte string using big endian encoding.

    If :data:`blocksize` is absent or zero, the byte string will
    be of minimal length.

    Otherwise, the length of the byte string is guaranteed to be a multiple
    of :data:`blocksize`. If necessary, zeroes (``\\x00``) are added at the left.

    .. note::
        In Python 3, if you are sure that :data:`n` can fit into
        :data:`blocksize` bytes, you can simply use the native method instead::

            >>> n.to_bytes(blocksize, 'big')

        For instance::

            >>> n = 80
            >>> n.to_bytes(2, 'big')
            b'\\x00P'

        However, and unlike this ``long_to_bytes()`` function,
        an ``OverflowError`` exception is raised if :data:`n` does not fit.
    """

    if n < 0 or blocksize < 0:
        raise ValueError("Values must be non-negative")

    result = []
    pack = struct.pack

    # Fill the first block independently from the value of n
    bsr = blocksize
    while bsr >= 8:
        result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
        n = n >> 64
        bsr -= 8

    while bsr >= 4:
        result.insert(0, pack('>I', n & 0xFFFFFFFF))
        n = n >> 32
        bsr -= 4

    while bsr > 0:
        result.insert(0, pack('>B', n & 0xFF))
        n = n >> 8
        bsr -= 1

    if n == 0:
        if len(result) == 0:
            bresult = b'\x00'
        else:
            bresult = b''.join(result)
    else:
        # The encoded number exceeds the block size
        while n > 0:
            result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
            n = n >> 64
        result[0] = result[0].lstrip(b'\x00')
        bresult = b''.join(result)
        # bresult has minimum length here
        if blocksize > 0:
            target_len = ((len(bresult) - 1) // blocksize + 1) * blocksize
            bresult = b'\x00' * (target_len - len(bresult)) + bresult

    return bresult


# bytes_to_long
def b2l(s):
    """Convert a byte string to a long integer (big endian).

    In Python 3.2+, use the native method instead::

        >>> int.from_bytes(s, 'big')

    For instance::

        >>> int.from_bytes(b'\x00P', 'big')
        80

    This is (essentially) the inverse of :func:`long_to_bytes`.
    """
    acc = 0

    unpack = struct.unpack

    # Up to Python 2.7.4, struct.unpack can't work with bytearrays nor
    # memoryviews
    if sys.version_info[0:3] < (2, 7, 4):
        if isinstance(s, bytearray):
            s = bytes(s)
        elif isinstance(s, memoryview):
            s = s.tobytes()

    length = len(s)
    if length % 4:
        extra = (4 - length % 4)
        s = b'\x00' * extra + s
        length = length + extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack('>I', s[i:i+4])[0]
    return acc

# 8bytes->1double (with padding)
def byte2double(src: bytes) -> List[float]:
    qws = byte2qword(src)
    result = []
    for i in qws:
        full_value = ctypes.c_uint64(i)
        double_value = ctypes.cast(ctypes.pointer(full_value), ctypes.POINTER(ctypes.c_double)).contents.value
        result.append(double_value)
    return result

# 4bytes->1double (with padding)
def byte2float(src: bytes) -> List[float]:
    qws = byte2dword(src)
    result = []
    for i in qws:
        full_value = ctypes.c_uint32(i)
        float_value = ctypes.cast(ctypes.pointer(full_value), ctypes.POINTER(ctypes.c_float)).contents.value
        result.append(float_value)
    return result