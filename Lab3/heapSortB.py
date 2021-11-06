def heapify(n, largest):
    root = largest
    left = root * 2 + 1
    right = root * 2 + 2

    if left < n and arr[root] < arr[left]:
        root = left
    if right < n and arr[root] < arr[right]:
        root = right

    if root != largest:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(n, root)


with open('sort.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('sort.out', 'w')

n = int(lines[0])
arr = list(map(int, lines[1].split()))

for i in range(n//2, -1, -1):
    heapify(n, i)

for i in range(n-1, -1, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(i, 0)

print(*arr, file=file_write)
file_write.close()
