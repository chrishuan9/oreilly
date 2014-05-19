__author__ = 'chris'
"""Print all factorials less than 1000."""
c = 0
f = 1
while (f < 1000):
    print(f)
    c += 1
    f = 1
    for n in range(c,0,-1):
        f = f * n
#
# if you already know N!, then you can produce (N+1)! (the next value in the sequence) by multiplying N! by N+1.
# You can make this program even more efficient by avoiding the second loop, since the second loop would be run
# for each factorial. This saves a lot of work.
#
c = 1
f = 1
while (f < 1000):
    print(f)
    c += 1
    f *= c