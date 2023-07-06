class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop(-1)

    def top(self):
        return self.data[0]

    def __str__(self):
        return f"[{', '.join(self.data)}]"
