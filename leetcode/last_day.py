class Solution(object):
    def latestDayToCross(self, row, col, cells):
        move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def can_cross(i, j, visited):
            if i == row - 1:
                return True
            if i < 0 or i >= row or j < 0 or j >= col:
                return False
            if matrix[i][j] == 1 or (i, j) in visited:
                return False
            
            visited.add((i, j))
            for next_i, next_j in move:
                if can_cross(i + next_i, j + next_j, visited):
                    return True
            return False
        
        left, right = 0, len(cells)
        while left < right:
            mid = (left + right) // 2
            matrix = [[0 for _ in range(col)] for _ in range(row)]
            visited = set()
            for k in range(mid):
                r, c = cells[k]
                matrix[r - 1][c - 1] = 1
            
            can_cross_now = False
            for start_col in range(col):
                if matrix[0][start_col] == 0 and can_cross(0, start_col, visited):
                    can_cross_now = True
                    break
            
            if can_cross_now:
                left = mid + 1
            else:
                right = mid
        
        return left - 1 

s = Solution()
days = s.latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]])
print(days) 