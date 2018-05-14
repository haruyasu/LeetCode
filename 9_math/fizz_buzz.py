class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                li.append("FizzBuzz")
            elif i % 3 == 0:
                li.append("Fizz")
            elif i % 5 == 0:
                li.append("Buzz")
            else:
                li.append(str(i))
        return li


n = 15
print(Solution().fizzBuzz(n))
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
