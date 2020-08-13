def mySqrt(x: int) -> int:
    if x <= 1:
        return x
    left = 1
    right = x
    while left <= right:
        mid = int(left + (right - left) / 2)
        print(mid)
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        elif square > x:
            right = mid - 1
    return right

if __name__ == "__main__":
    x = 8
    mySqrt(x)
