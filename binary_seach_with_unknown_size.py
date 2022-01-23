# Given a sorted array with unknown size, how to determine whether a number is in it or not.
# Example: dict[x] = {1 3 5 7 9 .... 1000 ... 10000000 ....}

#Target == 9999
#assumption if input[index] == NULL then we know the size of dictionary is < index

#index = 0
class DictWrapper:
    __a = []
    def __init__(self, a):
        print(a)
        if type(a) is list:
            self._a = a
    def __getitem__(self, n):
            if n>= len(self._a):
                return None
            else:
                return self._a[n]




def binary_search(dict, left, right, target):
  # print(dict.__a__)

  while left <= right:
    mid = (left + right) // 2
    # print(f"left={left} right={right} mid={mid}")
    if dict[mid] == None:
        right = mid
    elif dict[mid] == target:
      return mid
    elif dict[mid] < target:
      left = mid+1
    else:
      right = mid-1
  return -1

def binary_search_with_unknown_size(dict, index, target):
  while dict[index] is not None:
    print(index)
    if dict[index] == target:
      return index
    elif dict[index] < target:
        if index == 0:
            index = 1
        else:
            index *= 2
    else:
      break



  return binary_search(dict, index//2, index, target)

if __name__ == "__main__":
    d = DictWrapper([1,3,5,7,9,1000,10000000])
    print(binary_search_with_unknown_size(d, 0, 1000))
    d = DictWrapper([1,3,4,4,6,10,11,12,15,15])
    print(binary_search_with_unknown_size(d, 0, 6))
