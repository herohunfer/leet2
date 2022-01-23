def large_rectange_of_1s(m):
    d = [[0 for i in range(len(m[0]))] for j in range(len(m))]
    largest = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                d[i][j] = max(1, d[i-1][j]+1, d[i][j-1]+1, (d[i-1][j]+1)*(d[i][j-1]+1))
                largest = max(largest, d[i][j])
            else:
                d[i][j] = 0
    return largest
if __name__ == "__main__":
    print(large_rectange_of_1s(["10100", "10111", "11111", "10010"]))
    ###
    10100
    10111
    11111
    10010
    ###
