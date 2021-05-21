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

def get_topk(database,k):
    merge_sort(database,0,len(database)-1)
    return database[:k]

def merge_sort(array,left,right):
    if left >= right:
        return array
    middle = (left+right)//2
    merge_sort(array,left,middle)
    merge_sort(array,middle+1,right)
    pointer1 = left
    pointer2 = middle+1
    sorted_list = []
    while pointer1 <= middle and pointer2 <= right:
        if array[pointer1].rating >= array[pointer2].rating:
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



database = [
    Product(100, 'ABC', 20, '2016-7-20', 3.1),
    Product(101, 'BC', 50, '2016-8-13', 4.2),
    Product(102, 'BC', 200, '2018-2-10', 4.1)
]
topk = get_topk(database, 2)
topk.sort(key=lambda x:x.rating, reverse=True)
for d in topk:
    print('{}, {}'.format(d, d.rating))
