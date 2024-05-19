# Perfect Number

num = int(input("Enter a number to check it is perfect or not:"))
sum = 0

for i in range(1,num):
    if num % i == 0:
     sum = sum + i
     
     
   
   
if(sum == num):
       print("The no is perfect")
else:
       print("The no is not perfect")
