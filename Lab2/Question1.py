def insertion_sort_recursion(a,n):
    if n == 1:
        return
    else:
        insertion_sort_recursion(a,n-1)
        for i in range(0,n-1):
            if a[n-1] < a[i]:
                a[i],a[n-1] = a[n-1],a[i]
        print(a)

a = [5, 4, 3, 1]
insertion_sort_recursion(a, len(a))