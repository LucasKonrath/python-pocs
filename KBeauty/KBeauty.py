from collections import Counter
from math import comb


class KBeauty:
    def calculateBeauty(self, word: str, k: int) -> int:
        counter = Counter(word)
        if k > len(counter):
            return 0
        modulus = 10**9 + 7
        sorted_counts = sorted(counter.values(), reverse=True)
        max_freq = sorted_counts[k - 1]
        count = sorted_counts.count(max_freq)
        mult = 1

        for freq in sorted_counts:
            if freq == max_freq:
                break
            k -= 1
            mult = mult * freq % modulus

        return mult * comb(count, k) * pow(max_freq, k, modulus) % modulus


def main():
    kbeauty = KBeauty()
    word = "abbc"
    k = 2
    result = kbeauty.calculateBeauty(word, k)
    print(f"The beauty of the word '{word}' with k={k} is: {result}")


if __name__ == "__main__":
    main()

import unittest


class TestKBeauty(unittest.TestCase):
    def setUp(self):
        self.kbeauty = KBeauty()

    def test_basic(self):
        self.assertEqual(self.kbeauty.calculateBeauty("abbc", 2), 4)

    def test_all_unique(self):
        self.assertEqual(self.kbeauty.calculateBeauty("abcd", 2), 6)

    def test_all_same(self):
        self.assertEqual(self.kbeauty.calculateBeauty("aaaa", 1), 4)
        self.assertEqual(self.kbeauty.calculateBeauty("aaaa", 2), 0)

    def test_k_greater_than_unique(self):
        self.assertEqual(self.kbeauty.calculateBeauty("aabb", 3), 0)

    def test_empty_string(self):
        self.assertEqual(self.kbeauty.calculateBeauty("", 1), 0)

    def test_k_equals_unique(self):
        self.assertEqual(self.kbeauty.calculateBeauty("aabbcc", 3), 8)

    def test_large_k(self):
        self.assertEqual(self.kbeauty.calculateBeauty("abcde", 5), 1)


if __name__ == "__main__":
    unittest.main()
