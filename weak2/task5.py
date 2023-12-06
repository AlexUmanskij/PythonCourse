
def lesenka(n, k = 0):
    if n == 0:
        return 1
    ans = 0

    for i in range(k + 1, n + 1):
        ans += lesenka(n - i, i)
    return ans

print(lesenka(7))