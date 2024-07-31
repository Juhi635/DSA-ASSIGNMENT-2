# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# SUBMISSION: https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1277075059

class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val):
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        return self.list[int(len(self.list) * self._random())]

    def _random(self):
        x = 123456789
        x = (x * 1103515245 + 12345) % 2**31
        return x / 2**31