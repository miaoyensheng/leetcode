# Given N, count the number of ways to express N as sum of 1, 3, 4.

def NumberFactor(n):
    if n == 0 or n == 1 or n == 2 :
        return 1
    elif n < 0 :
        return 0
    else:
        num1 = NumberFactor(n-1)
        num2 = NumberFactor(n-3)
        num3 = NumberFactor(n-4)

        return num1+num2+num3

print(NumberFactor(5))