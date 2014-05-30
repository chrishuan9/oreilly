__author__ = 'chris'
"""Initial implementation of complex numbers."""


class Cplx:
    pass


def cplx(real, imag):
    c = Cplx()
    c.real = real
    c.imag = imag
    return c


def cadd(c1, c2):
    c = Cplx()
    c.real = c1.real + c2.real
    c.imag = c1.imag + c2.imag
    return c


def cstr(c):
    return "%s+%sj" % (c.real, c.imag)


if __name__ == "__main__":
    zero = cplx(0.0, 0.0)
    one = cplx(1.0, 0.0)
    i = cplx(0.0, 1.0)
    result = cadd(zero, cadd(one, i))
    print(cstr(result))