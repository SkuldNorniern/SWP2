import time
import random

def iterfibo(n) :
    List = [0, 1, 1]
    # final number = n
    for i in range(3, n):
        List.append(int(List[i - 1]) + int(List[i - 2]))
    return List


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    #Iterfibo 시간
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    # fibo 시간
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
