file = open('turtle.in', 'r')
write_file = open('turtle.out', 'w')

n, m = map(int, file.readline().split())
arr = [[j for j in list(map(int, i.strip().split()))] for i in file.readlines()]

din_arr = [[0 for i in range(m)] for j in range(n)]
din_arr[n-1][0] = arr[n-1][0]

for i in range(n-2, -1, -1):
    din_arr[i][0] = din_arr[i + 1][0] + arr[i][0]

for i in range(1, m):
    din_arr[n-1][i] = din_arr[n-1][i-1] + arr[n-1][i]

for i in range(n-2, -1, -1):
    for j in range(1, m):
        din_arr[i][j] = max(din_arr[i+1][j], din_arr[i][j-1]) + arr[i][j]

write_file.write(str(din_arr[0][m-1]))

file.close()
write_file.close()