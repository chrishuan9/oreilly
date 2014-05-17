__author__ = 'chris'
"""Produce a listing of people's names, ages and weights."""
data = [
    ("Steve", 59, 202),
    ("Dorothy", 49, 156),
    ("Simon", 39, 155),
    ("David", 61, 135)
]
for row in data:
    print("{0[0]:<12s} {0[1]:4d} {0[2]:4d}".format(row))