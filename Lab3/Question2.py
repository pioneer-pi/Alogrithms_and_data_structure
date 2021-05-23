class minheap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        str_ = ""
        if self.data:
            for i in self.data[:-1]:
                str_ += str(i) + ", "
            str_ += str(self.data[-1])
        return str_

    def build(self, lst):
        self.data = lst
        length = len(self)
        start = (length-1-1)//2
        while start >= 0:
            self.down(start)
            start -= 1

    def insert(self, x):
        self.data.append(x)
        position = len(self)-1
        pre = (position-1)//2
        while pre >= 0:
            if self.data[position] < self.data[pre]:
                self.data[position],self.data[pre] = self.data[pre],self.data[position]
                position = pre
                pre = (pre-1) // 2
            else:
                break

    def delete_min(self):
        if len(self) == 0:
            print("The heap is empty!")
            return
        else:
            min_value = self.data[0]
            last = self.data.pop()
            if len(self.data) > 1 :
                self.data[0] = last
                self.down(0)
        return min_value

    def down(self,index):
        end = (len(self) - 1 - 1)//2
        while index <= end:
            left = index * 2 + 1
            right = index * 2 + 2
            if right <= len(self)-1 and self.data[left] > self.data[right]:
                min_ = right
            else:
                min_ = left
            if self.data[index] > self.data[min_]:
                self.data[index],self.data[min_] = self.data[min_],self.data[index]
                index = min_
            else:
                break

# h = minheap()
# h.build([12, 3, 4, 7, 6, 13, 1, 10, 9, 8, 14])
# print(h)
# h.insert(11)
# print(h)
# x = h.delete_min()
# print(x)
# print(h)

# h = minheap()
# print(h)
# h.insert(1)
# print(h)
# h.insert(2)
# print(h)
# h.insert(3)
# print(h)
# print(h.delete_min())
# print(h)
# h.delete_min()
# h.delete_min()
# h.delete_min()

# h.delete_min()
# print(h)
# h.delete_min()
# print(h)
# h.insert(2)
# print(h)