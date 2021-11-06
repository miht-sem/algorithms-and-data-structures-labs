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

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + ">-"
            cur = cur.next
        return out[::-1]

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


with open('postfix.in', 'r') as file_read:
    line = file_read.readline().strip().split()


file_write = open('postfix.out', 'w')
stack = Stack()

for i in line:
    if i not in '+-*':
        stack.push(int(i))
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.push(a + b)
        elif i == '-':
            stack.push(a - b)
        else:
            stack.push(a * b)

print(stack.pop(), file=file_write)
file_write.close()
