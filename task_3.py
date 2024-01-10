"""
You are given a list of cube details (tuple of 4 integers: X coordinate, Y coordinate, Z coordinate, edge length).

> Each coordinate is the minimum value.
> All edges parallel to the coordinate axes.

If the cube share the part of another cube or touch with the face of another cube, they are considered as one object.
You should return a list (or iterable) of the volumes of all objects.

--Input--
    A list of tuples of 4 integers: X coordinate, Y coordinate, Z coordinate, edge length.

--Output--
    A list of integers (volume of cubes).

--Example--
    sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52]       # fused
    sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54]       # touch with faces
    sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27]   # touch with edges

"""

from typing import Tuple, List, Iterable


def fused_cubes(cubes: List[Tuple[int, int, int, int]]) -> Iterable[int]:
    # implement
    return []


if __name__ == '__main__':
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'