# https://leetcode.com/problems/implement-stack-using-queues/description/
# SUBMISSION: https://leetcode.com/problems/implement-stack-using-queues/submissions/1275168680

class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return not self.stack