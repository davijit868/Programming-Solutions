'''

Problem: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
Solution: https://ide.geeksforgeeks.org/1DrM1klLKE

'''

def subset_sum(arr, l, s):
    dp = [[False for i in range(s+1)] for j in range(l+1)]
    for i in range(l+1):
        dp[i][0] = True
    for i in range(1, l+1):
        for j in range(1, s+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[l][s]

if __name__ == '__main__':
    s = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    if subset_sum(arr, l, s):
        print(True)
    else:
        print(False)
