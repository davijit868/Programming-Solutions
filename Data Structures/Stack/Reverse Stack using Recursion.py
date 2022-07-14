'''

Reverse a stack using recursion
https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/

'''

stack = list(map(int, input().split()))

def insert_bottom(stack, num):
    if not stack:
        stack.append(num)
    else:
        temp = stack.pop()
        insert_bottom(stack, num)
        stack.append(temp)
    return stack

def recursion(stack):
    if stack: 
        temp = stack.pop()
        stack = recursion(stack)
        stack = insert_bottom(stack, temp)
    return stack

print(recursion(stack))

        
            
