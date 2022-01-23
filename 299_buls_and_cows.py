# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"

# O(n)
# bulls + cows = same collection of digits
from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCt = Counter(secret)
        guessCt = Counter(guess)
        bulls, cows = 0, 0
        for x in secretCt:
            if x in guessCt:
                cows += min(guessCt[x], secretCt[x])
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        cows -= bulls
        return f"{bulls}A{cows}B"
