def validPalindrome(s: str) -> bool:

    def isPalindroms(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return isPalindroms(s, left, right - 1) or isPalindroms(s, left + 1 , right)
        left += 1
        right -= 1
    return True

