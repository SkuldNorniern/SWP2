import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    g=[1,1,2];
    for i in range(3,n):
        g.append(g[i-1]+g[i-2])
    return g[n-1]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    ans=iterfibo(nbr)
    ts = time.time() - ts
    print("iterFibo(%d)=%d, time %.6f" %(nbr,ans, ts))
