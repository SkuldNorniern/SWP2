import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target): # L :탐색 대상이 되는 리스트 , l : lower , U : upper , target : 탐색하고자하는 값
    m = int ( (l + (u-1) ) // 2 )
    if l>u:
        return -1
    elif L[m] == target : # target이 중간값일 때
        return L[m]
    elif target > L[m] : # target이 중간값보다 위에 있을 때
        return recbinsearch(L,m, u, target)
    elif target < L[m] : # target이 중간값보다 아래에 있을 때
        return recbinsearch(L ,l , m , target )


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
