from collections import Counter

s="anagram"
t="nagaram"
def IsAnagram(s,t):
    if len(s)!=len(t):
        return False

    s_dict=Counter(s)
    t_dict=Counter(t)

    return s_dict==t_dict

print(IsAnagram(s,t))