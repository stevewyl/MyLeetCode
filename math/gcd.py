# 辗转相除法，缺点：大数取模慢
def gcd_v1(a, b):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    return gcd_v1(big % small, small)

# 更相减损法，缺点：运算次数多
def gcd_v2(a, b):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    return gcd_v1(big - small, small)

# 移位运算 -> 为啥更慢了？
def gcd_v3(a, b):
    if a == b:
        return a
    if (a & 1) == 0 and (b & 1) == 0:
        return gcd_v3(a >> 1, b >> 1) << 1
    elif (a & 1) == 0 and (b & 1) != 0:
        return gcd_v3(a >> 1, b)
    elif (a & 1) != 0 and (b & 1) == 0:
        return gcd_v3(a, b >> 1)
    else:
        big = max(a, b)
        small = min(a, b)
        return gcd_v3(big - small, small)

if __name__ == "__main__":
    from IPython import get_ipython
    ipython = get_ipython()

    a = 12213478324
    b = 213123

    ipython.magic("%timeit gcd_v1(a, b)") # 4.2us
    ipython.magic("%timeit gcd_v2(a, b)") # 4.66us
    ipython.magic("%timeit gcd_v3(a, b)") # 25.9us