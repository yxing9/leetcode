# 733. Flood Fill
# dfs
# bfs 0


# me and lc
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(i, j):
            if i in range(r) and j in range(c) and image[i][j] == ogColor:
            # if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != ogColor:
            #     return
                image[i][j] = newColor
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
            
        r = len(image)
        c = len(image[0])
        ogColor = image[sr][sc]
        
        if ogColor != newColor: # avoid infinite loop if newColor is the same as ogColor
            dfs(sr, sc)
        
        return image
# Runtime: 136 ms, faster than 5.36%



# a little refactor
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(i, j):
            # if i in range(r) and j in range(c) and image[i][j] == ogColor:
            if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != ogColor:
                return
            image[i][j] = newColor
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        r = len(image)
        c = len(image[0])
        ogColor = image[sr][sc]
        
        if ogColor != newColor: # avoid infinite loop if newColor is the same as ogColor
            dfs(sr, sc)
        
        return image
# Runtime: 76 ms, faster than 68.53%



# -----------------------------------
# forget about writing two functions instead of nested functions
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ogColor = image[sr][sc]
        if ogColor != newColor:
            self.dfs(image, sr, sc, ogColor, newColor)
        return image
    
    def dfs(self, image, r, c, ogColor):
        if r in range(len(image)) and c in range(len(image[0])) and image[r][c] == ogColor:
            image[r][c] = newColor
            self.dfs(image, r-1, c, ogColor, newColor)
            self.dfs(image, r+1, c, ogColor, newColor)
            self.dfs(image, r, c-1, ogColor, newColor)
            self.dfs(image, r, c+1, ogColor, newColor)
# TypeError: dfs() takes 5 positional arguments but 6 were given




'''

edge case

when newColor == ogColor
[[0,0,0],[0,1,1]]
1
1
1

'''