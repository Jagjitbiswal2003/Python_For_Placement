#Reduce function

from functools import reduce

def multi(m,n):
    return m*n

numbers = [1,2,3,4,5,6]
ans = reduce(multi,numbers)
print(ans)

#Using Lambda function

ans1 = reduce(lambda a,b:a*b,numbers)
print(ans1)