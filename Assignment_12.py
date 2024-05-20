# Map function

def square(num):
    return num**2


numbers = [1,2,3,4,5]

ans =list(map(square,numbers))

print(ans)

# Using Lambda function

ans1 = list(map(lambda a:a*a,numbers))
print(ans1)