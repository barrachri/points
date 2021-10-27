from src.main import main


def test_main_points_in_response():
    response = main([])
    assert "points" in response

def test_main_return_points():
    points = [(1,2), (3,3), (5,4)]

    response = main(points)
    assert response['points'] == points


def test_min_distance_in_reponse():
    points = [(1,2), (3,3), (5,4)]

    response = main(points)
    assert "min_distance" in response

def test_max_distance_in_reponse():
    points = [(1,2), (3,3), (5,4)]

    response = main(points)
    assert "max_distance" in response

def test_main_return_min_distance():
    points = [(1,2), (3,3), (5,4)]

    response = main(points)
    assert response['min_distance'] == {
            "distance": 2.23606797749979,
            "points": ((5, 4), (3, 3))
        }

def test_main_return_max_distance():
    points = [(1,2), (3,3), (5,4)]

    response = main(points)
    assert response['max_distance'] == {
            "distance": 4.47213595499958,
            "points": ((5,4), (1,2))
        }
