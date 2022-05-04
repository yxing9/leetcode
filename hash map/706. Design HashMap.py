# 706. Design HashMap
# Easy


# my solution mimicking Larry's solution yesterday
class MyHashMap:

    def __init__(self):
        MAX = 10 ** 6 + 2
        self.table = [-1] * MAX

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        return self.table[key]

    def remove(self, key: int) -> None:
        self.table[key] = -1
# 04/22/2022 19:46


# Larry, https://www.youtube.com/watch?v=hoAArypm_zc
class MyHashMap:

    def __init__(self):
        MAX = 10 ** 6 + 5
        self.lookup = [None] * MAX

    def put(self, key: int, value: int) -> None:
        self.lookup[key] = value

    def get(self, key: int) -> int:
        if self.lookup[key] is None:
            return -1
        return self.lookup[key]

    def remove(self, key: int) -> None:
        self.lookup[key] = None
# 04/22/2022 20:01
