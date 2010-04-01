import random
import unittest

class Sorter:
    def bubble_sort(self, items):
        "Uses Bubble Sort to sort a list in O(n^2) time complexity."
        while True:
            for i in range(len(items)-1):
                if items[i] > items[i+1]:
                    items[i], items[i+1] = items[i+1], items[i]
                    break
            else:
                break
        return items

    def insertion_sort(self, items):
        "Uses Insertion Sort to sort a list in \
                O(n^2) - worst case, \
                O(n) - best case, and \
                O(n^2) - average case."
        for removed_index in range(len(items)):
            removed_value = items[removed_index]
            insert_index = removed_index
            while insert_index > 0 and removed_value < items[insert_index-1]:
                items[insert_index] = items[insert_index-1]
                insert_index -= 1
            items[insert_index] = removed_value
        return items

    def mergesort(self, items):
        "Uses Merge Sort to sort a list in \
                O(n * log(n)) - worst case, \
                O(n * log(n)) - best case or O(n) natural variant and \
                O(n * log(n)) - average case."
        if len(items) <= 1:
            return items[:]

        middle = len(items)/2
        left = self.mergesort(items[:middle])
        right = self.mergesort(items[middle:])

        return self.merge(left, right)

    def merge(self, left, right):
        "The merge function for Merge sort."
        if left == [] or right == []:
            return left + right
        elif left[0] <= right[0]:
            return left[:1] + self.merge(left[1:], right)
        else:
            return right[:1] + self.merge(left, right[1:])

class TestSorter(unittest.TestCase):

    def setUp(self):
        self.sorter = Sorter()
        self.seq = range(10)

    def test_bubble_sort(self):
        random.shuffle(self.seq)
        sorted = self.sorter.bubble_sort(self.seq)
        self.assertEqual(sorted, range(10))

    def test_insertion_sort(self):
        random.shuffle(self.seq)
        sorted = self.sorter.insertion_sort(self.seq)
        self.assertEqual(sorted, range(10))

    def test_mergesort(self):
        random.shuffle(self.seq)
        sorted = self.sorter.mergesort(self.seq)
        self.assertEqual(sorted, range(10))

    def test_merge(self):
        right = range(3)
        left = range(3, 7)
        sorted = self.sorter.merge(left, right)
        self.assertEqual(sorted, range(7))

if __name__ == '__main__':
    unittest.main()
