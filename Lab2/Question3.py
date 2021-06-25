'''
The code about Merge sort in CSDN.
'''
def merge(left,right):
    res = []
    while (len(left) > 0) and (len(right) > 0):
        if left[0] > right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res
def merge_sort(array,l,r):
    length = len(array)
    if length < 2:
        return array
    mid = length // 2
    left_sort = merge_sort(array[:mid])
    right_sort = merge_sort(array[mid:])
    return merge(left_sort,right_sort)

def Merge_sort(array,left,right):
    if left == right:
        return
    middle = (left+right)//2
    Merge_sort(array,left,middle)
    Merge_sort(array,middle+1,right)
    pointer1 = left
    pointer2 = middle+1
    sorted_list = []
    while pointer1 <= middle and pointer2 <= right:
        if array[pointer1] < array[pointer2]:
            sorted_list.append(array[pointer1])
            pointer1 += 1
        else:
            sorted_list.append(array[pointer2])
            pointer2 += 1
    if pointer1 <= middle:
        for i in range(pointer1,middle+1):
            sorted_list.append(array[i])
    elif pointer2 <= right:
        for i in range(pointer2,right+1):
            sorted_list.append(array[i])
    array[left:right+1] = sorted_list

'''
My own answer
'''

import datetime
class Product:
    def __init__(self, id, name, price, release_date, rating):
        self.id = id
        self.name = name
        self.price = price
        self.release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        self.rating = rating

    def __repr__(self):
        return '{}'.format(self.id)
database = [
    Product(1, 'A', 5000, '2019-10-24', 4.7),
    Product(2, 'B', 300, '2018-1-14', 3.1),
    Product(3, 'C', 1200, '2020-3-3', 5),
    Product(4, 'D', 10, '2019-7-19', 4.2),
    Product(5, 'E', 50, '2019-12-4', 3.5),
    Product(6, 'F', 180, '2021-3-8', 3.9),
    Product(100, 'ABC', 20, '2016-7-20', 3.1),
    Product(101, 'BC', 50, '2016-8-13', 4.2),
    Product(102, 'BC', 200, '2018-2-10', 4.1)
]
def merge_sort2(array,left,right):
    if left >= right:
        return array
    middle = (left+right)//2
    merge_sort2(array,left,middle)
    merge_sort2(array,middle+1,right)
    print("Merge {} and {}".format(array[left:middle+1],array[middle+1:right+1]))
    pointer1 = left
    pointer2 = middle+1
    sorted_list = []
    while pointer1 <= middle and pointer2 <= right:
        if array[pointer1].rating > array[pointer2].rating:
            sorted_list.append(array[pointer1])
            pointer1 += 1
        else:
            sorted_list.append(array[pointer2])
            pointer2 += 1
    if pointer1 <= middle:
        for i in range(pointer1,middle+1):
            sorted_list.append(array[i])
    elif pointer2 <= right:
        for i in range(pointer2,right+1):
            sorted_list.append(array[i])
    array[left:right+1] = sorted_list
    print("After merge: {}".format(array[left:right+1]))

merge_sort2(database,0,len(database)-1)