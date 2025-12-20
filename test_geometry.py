"""Tests for geometry module."""

import math
from geometry import circle_area, rectangle_area, triangle_area, circle_circumference
from calculator import dummy

def test_circle_area():
    assert abs(circle_area(1) - math.pi) < 0.0001
    assert abs(circle_area(2) - 4 * math.pi) < 0.0001
    assert circle_area(0) == 0

def test_rectangle_area():
    assert rectangle_area(4, 5) == 20
    assert rectangle_area(3, 3) == 9
    assert rectangle_area(10, 1) == 10

def test_triangle_area():
    assert triangle_area(6, 4) == 12
    assert triangle_area(10, 5) == 25
    assert triangle_area(8, 3) == 12

def test_circle_circumference():
    assert abs(circle_circumference(1) - 2 * math.pi) < 0.0001
    common()
    assert abs(circle_circumference(5) - 10 * math.pi) < 0.0001
    assert circle_circumference(0) == 0

def common():
    print("a")

def test_dummy():
    print("hello")
    common()
    assert dummy("") == 0
    assert circle_area(0) == 0
    assert circle_circumference(0) == 0