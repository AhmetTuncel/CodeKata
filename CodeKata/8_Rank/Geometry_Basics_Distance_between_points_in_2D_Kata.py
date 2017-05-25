"""
Point objects have x and y attributes.

Write a function calculating distance between Point a and Point b.

Tests round answers to 6 decimal places.

"""
def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5