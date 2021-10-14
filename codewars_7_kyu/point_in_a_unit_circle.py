def point_in_circle(x, y):
    return (x**2 + y**2)**(0.5) < 1


if __name__ == '__main__':
    assert point_in_circle(0, 0) == True
    assert point_in_circle(2, 0) == False
    assert point_in_circle(-1.1, 0) == False
    assert point_in_circle(0, 0.9) == True
    assert point_in_circle(1, 0) == False