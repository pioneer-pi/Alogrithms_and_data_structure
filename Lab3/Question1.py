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


#Teacher's code
def get_topk(database,k):
    k_largest(database,0,len(database)-1,k)
def k_largest(a,l,r,k):
    if l < r:
        p = partition(a,l,r)
        if r-p+1 == k:
            return
        elif r-p+1 < k:
            k_largest(a,l,p-1,k-r+p-1)
        else:
            k_largest(a,p+1,r,k)

def partition(a,l,r):
    if l > r:
        raise IndexError("Index out of range")
    elif l == r:
        return l
    else:
        m = (l+r)//2
        pivot_pos = sorted({l:a[l],m:a[m],r:a[r]}.items(), key = lambda  x:x[1].rating)[1][0]
        pivot = a[pivot_pos]
        a[pivot_pos] = a[l]
        a[l] = pivot
        i = l + 1
        j = r
        while True:
            while i <= r and a[i].rating < pivot.rating:
                i += 1
            while j >= 1 and a[j].rating > pivot.rating:
                j -= 1
            if i < j:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
            else:
                a[l] = a[j]
                a[j] = pivot
                return j