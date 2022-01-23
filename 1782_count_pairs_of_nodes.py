class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cnt, res = [0] * (n+1), []
        shared = Counter((min(n1, n2), max(n1,n2)) for n1, n2 in edges)

        for n1,n2 in edges:
            cnt[n1] += 1
            cnt[n2] += 1

        sorted_cnt = sorted(cnt)

        for q in queries:
            ans = 0
            i, j = 1, n
            while i < j:
                if q < sorted_cnt[i] + sorted_cnt[j]:
                    ans += j-i
                    j -= 1
                else:
                    i += 1
            for (i,j), k in shared.items():
                if cnt[i] + cnt[j] > q and cnt[i] + cnt[j] - k <=q:
                    ans -= 1
            res.append(ans)
        return res


# You are given an undirected graph represented by an integer n, which is the number of nodes, and edges, where edges[i] = [ui, vi] which indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.
#
# The answer to the jth query is the number of pairs of nodes (a, b) that satisfy the following conditions:
#
# a < b
# cnt is strictly greater than queries[j], where cnt is the number of edges incident to a or b.
# Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.
#
# Note that there can be repeated edges.
#
#
#
# Example 1:
#
#
# Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# Output: [6,5]
# Explanation: The number of edges incident to at least one of each pair is shown above.
# Example 2:
#
# Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
# Output: [10,10,9,8,6]
#
#
# Constraints:
#
# 2 <= n <= 2 * 104
# 1 <= edges.length <= 105
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length
