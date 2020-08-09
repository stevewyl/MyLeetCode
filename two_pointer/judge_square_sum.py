def judgeSquareSum(c: int) -> bool:
    if c < 0:
        return False
    left = 0
    right = int(c ** 0.5)
    while left <= right:
        squre_sum = left ** 2 + right ** 2
        if squre_sum > c:
            right -= 1
        elif squre_sum < c:
            left += 1
        else:
            print(left, right)
            return True
    return False

if __name__ == "__main__":
    target = 100000000
    print(judgeSquareSum(target))
