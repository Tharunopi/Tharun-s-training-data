import time

from PycharmProjects.pythondfe.main import pattern


class SubStrings:

    def __init__(self, text=None, pattern=None):
        self.text = text
        self.pattern = pattern

    def are_equal(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True

    def navie_algorithm(self):
        positions = []

        for i in range(len(self.text)):
            if self.are_equal(self.text[i : i+len(self.pattern)], self.pattern):
                print(self.text[i:i+5], self.pattern)
                positions.append(i)
        return positions

    def rabin_karp_algorithm(self):
        base, prime = 256, 101
        n, m = len(self.text), len(self.pattern)

        pattern_hash = 0
        text_hash = 0



start = time.time()
ss = SubStrings("excel is the college located in namakkal district   excel is popular", "excel")
print(ss.navie_algorithm())
end = time.time()
print(end - start)