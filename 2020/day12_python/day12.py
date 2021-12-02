import sys
import re
import math
import numpy as np


def main():
    east, north = (0, 0)
    waypoint = [10, 1]

    for line in sys.stdin:
        g = re.findall(r'([NSEWLRF])(\d+)', line)[0]
        action = g[0]
        value = int(g[1])

        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L' or action == 'R':
            if action == 'L':
                value *= -1
            rad = value / 360 * 2 * math.pi
            c, s = np.cos(rad), np.sin(rad)
            j = np.array([[c, s], [-s, c]])
            waypoint = np.dot(j, waypoint)
        elif action == 'F':
            east += waypoint[0] * value
            north += waypoint[1] * value

    print(int(round(abs(east) + abs(north))))


if __name__ == '__main__':
    main()