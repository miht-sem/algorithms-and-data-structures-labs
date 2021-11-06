file = open('aplusb.in', 'r')
write_file = open('aplusb.out', 'w')

a, b = map(int, file.readline().split())
write_file.write(str(a + b))

file.close()
write_file.close()
