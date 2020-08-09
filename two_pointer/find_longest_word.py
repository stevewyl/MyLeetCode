from typing import List

def findLongestWord(s: str, d: List[str]) -> str:
    def check_sub_string(s1: str, s2: str) -> bool:
        p1 = 0
        p2 = 0
        l1 = len(s1)
        l2 = len(s2)
        while p1 <= l1 or p2 <= l2:
            if p2 == l2:
                return True
            if p1 == l1:
                return False
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1

    results = [w for w in d if check_sub_string(s, w)]
    if results:
        return sorted(results, key=lambda x: (-len(x), x[0]))[0]
    else:
        return ""

if __name__ == "__main__":
    s = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]
    assert findLongestWord(s, d) == "apple"