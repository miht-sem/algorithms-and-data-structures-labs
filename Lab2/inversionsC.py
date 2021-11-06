def merge(list_1, list_2):
    global count_inversions
    i = 0
    j = 0
    merge_list = []

    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            merge_list.append(list_1[i])
            i += 1
        else:
            merge_list.append(list_2[j])
            j += 1
            count_inversions += len(list_1) - i

    merge_list += list_1[i:] + list_2[j:]

    return merge_list


def merge_sort(list_):
    if len(list_) < 2:
        return list_

    middle = len(list_) // 2
    return merge(merge_sort(list_[:middle]), merge_sort(list_[middle:]))


file_read = open('inversions.in', 'r')
write_file = open('inversions.out', 'w')

count_inversions = 0

arr = list(map(int, file_read.readlines()[1].split()))
merge_sort(arr)

write_file.write(str(count_inversions))

file_read.close()
write_file.close()

