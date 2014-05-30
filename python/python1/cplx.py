__author__ = 'chris'
"""Initial implementation of complex numbers."""


class Cplx:
    pass


def cinit(c, real, imag):
    c.real = real
    c.imag = imag


def cadd(c1, c2):
    c = Cplx()
    c.real = c1.real + c2.real
    c.imag = c1.imag + c2.imag
    return c


def cstr(c):
    return "%s+%sj" % (c.real, c.imag)


if __name__ == "__main__":
    zero = Cplx()
    cinit(zero, 0.0, 0.0)
    one = Cplx()
    cinit(one, 1.0, 0.0)
    i = Cplx()
    cinit(i, 0.0, 1.0)
    result = cadd(zero, cadd(one, i))
    print(cstr(result))