def getMax(input: list):
    M = [0]*(len(input))
    M[0] = input[0]
    globalMax = input[0]
    for i in range(1, len(input)):
        M[i] = max(M[i-1] + input[i], input[i])
        globalMax = max(globalMax, M[i])
    return globalMax

def getMax2(input: list):
    lastMax = input[0]
    globalMax = input[0]
    for i in range(1, len(input)):
        lastMax = max(lastMax + input[i], input[i])
        globalMax = max(globalMax, lastMax)
    return globalMax

if __name__ == "__main__":
    print(getMax2([1,2,4,-1,-2,10,-1]))
