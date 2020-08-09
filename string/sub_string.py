# https://leetcode-cn.com/problems/palindromic-substrings

def countSubstrings(self, s: str) -> int:
    # 中心扩展法
    def extend_substring(s: str, start: int, end: int) -> int:
        cnt_tmp = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            cnt_tmp += 1
        return cnt_tmp

    cnt = 0
    for i in range(len(s)):
        cnt += extend_substring(s, i, i) # 奇数长度
        cnt += extend_substring(s, i, i + 1) # 偶数长度

    return cnt