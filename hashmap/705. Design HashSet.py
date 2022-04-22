# 705. Design HashSet
# Easy


# Larry, https://www.youtube.com/watch?v=-_8pWyYX8yM
class MyHashSet:

    def __init__(self):
        MAX = 10 ** 6 + 2
        self.table = [False] * MAX

    def add(self, key: int) -> None:
        self.table[key] = True

    def remove(self, key: int) -> None:
        self.table[key] = False

    def contains(self, key: int) -> bool:
        return self.table[key]
# 04/21/2022 19:17


