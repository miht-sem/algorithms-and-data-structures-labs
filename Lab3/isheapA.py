with open('isheap.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('isheap.out', 'w')

n = int(lines[0])
arr = list(map(int, lines[1].split()))

for i in range(n):
    if 2 * i + 1 < n:
        if arr[i] > arr[2 * i + 1]:
            print('NO', file=file_write)
            file_write.close()
            exit()
    if 2 * i + 2 < n:
        if arr[i] > arr[2 * i + 2]:
            print('NO', file=file_write)
            file_write.close()
            exit()

print('YES', file=file_write)
file_write.close()
