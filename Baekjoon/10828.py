# 10828

class Stack():
    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.empty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return int(self.size() == 0)

    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]

import sys
input = sys.stdin.readline
T = int(input())
stack = Stack()

for t in range(T):
    k = input().split()
    if k[0] == 'push':
        stack.push(int(k[1]))
    elif k[0] == 'pop':
        print(stack.pop())
    elif k[0] == 'size':
        print(stack.size())
    elif k[0] == 'empty':
        print(stack.empty())
    elif k[0] == 'top':
        print(stack.top())