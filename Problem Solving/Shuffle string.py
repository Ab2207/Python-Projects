"""
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.
"""


def restoreString(s, indices):

    shuffled_s = [" " for i in range(len(s))]

    for idx, char in enumerate(s):
        shuffled_s[indices[idx]] = char
    return "".join(shuffled_s)

print(restoreString("aaiougrt", [4,0,2,6,7,3,1,5]))