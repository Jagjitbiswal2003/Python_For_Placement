# Loop

# Syntax 

# for variable in iterable:
   # code block to be executed
   
# while condition:
    # code block to be executed
    
# Factorial calculation:

num = int(input("Enter the number to find the factorial:"))
multi = 1

for i in range(1,num+1):
     multi = multi * i
     i=i+1
print(multi)
     