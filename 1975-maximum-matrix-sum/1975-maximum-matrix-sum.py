class Solution(object):
    def maxMatrixSum(self, matrix):
        total_sum = 0
        neg_count = 0
        min_abs = float('inf')
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total_sum += abs_val
                min_abs = min(min_abs, abs_val)
        
        if neg_count % 2 == 1:
            total_sum -= 2 * min_abs
        
        return total_sum
