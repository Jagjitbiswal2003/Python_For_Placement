# Prime numbers within a range:
# Write a program that prints all prime numbers between 1 and 100 using a for loop.

num = 2
while num < 100:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
    num += 1

  