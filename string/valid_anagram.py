from typing import List, Dict

# 方法一：统计每个字符的出现次数（哈希表）
def isAnagram1(s: str, t: str) -> bool:
    def get_char_cnt(s: str) -> Dict[str, int]:
        char_cnt = {}
        for c in s:
            if c not in char_cnt:
                char_cnt[c] = 1
            else:
                char_cnt[c] += 1
        return char_cnt

    s_cnt = get_char_cnt(s)
    t_cnt = get_char_cnt(t)
    if len(s_cnt) == len(t_cnt):
        for c, cnt in s_cnt.items():
            if t_cnt.get(c, 0) != cnt:
                return False
        return True
    else:
        return False

# 方法二：整形数组
def isAnagram2(s: str, t: str) -> bool:
    def get_char_cnt(s: str) -> List[int]:
        char_cnt = [0] * 26
        for c in s:
            char_cnt[ord(c) - 97] += 1
        return char_cnt

    s_cnt = get_char_cnt(s)
    t_cnt = get_char_cnt(t)

    if s_cnt == t_cnt:
        return True
    else:
        return False

