from random import random
def quicksort(a: list):
    quicksort1(a, 0, len(a)-1)
    return a

def quicksort1(a:list, left: int, right:int):
    if left >= right:
        return
    pivot = partition(a, left, right)
    quicksort1(a, left, pivot-1)
    quicksort1(a, pivot+1, right)


def partition(a: list, left: int, right: int):
    pivot = selectPivot(left, right)
    swap(a, pivot, right)
    i = left
    j = right-1
    while i<= j:
        if a[i] <= a[right]:
            i += 1
        elif a[j] > a[right]:
            j -= 1
        else:
            swap(a, i, j)
    swap(a, i, right)
    return i

def selectPivot(left: int, right:int):
    return left + int(random()*(right-left+1))

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == "__main__":
    a = [1, 9, 8, 5, 3]
    quicksort(a)
    print(a)
