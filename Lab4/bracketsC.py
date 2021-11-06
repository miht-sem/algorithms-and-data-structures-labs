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
        cur = self.head
        if not self.isEmpty():
            cur = self.head.next
        # print(value, self.size)
        if value in '([':
            node = Node(value)
            node.next = self.head.next
            self.head.next = node
            self.size += 1
            # print(self, end='\n')
            return True
        elif brackets[value] == cur.value:
            _ = self.pop()
            # print('Yes', self, end='\n\n')
            return True
        else:
            # print('No', self, end='\n\n')
            return False

    def pop(self):
        if self.isEmpty():
            raise Exception('You are trying to pop from empty stack!')
        pop_element = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return pop_element.value


brackets = {']': '[', ')': '('}

with open('brackets.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('brackets.out', 'w')

for i in lines:
    stack = Stack()
    f = 1
    for j in i.strip():
        if not stack.push(j):
            print('NO', file=file_write)
            f = 0
            break
    if f == 1 and stack.isEmpty():
        print('YES', file=file_write)
    elif f != 0:
        print('NO', file=file_write)

file_write.close()
