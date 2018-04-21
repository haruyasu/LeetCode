class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]

        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m = len(choices)
            n = len(result)
            result += [result[i % n] for i in range(n, m * n)]

            for i in range(m * n):
                result[i] = choices[int(i / n)] + result[i]

        return result


print(Solution().letterCombinations("23"))