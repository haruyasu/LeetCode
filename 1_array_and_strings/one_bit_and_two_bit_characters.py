class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = 0
        for i in reversed(range(len(bits) - 1)):
            if bits[i] == 0:
                break
            parity ^= bits[i]
        return parity == 0

bits = [1, 0, 0]
print(Solution().isOneBitCharacter(bits))
# True

bits = [1, 1, 1, 0]
print(Solution().isOneBitCharacter(bits))
# False
