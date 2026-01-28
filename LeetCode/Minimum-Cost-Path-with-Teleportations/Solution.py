inf = float('inf')
dp = [[inf] * n for _ in range(m)]
dp[0][0] = 0
def update():
    for i in range(m):
        for j in range(n):
            temp = grid[i][j] + min(
                dp[i-1][j] if i else inf, 
                dp[i][j-1] if j else inf
            )
            if temp < dp[i][j]: dp[i][j] = temp
update()