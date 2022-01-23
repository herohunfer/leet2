# 0 1 2 3   4  5
# 1 2 3 8  10 13
# 2 5 7 11 13 14

# 1 2 2 3 5 7 8 10 11 13 13 14

#5th -> 5
#2 3
#7 3

# TODO: better use a helper function to pass k value down




import sys
def find_kth_smallest_element(a, b, k):
    a_start = 0
    b_start = 0
    a_mid = 0
    b_mid = 0
    while k>1:
        a_mid =  a_start + k //2 -1
        b_mid = b_start + k //2-1
        a_val =  sys.maxsize if a_mid >= len(a) else a[a_mid]
        b_val = sys.maxsize if b_mid >= len(b) else b[b_mid]
        print(f"a_start={a_start} a_mid={a_mid} a_val={a_val} b_start={b_start} b_mid={b_mid} b_val={b_val} k={k}")
        if a_val < b_val:
            # get rid of left half of a and right half of b
            a_start = a_mid+1
        else:
            b_start = b_mid+1
        k = k - k//2

    print(f"a_start={a_start} b_start={b_start} k={k}")

    if a_start >= len(a):
        return b[b_start + k -1]
    if b_start >= len(b):
        return a[a_start + k -1]
    if k == 1:
        print(k)
        return min(a[a_start], b[b_start])


print(find_kth_smallest_element([1,2,3,8,10,13], [2,5,7,11,13,14],5))
