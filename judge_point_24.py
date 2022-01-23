# 3 3 8 8 -> 8/(3-8/3)


class Solution:
    def judgePoint24(self, cards) -> bool:
        def helper(vals):
            print(vals)
            if len(vals) == 1:
                return 24-1e-9 < vals[0] < 24+1e-9
            for i in range(len(vals)):
                for j in range(i+1, len(vals)):
                    newvals = vals[:i] + vals[i+1:j] + vals[j+1:]
                    if (helper(newvals + [vals[i]+vals[j]])
                        or helper(newvals + [vals[i]-vals[j]])
                        or helper(newvals + [vals[j]-vals[i]])
                        or helper(newvals + [vals[i]*vals[j]])
                        or (helper(newvals + [vals[i]/vals[j]]) if vals[j] else False)
                        or (helper(newvals + [vals[j]/vals[i]]) if vals[i] else False)
                    ):
                        return True
            return False
        return helper(cards)

if __name__ == "__main__":
    s = Solution()
    print(s.judgePoint24([1,2,1,2]))
