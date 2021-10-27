from math import dist
from typing import List, Tuple

points = [(1,2), (3,3), (5,4)]

def calculate_distance(a, b):
    return dist(a, b)

def main(points):
    data = {}

    for point in points:
        for _point in points:
            if point != _point:
                data[(point, _point)] = calculate_distance(point, _point)

    if data:
        min_distance = min(data.values())
        max_distance = max(data.values())

        for pair, distance in data.items():
            if distance == min_distance:
                min_pair = pair
            elif distance == max_distance:
                max_pair = pair

        return {
            "points": points,
            "min_distance": {
                "distance": min_distance,
                "points": min_pair
            },
            "max_distance": {
                "distance": max_distance,
                "points": max_pair
            }
        }
    return {
        "points": points
    }
