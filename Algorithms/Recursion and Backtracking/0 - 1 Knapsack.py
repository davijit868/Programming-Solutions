'''
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0/?track=md-dp&batchId=144

'''

def knapsack(value, weight, N, W):
    if N <= 0 or W <= 0:
        return 0
    if weight[-1] <= W:
        return max((value[-1] + knapsack(value[:-1], weight[:-1], N-1, W-weight[-1])), \
        knapsack(value[:-1], weight[:-1], N-1, W))
    else:
        return knapsack(value[:-1], weight[:-1], N-1, W)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        W = int(input())
        value = list(map(int, input().split()))
        weight = list(map(int, input().split()))
        max_val = knapsack(value, weight, N, W)
        print(max_val)
