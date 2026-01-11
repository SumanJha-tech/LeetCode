class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        maxArea = 0
        
        for r in range(rows):
            # Build histogram for this row
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                curHeight = heights[i] if i < cols else 0
                
                while stack and curHeight < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                
                stack.append(i)
        
        return maxArea
