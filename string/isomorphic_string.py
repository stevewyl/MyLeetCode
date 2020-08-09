def isIsomorphic(s: str, t: str) -> bool:
    char_pos_s = {}
    char_pos_t = {}
    for i in range(len(s)):
        if char_pos_s.get(s[i], -1) != char_pos_t.get(t[i], -1):
            return False
        char_pos_s[s[i]] = i
        char_pos_t[t[i]] = i
    return True

if __name__ == "__main__":
    s = "paper"
    t = "title"
    assert isIsomorphic(s, t) == True