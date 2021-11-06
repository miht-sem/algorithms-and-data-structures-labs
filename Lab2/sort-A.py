from random import randint


def quick_sort(list_):
    if len(list_) < 2:
        return list_
    fix = randint(0, len(list_) - 2)
    fix_element = list_[fix]
    less = [i for i in list_[:fix] if i <= fix_element] + [i for i in list_[fix+1:] if i <= fix_element]
    greater = [i for i in list_[:fix] if i > fix_element] + [i for i in list_[fix + 1:] if i > fix_element]
    return quick_sort(less) + [fix_element] + quick_sort(greater)


file_read = open('sort.in', 'r')
write_file = open('sort.out', 'w')


arr = quick_sort(list(map(int, file_read.readlines()[1].split())))
arr = list(map(str, arr))
write_file.write(' '.join(arr))

file_read.close()
write_file.close()
