# Given N, count the number of ways to express N as sum of 1, 3, 4.

def NumberFactor(n):
    if n == 0 or n == 1 or n == 2 :
        return 1
    elif n == 3 :
        return 2
    else:
        NumberFactor