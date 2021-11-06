from random import randint


def quick_sort(list_):
    if len(list_) < 2:
        return list_
    fix = randint(0, len(list_) - 1)
    pivot = list_[fix]
    less = [i for i in list_[:fix] if i <= pivot] + [i for i in list_[fix+1:] if i <= pivot]
    greater = [i for i in list_[:fix] if i > pivot] + [i for i in list_[fix+1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


file_read = open('kth.in', 'r')
write_file = open('kth.out', 'w')


n, k = map(int, file_read.readline().split())
A, B, C, a1, a2 = map(int, file_read.readline().split())

arr = [a1, a2]
for i in range(2, n):
    num = A * arr[i - 2] + B * arr[i - 1] + C
    if num > ((2 ** 32) - 1):
        arr.append(num - 2 ** 33)
    elif num < (-((2 ** 32) - 1)):
        arr.append(num % (2 ** 32))
    else:
        arr.append(num)


write_file.write(" ".join(list(map(str, arr))) + '\n')

arr = quick_sort(arr)

write_file.write(str(arr[k-1]) + '\n')
write_file.write(" ".join(list(map(str, arr))))


file_read.close()
write_file.close()
