'''

Problem: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
Solution: https://ide.geeksforgeeks.org/0KMKAdwsZf

'''

def subset_sum(arr, l, s):
    if s == 0: return True
    if l <= 0: return False
    if arr[l-1] > s: return subset_sum(arr, l-1, s) 
    return subset_sum(arr, l-1, s) or subset_sum(arr, l-1, s-arr[l-1])

if __name__ == '__main__':
    s = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    if subset_sum(arr, l, s):
        print(True)
    else:
        print(False)
