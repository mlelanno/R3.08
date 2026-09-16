import pytest
from src.formes import Point

def test_point_creation():
    p = Point(2, 3)
    assert p.get_x() == 2.0
    assert p.get_y() == 3.0

def test_distance_coordonnee():
    p1 = Point(2, 3)
    assert p1.distance_coordonnees(2, 3) == 0

def test_distance_point():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distancePoint(p2) == 5.0

def test_cercle_base():
    p = Point()