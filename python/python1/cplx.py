__author__ = 'chris'
"""Initial implementation of complex numbers."""


class Cplx:
    #pass statement no longer needed because class body is not empty anymore
    #pass

    def __init__(c, real, imag):
        c.real = real
        c.imag = imag

    def cadd(c1, c2):
        c = Cplx(c1.real + c2.real, c1.imag + c2.imag)
        return c

    def cstr(c):
        return "%s+%sj" % (c.real, c.imag)


if __name__ == "__main__":
    zero = Cplx(0.0, 0.0)
    one = Cplx(1.0, 0.0)
    i = Cplx(0.0, 1.0)
    result = zero.cadd(one.cadd(i))
    print(result.cstr())