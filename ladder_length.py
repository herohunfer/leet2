class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = [beginWord]
        pos = 0
        path = {beginWord: 1}
        while pos < len(q):
            current = q[pos]
            # print(f"current={current}")
            for i in range(len(current)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == current[i]:
                        continue
                    temp = current[:i] + ch + current[i+1:]

                    if temp in words and temp not in path:
                        path[temp] = path[current] + 1
                        # print(f"temp={temp} path[temp]={path[temp]}")
                        if temp == endWord:
                            return path[temp]
                        q.append(temp)
            pos += 1
        return 0

if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
