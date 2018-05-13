class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq
        
    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq


for i in range(1, 10):
    print(Solution().countAndSay(i))
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221