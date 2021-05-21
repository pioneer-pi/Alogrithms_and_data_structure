cent = [50,20,10,5,1]
def count(n):
    if n < 1:
        return 0
    for i in cent:
        if i < n:
            print("{} x {}".format(i,n//i))
            return n//i + count(n%i)
print(count(97))