def heapify(lenOfArray, lower):
    root = lower
    left = root * 2 + 1
    right = root * 2 + 2

    if left < lenOfArray and arr[root][0] > arr[left][0]:
        root = left
    if right < lenOfArray and arr[root][0] > arr[right][0]:
        root = right

    if root != lower:
        arr[root], arr[lower] = arr[lower], arr[root]
        heapify(lenOfArray, root)


def heapify_up(lower):
    root = (lower - 1) // 2
    if lower > 0 and arr[lower][0] < arr[root][0]:
        arr[lower], arr[root] = arr[root], arr[lower]
        heapify_up(root)


with open('priorityqueue.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('priorityqueue.out', 'w')

arr = []
count_ = 1
n = 0
for i in lines:
    a, *_ = i.split()
    if not _:
        if n == 0:
            print('*', file=file_write)
        else:
            arr[0], arr[-1] = arr[-1], arr[0]
            print(arr.pop(-1)[0], file=file_write)
            n = len(arr)
            heapify(n, 0)
    elif len(_) == 1:
        arr.append([int(_[0]), count_])
        n = len(arr)
        heapify_up(n-1)
    else:
        x, y = map(int, _)
        temp = 0
        n = len(arr)
        for j in range(n):
            if arr[j][1] == x:
                arr[j][0] = y
                heapify_up(j)
                break
    count_ += 1


file_write.close()
