class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        # find max and keep at the end
        i = 0
        while i < len(self.arr)-1:
            maxIndex = 0
            j = 1
            while j < len(self.arr) - i - 1:
                if self.arr[j] > self.arr[maxIndex]:
                    maxIndex = j
                j += 1
            temp = self.arr[len(self.arr) - i - 1]
            self.arr[len(self.arr) - i - 1] = self.arr[maxIndex]
            self.arr[maxIndex] = temp
            i += 1

        print(*self.arr)


s = SelectionSort([9, 1, 8, 2, 7, 3, 6, 4, 5])
s.sort()
