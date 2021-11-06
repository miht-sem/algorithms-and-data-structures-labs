file = open('sortland.in', 'r')
write_file = open('sortland.out', 'w')

arr = list(map(float, file.readlines()[1].split()))
N = len(arr)

residents = {}

for ind, el in enumerate(arr, 1):
    residents[el] = ind

for i in range(1, N):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

arr = list(map(str, [residents[arr[0]], residents[arr[len(arr) // 2]], residents[arr[-1]]]))
write_file.write(' '.join(arr))

file.close()
write_file.close()
