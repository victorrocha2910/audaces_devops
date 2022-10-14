import ctypes
import os

here = os.path.dirname(os.path.abspath(__file__))


def sum_values(a, b):
    path = f"{here}/../libs/MathLibrary_x86.dll"
    dll = ctypes.WinDLL(path)

    ctype_a = ctypes.c_int(a)
    ctype_b = ctypes.c_int(b)
    return dll.sum(ctype_a, ctype_b)

