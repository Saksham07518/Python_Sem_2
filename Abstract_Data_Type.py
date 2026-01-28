class ArrayADT:
    """
    Array Abstract Data Type (ADT)
    Defines operations on array without exposing implementation details
    """

    def __init__(self, size):
        self.size = size              # Maximum capacity
        self.array = [None] * size    # Internal storage
        self.length = 0               # Current number of elements

    # -------- Traversal --------
    def traverse(self):
        if self.length == 0:
            print("Array is empty")
            return
        for i in range(self.length):
            print(self.array[i], end=" ")
        print()

    # -------- Insertion --------
    def insert(self, index, value):
        if self.length == self.size:
            print("Overflow: Array is full")
            return
        if index < 0 or index > self.length:
            print("Invalid index")
            return

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.length += 1

    # -------- Deletion --------
    def delete(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index")
            return

        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.length - 1] = None
        self.length -= 1

    # -------- Search --------
    def search(self, value):
        for i in range(self.length):
            if self.array[i] == value:
                return i
        return -1

    # -------- Update --------
    def update(self, index, value):
        if index < 0 or index >= self.length:
            print("Invalid index")
            return
        self.array[index] = value

    # -------- Utility Methods --------
    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def get_size(self):
        return self.length


arr = ArrayADT(5)

arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)

arr.traverse()        # 10 20 30

arr.update(1, 25)
arr.delete(0)

arr.traverse()        # 25 30