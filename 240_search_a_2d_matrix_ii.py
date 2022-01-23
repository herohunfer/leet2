class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N = len(matrix[0]), len(matrix)
        i = bisect.bisect(matrix[0], target, 0)-1
        # print(f"{i} {j}")
        while i>=0 and j < len(matrix):
            if matrix[j][i] == target:
                return True
            elif matrix[j][i] > target:
                i -= 1
            else:
                j += 1
        return False
        
