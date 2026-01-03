class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        # For n = 1
        same = 6   # patterns like ABA
        diff = 6   # patterns like ABC
        
        for _ in range(2, n + 1):
            new_same = (same * 3 + diff * 2) % MOD
            new_diff = (same * 2 + diff * 2) % MOD
            same, diff = new_same, new_diff
        
        return (same + diff) % MOD
