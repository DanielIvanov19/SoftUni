from typing import List


class BaseStack:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(self.data)}]"

class AddStack(BaseStack):
    def push(self, element: str):
        self.data.append(element)

class RemoveStack(BaseStack):
    def pop(self):
        return self.data.pop()

class TopStack(BaseStack):
    def top(self):
        return self.data[0]

class Stack(AddStack, RemoveStack, TopStack):
    pass

s = Stack()
s.push('a')
s.push('a')
s.push('a')
s.pop()
print(s.top())
print(s.is_empty())
print(s)