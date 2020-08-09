def reverseVowels(s: str) -> str:
    left = 0
    right = len(s) - 1
    s_list = list(s)
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    while left < right:
        s_left = s_list[left]
        s_right = s_list[right]
        while s_left not in vowels and left < right:
            left += 1
            s_left = s_list[left]
        while s_right not in vowels and left < right:
            right -= 1
            s_right = s_list[right]
        s_list[left] = s_right
        s_list[right] = s_left
        left += 1
        right -= 1
    return "".join(s_list)

if __name__ == "__main__":
    s = "leetcode"
    rs = "leotcede"
    assert rs == reverseVowels(s)
