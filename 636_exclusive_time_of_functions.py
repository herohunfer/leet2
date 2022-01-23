class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        current = 0
        for log in logs:
            log = log.split(":")
            if log[1] == "start":
                if stack:
                    res[stack[-1]] += int(log[2]) - current
                stack.append(int(log[0]))
                current = int(log[2])
            else:
                prog = stack.pop()
                res[prog] += int(log[2]) - current + 1
                current = int(log[2]) + 1
        return res
