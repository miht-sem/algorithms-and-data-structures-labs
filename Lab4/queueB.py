class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def enQueue(self, value):
        node = Node(value)

        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deQueue(self):

        if self.front is None:
            raise Exception('Queue is empty!')

        removed_element = self.front.value

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed_element


stack = Queue()

with open('queue.in', 'r') as file_read:
    lines = file_read.readlines()

file_write = open('queue.out', 'w')

n = int(lines[0])
arr = []

for i in range(1, n + 1):
    command = lines[i].rstrip().split()
    if command[0] == '+':
        stack.enQueue(command[1])
    else:
        print(stack.deQueue(), file=file_write)

file_write.close()
