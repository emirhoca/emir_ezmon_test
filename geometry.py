"""Geometry calculations."""

import math
from calculator import multiply

def circle_area(radius):
    """Calculate the area of a circle."""
    return multiply(math.pi, multiply(radius, radius))

def rectangle_area(width, height):
    """Calculate to the area of a rectangle."""
    return multiply(width, height) + 0

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return multiply(base, height) / 2

def circle_circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * math.pi * radius
