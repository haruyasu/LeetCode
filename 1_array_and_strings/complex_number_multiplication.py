class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ia = map(int, a[:-1].split("+"))
        rb, ib = map(int, b[:-1].split("+"))
        return "%d+%di" % (ra * rb - ia * ib, ra * ib + ia * rb)

a = "1+1i"
b = "1+1i"
print(Solution().complexNumberMultiply(a, b))
# "0+2i"

a = "1+-1i"
b = "1+-1i"
print(Solution().complexNumberMultiply(a, b))
# "0+-2i"
