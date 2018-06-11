class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        li = [0, 0]
        for i in moves:
            if i == "R":
                li[1] += 1
            elif i == "L":
                li[1] -= 1
            elif i == "U":
                li[0] += 1
            elif i == "D":
                li[0] -= 1
        if li[0] == 0 and li[1] == 0:
            return True
        else:
            return False

moves = "UD"
print(Solution().judgeCircle(moves))
# true

moves = "LL"
print(Solution().judgeCircle(moves))
# false
