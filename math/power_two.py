def solution1(n):
    temp = 1
    while temp <= n:
        if temp == n:
            return True
        temp = temp * 2
    return False

def solution2(n):
    temp = 1
    while temp <= n:
        if temp == n:
            return True
        temp = temp << 1
    return False

if __name__ == "__main__":
    from IPython import get_ipython
    ipython = get_ipython()

    nl = [1232184, 128]
    for n in nl:
        print(f"n = {n}")
        ipython.magic("%timeit solution1(n)")
        ipython.magic("%timeit solution2(n)")
