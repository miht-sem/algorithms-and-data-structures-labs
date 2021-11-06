def merge(list_1, list_2):
    i = 0
    j = 0
    merge_list = []

    while i < len(list_1) and j < len(list_2):
        if list_1[i][0] <= list_2[j][0]:
            merge_list.append(list_1[i])
            i += 1
        else:
            merge_list.append(list_2[j])
            j += 1

    merge_list += list_1[i:] + list_2[j:]

    return merge_list


def merge_sort(list_):
    if len(list_) < 2:
        return list_

    middle = len(list_) // 2
    return merge(merge_sort(list_[:middle]), merge_sort(list_[middle:]))


file_read = open('race.in', 'r')
write_file = open('race.out', 'w')


n = int(file_read.readline())
countries = []

for i in range(n):
    countries.append(file_read.readline().split())

sorted_list = merge_sort(countries)

f = 0
temp = ''
for i in sorted_list:
    if i[0] != temp:
        write_file.writelines([f'=== {i[0]} ===\n', i[1] + '\n'])
        temp = i[0]
    else:
        write_file.write(i[1] + '\n')

file_read.close()
write_file.close()
