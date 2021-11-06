file = open('smallsort.in', 'r')
write_file = open('smallsort.out', 'w')

arr = list(map(int, file.readlines()[1].split()))

N = len(arr)

for i in range(1, N):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j-1] = arr[j - 1], arr[j]
        else:
            break

arr = list(map(str, arr))

write_file.write(' '.join(arr))

file.close()
write_file.close()