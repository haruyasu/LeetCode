class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        is_prime = [True] * n
        num = int(n / 2)
        for i in range(3, n, 2):
            if i * i >= n:
                break
            
            if not is_prime[i]:
                continue
            
            for j in range(i * i, n, 2 * i):
                if not is_prime[j]:
                    continue
                
                num -= 1
                is_prime[j] = False
        return num

n = 10
print(Solution().countPrimes(n))
# 4
