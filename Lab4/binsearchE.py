def r_bin_search(num):

    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == num:
            index = middle
            left = middle + 1
        elif num > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return index + 1 if index != -1 else -1


def l_bin_search(num):

    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == num:
            index = middle
            right = middle - 1
        elif num > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return index + 1 if index != -1 else -1


with open('binsearch.in', 'r') as file_read:
    lines = file_read.readlines()


file_write = open('binsearch.out', 'w')

n = int(lines[0])
arr = list(map(int, lines[1].split()))
requests = int(lines[2])
for i in lines[3].split():
    left_bin = l_bin_search(int(i))
    right_bin = r_bin_search(int(i))
    print(left_bin, right_bin, file=file_write)

file_write.close()
