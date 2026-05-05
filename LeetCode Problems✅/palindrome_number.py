def palindrome():
    x = 10
    temp = x
    n = 0
    while temp > 0:
        r = temp % 10
        n = n * 10 + r
        temp = temp // 10
    return x == n
print(palindrome())    