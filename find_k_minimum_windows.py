def find_k_minimum_windows(S: str, T: str):
    need, missing = collec

    res = []
    C = [0] * 26
    currentSize = 0
    count = 0
    Current = [0] * 26
    for c in T:
        C[ord(c)-ord('A')] +=1
    print(C)
    for size in range(len(T), len(S)+1):
        currentSize = 0
        Current = [0] * 26
        for i in range(len(S)-1, 0, -1):
            if currentSize < size:
                Current[ord(S[i]) - ord('A')] += 1
                currentSize += 1
            else:
                Current[ord(S[i+size]) - ord('A')] -= 1
                Current[ord(S[i]) - ord('A')] += 1

            if currentSize == size and compare(C, Current):
                print(S[i:i+size])
                print(Current)
                res.append(S[i: i+size])
                count += 1
                if k == count:
                    return res

if __name__ == "__main__":
    print(find_k_minimum_windows("ADOBECODEBANCACB", "ABC", 5))
    print(find_k_minimum_windows("ADOBECODEAABNCZA", "ABCA",7))
