def longestPalindrome(s: str) -> int:
    def get_char_cnt(s: str):
        char_cnt = {}
        for c in s:
            if c not in char_cnt:
                char_cnt[c] = 1
            else:
                char_cnt[c] += 1
        return char_cnt

    char_cnt = get_char_cnt(s)
    length = 0
    for cnt in char_cnt.values():
        length += int(cnt / 2) * 2
    if length < len(s):
        length += 1
    return length
