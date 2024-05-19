# Amstrong number
import math
num = int(input("Enter a number to check it is amstrong or not:"))
digit = int(input("Enter the digit of input no:"))
sum = 0
multi = 1
temp = num

while(num > 0):
  rem = num % 10
  sum = sum + math.pow(rem,digit)
  num = num//10
  
if(temp == sum):
     print("The no is amstrong no")
else:
     print("The no is not amstrong no")         