class OrderedStream:

    def __init__(self, n: int):
        self.words = [''] * n
        self.n = n
        self.ptr = 0

    def insert(self, idKey: int, value: str):
        
        # Declaring variables
        res = []

        # Inserting the value into the words list
        self.words[idKey - 1] = value

        # Making the result list
        while self.ptr < self.n and self.words[self.ptr]:
            res.append(self.words[self.ptr])
            self.ptr += 1

        # Returning result
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

# Time - O(N)
# Space - O(N)