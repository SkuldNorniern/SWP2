import time
import random

def fibo(n):
    lst = [1,1]
    if n == 1 or n == 2:
        return n

    for i in range(2, n):
        lst.append(lst[i-2]+lst[i-1])
    return lst[n-1]


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
