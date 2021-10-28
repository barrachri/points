# Task

We need to write an application that accepts a list of 2-dimensional points and calculates the closest and the most distance one.

The app should return a response like this one:

```
{
    'points': [(1, 4), (4, 4), (3, 2), (5, 1)],
    'min_distance': {'distance': 2.23606797749979, 'points': ((5, 1), (3, 2))},
    'max_distance': {'distance': 5.0, 'points': ((5, 1), (1, 4))}
}
```

Where:
- `points` is the list with points received by the app,
- `min_distance` is a dictionary with the value of the minimum distance and the 2 points that have that distance, and
- `max_distance` is a dictionary with the value of the maximum distance and the 2 points that have that distance.

