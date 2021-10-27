# Task

We need to write an application that while accept a list of pair off points.

And calculate the closest and the most distance one.

The app should return a response like this one

```
{
    # points received
    'points': [(1, 4), (4, 4), (3, 2), (5, 1)],
    # closest pair of points
    'min_distance': {'distance': 2.23606797749979, 'points': ((5, 1), (3, 2))},
    # most distant pair of points
    'max_distance': {'distance': 5.0, 'points': ((5, 1), (1, 4))}
    }
```
