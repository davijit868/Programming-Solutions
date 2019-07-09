def combination(index, data, i):
    if(index == r): 
        for j in range(r): 
            print(data[j], end = " ") 
        print(" ") 
        return
    if(i >= n): 
        return
    data[index] = arr[i]
    combination(index + 1, data, i + 1)
    combination(index, data, i + 1) 

def call_combination():
    data = list(range(r)) 
    combinationUtil( 0, data, 0) 
  

arr = [10, 20, 30, 40, 50] 
  
r = 3
n = len(arr) 
call_combination() 
