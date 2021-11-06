def merge(list_1, list_2, ind):
    i = 0
    j = 0
    merge_list = []

    while i < len(list_1) and j < len(list_2):
        if list_1[i][ind] <= list_2[j][ind]:
            merge_list.append(list_1[i])
            i += 1
        else:
            merge_list.append(list_2[j])
            j += 1

    merge_list += list_1[i:] + list_2[j:]

    return merge_list


def merge_sort(list_, ind):
    if len(list_) < 2:
        return list_

    middle = len(list_) // 2
    return merge(merge_sort(list_[:middle], ind), merge_sort(list_[middle:], ind), ind)


with open('radixsort.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('radixsort.out', 'w')

n, m, k = map(int, lines[0].rstrip().split())
arr = [lines[i].strip().rstrip() for i in range(1, n+1)]
temp = 0
count = 0
for i in range(m-1, -1, -1):
    arr = merge_sort(arr, i)
    count += 1
    if count == k:
        break
print(*arr, sep='\n', file=file_write)
file_write.close()
