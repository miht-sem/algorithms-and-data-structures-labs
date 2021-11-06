file = open('aplusbb.in', 'r')
write_file = open('aplusbb.out', 'w')

a, b = map(int, file.readline().split())
write_file.write(str(a + b ** 2))

file.close()
write_file.close()