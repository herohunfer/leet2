import sys
def sort(input, buffer):
    currentMax = -sys.maxsize-1
    count = 0
    buffer = []
    while len(input) > 0:
        currentMax = -sys.maxsize-1
        while len(input) > 0:
            current = input.pop()
            print(f"current={current} input={input} buffer={buffer}")
            if currentMax < current:
                count = 1
                currentMax = current
            elif currentMax == current:
                count += 1
            buffer.append(current)

        while len(buffer) > 0 and buffer[-1] <= currentMax:
            tmp = buffer.pop()
            if tmp != currentMax:
                input.append(tmp)

        for _ in range(count):
            buffer.append(currentMax)

    while len(buffer) > 0:
        tmp = buffer.pop()
        input.append(tmp)

if __name__ == "__main__":
    input = [2,3,9,5,2]
    sort(input, [])
    print(input)
