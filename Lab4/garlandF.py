import math


def last_lamp():

    left = 0.0
    right = arr[0]

    while not math.isclose(right, left, abs_tol=1e-3):
        arr[1] = (left + right) / 2
        up = 1
        for i in range(2, n):
            arr[i] = 2 * arr[i - 1] - arr[i - 2] + 2
            if arr[i] < 0:
                up = 0
                break
        if up:
            right = arr[1]
        else:
            left = arr[1]

    return arr[-1]


with open('garland.in', 'r') as file_read:
    lines = file_read.readline().strip().split()

file_write = open('garland.out', 'w')

n = int(lines[0])

arr = [0.0 for i in range(n)]
arr[0] = float(lines[1])

print('{0:.2f}'.format(last_lamp()), file=file_write)

file_write.close()