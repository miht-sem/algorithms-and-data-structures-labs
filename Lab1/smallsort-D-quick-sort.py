from random import randint


def quick_sort(list_):
    if len(list_) < 2:
        return list_
    main_el = randint(0, len(list_) - 2)
    pivot = list_[main_el]
    less = [i for i in list_[:main_el] if i <= pivot] + [i for i in list_[main_el + 1:] if i <= pivot]
    greater = [i for i in list_[:main_el] if i > pivot] + [i for i in list_[main_el + 1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


file = open('smallsort.in', 'r')
write_file = open('smallsort.out', 'w')

arr = list(map(int, file.readlines()[1].split()))
arr = list(map(str, quick_sort(arr)))
write_file.write(' '.join(arr))

file.close()
write_file.close()