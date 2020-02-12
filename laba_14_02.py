def collision(point_arr):
    if (len(point_arr) >= 2):
        import math
        (x1, y1, vx1, vy1) = point_arr[0]
        (x2, y2, vx2, vy2) = point_arr[1]
        if(math.fabs(x1 - x2)< 1 and math.fabs(y1 - y2)< 1):
            point_arr1 = [(x1,y1,vx2,vy2), (x2, y2, vx1, vy1)]
        else:
            point_arr1 = point_arr
    else:
        point_arr1 = point_arr
    return point_arr1

def test_baseline():
    # Радиус молекул == 1
    assert collision([])==[]
    assert collision([(0,0, 5,5)])==[(0,0, 5,5)]
    assert collision([(0,0, 5,5), (2,2, -5,-5)])==[(0,0, 5,5), (2,2, -5,-5)]
    assert collision([(0, 0, 5, 5), (0.5, 0.5, -5, -5)]) == [(0, 0, -5, -5), (0.5, 0.5, 5, 5)]
    # Тест на разлет при слишком близком столкновении