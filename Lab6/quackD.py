import queue


def goToLabel(commandToGo):
    for j in range(len(labels)):
        if labels[j][0] == commandToGo:
            return labels[j][1]


with open('quack.in', 'r') as file_read:
    commands = [command.strip() for command in file_read.readlines()]

file_write = open('quack.out', 'w')

queue = queue.Queue()
registers = [0] * 26
labels = []

i = 0
while i < len(commands):
    if commands[i][0] == ':':
        if commands[i][1:] not in labels:
            labels.append([commands[i][1:], i])
    i += 1

i = 0
while i < len(commands):
    if commands[i] == '+':
        queue.put((queue.get() + queue.get()) % 65536)
    elif commands[i] == '-':
        queue.put((queue.get() - queue.get()) % 65536)
    elif commands[i] == '*':
        queue.put((queue.get() * queue.get()) % 65536)
    elif commands[i] == '/':
        x = queue.get()
        y = queue.get()
        if y == 0:
            queue.put(0)
        else:
            queue.put((x // y) % 65536)
    elif commands[i] == '%':
        x = queue.get()
        y = queue.get()
        if y == 0:
            queue.put(0)
        else:
            queue.put((x % y) % 65536)
    elif commands[i][0] == '>':
        registers[ord(commands[i][1]) % 97] = queue.get()
    elif commands[i][0] == '<':
        queue.put(registers[ord(commands[i][1]) % 97])
    elif commands[i] == 'P':
        print(queue.get(), file=file_write)
    elif commands[i][0] == 'P':
        print(registers[ord(commands[i][1]) % 97], file=file_write)
    elif commands[i] == 'C':
        print(chr(queue.get() % 256), end='', file=file_write)
    elif commands[i][0] == 'C':
        print(chr(registers[ord(commands[i][1]) % 97] % 256), end='', file=file_write)
    elif commands[i][0] == 'J':
        i = goToLabel(commands[i][1:])
    elif commands[i][0] == 'Z':
        if registers[ord(commands[i][1]) % 97] == 0:
            i = goToLabel(commands[i][2:])
    elif commands[i][0] == 'E':
        if registers[ord(commands[i][1]) % 97] == registers[ord(commands[i][2]) % 97]:
            i = goToLabel(commands[i][3:])
    elif commands[i][0] == 'G':
        if registers[ord(commands[i][1]) % 97] > registers[ord(commands[i][2]) % 97]:
            i = goToLabel(commands[i][3:])
    elif commands[i] == 'Q':
        exit(1)
    elif commands[i].isdigit():
        queue.put(int(commands[i]))
    i += 1

file_write.close()
