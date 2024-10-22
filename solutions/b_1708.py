import sys
from functools import cmp_to_key
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def ccw(_x1, _y1, _x2, _y2):
    return _x1 * _y2 - _x2 * _y1


def cmp_ccw(p1, p2):
    _v1 = (p1.x - start.x, p1.y - start.y)
    _v2 = (p2.x - start.x, p2.y - start.y)
    d = ccw(*_v1, *_v2)
    if d == 0:
        v_size = [(x ** 2 + y ** 2) for x, y in [_v1, _v2]]
        return int(v_size[0] > v_size[1])
    return -1 * (d // abs(d))


read = sys.stdin.readline
N = int(read())
points = sorted([Point(*map(int, read().split())) for _ in range(N)], key=lambda p: (p.y, p.x))
start = points[0]  # base point
slice_points = sorted(points[1:], key=cmp_to_key(cmp_ccw))
stack = [points[0], slice_points[0]]
for point in slice_points[1:]:
    while len(stack) >= 2 and ccw(
            stack[-1].x - stack[-2].x, stack[-1].y - stack[-2].y,
            point.x - stack[-1].x, point.y - stack[-1].y) <= 0:
        stack.pop()
    stack.append(point)

print(len(stack))
