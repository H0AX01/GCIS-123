from polygon import Polygon
import pytest

def test_polygon_initialization():
    print("Test:")
    polygon = Polygon("Triangle", [3.0, 3.0, 3.0])
    print(polygon.get_name() == "Triangle")  
    print(polygon.get_side() == [3.0, 3.0, 3.0])  
    polygon.set_name("Hexagon")
    polygon.set_side([4.0,4.0,4.0])
    print("After Changing the values name :",polygon.get_name())
    print("After Changing the valuses side:",polygon.get_side())




# Phase 2 Testing wether the polygon is equal or not
def test_polygon_equality():
    print("We test the equality first:")
    polygon1 = Polygon("Triangle", [3.0, 3.0, 3.0])
    polygon2 = Polygon("Triangle", [3.0, 3.0, 3.0])
    print(polygon1 == polygon2)  

def test_polygon_not_equal():
    print("Now we test if they arent equal:")
    polygon1 = Polygon("Triangle", [3.0, 3.0, 3.0])
    polygon2 = Polygon("Square", [1.0, 1.0, 1.0])
    print(polygon1 != polygon2)

def test_polygon_str():
    print("We test the String Function:")
    polygon3 = Polygon("Triangle", [3, 3, 3])
    print(polygon3.__str__() == "Triangle with sides [3, 3, 3]")
    print(polygon3)

def calculate_circumference ():
    polygon4 = Polygon("Square", [4.0,5.0,6.0])
    assert polygon4.calculate_circumference() == pytest.approx(15.0, rel=0.1)

    polygon5 = Polygon("Hexagon", [6.0,7.0,8.0])
    assert polygon5.calculate_circumference() == pytest.approx(21.0, rel=0.1)





test_polygon_initialization()
test_polygon_equality()
test_polygon_not_equal()
test_polygon_str()
calculate_circumference()