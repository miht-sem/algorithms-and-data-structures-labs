class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def peek(self):
        if self.isEmpty():
            raise Exception('You are trying to peek empty stack!')
        return self.head.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('You are trying to pop from empty stack!')
        pop_element = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return pop_element.value


stack = Stack()

with open('stack.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('stack.out', 'w')

n = int(lines[0])
arr = []

for i in range(1, n+1):
    command = lines[i].rstrip().split()
    if command[0] == '+':
        stack.push(command[1])
    else:
        print(stack.pop(), file=file_write)

file_write.close()


