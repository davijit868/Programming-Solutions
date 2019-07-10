def combinationUtil(index, data, i):
    if(index == r): 
        for j in range(r): 
            print(data[j], end = " ") 
        print(" ") 
        return
    if(i >= n): 
        return
    data[index] = arr[i]
    combinationUtil(index + 1, data, i + 1)
    combinationUtil(index, data, i + 1) 

arr = [10, 20, 30, 40, 50] 
r = 3
n = len(arr) 
data = list(range(r)) 
combinationUtil( 0, data, 0) 
