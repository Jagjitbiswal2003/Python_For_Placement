# Filter Function

def is_even(n):
    if n%2 == 0:
     return n
 
numbers = [1,2,3,4,5,6]
 
ans = filter(is_even,numbers)

print(list(ans)) 


# using Lambda function

ans1 = filter(lambda a:a%2==0,numbers)
print(list(ans1))
    