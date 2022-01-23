class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        distance = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    distance[i][j] = j
                elif j == 0:
                    distance[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    distance[i][j] = distance[i-1][j-1]
                else:
                    distance[i][j] = min(distance[i-1][j]+1, distance[i][j-1]+1)
                    distance[i][j] = min(distance[i-1][j-1]+1, distance[i][j])
        return distance[len(word1)][len(word2)]


# also a good solution
class Solution:
    def minDistance(self, word1, word2, i, j, memo):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance2(word1, word2, i + 1, j + 1, memo)
            else:
                insert = 1 + self.minDistance2(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance2(word1, word2, i + 1, j, memo)
                replace = 1 + self.minDistance2(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]
