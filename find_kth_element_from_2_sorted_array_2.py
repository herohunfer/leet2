# 0 1 2 3   4  5
# 1 2 3 8  10 13
# 2 5 7 11 13 14

# 1 2 2 3 5 7 8 10 11 13 13 14

#5th -> 5
#2 3
#7 3
import sys

def find(a,b, aleft, bleft, k):
    if k == 1:
        return min(a[aleft], b[bleft])
    # edge case
    # if one array fully tranversed, only need look at the other
    if aleft >= len(a):
        return b[bleft+k-1]
    if bleft >= len(b):
        return a[aleft+k-1]
    # include left node, therefore need -1

    amid = aleft + k//2 -1
    bmid = bleft + k//2 -1
    aval = sys.maxsize if amid >= len(a) else a[amid]
    bval = sys.maxsize if bmid >= len(b) else b[bmid]
    if aval < bval:
        aleft = amid + 1
    else:
        bleft = bmid + 1


    return find(a,b,aleft, bleft, k-k//2)

def main():
    print(find([1,2,3,8,10,13], [2,5,7,11,13,14],0, 0, 5))

if __name__ == "__main__":
    main()
