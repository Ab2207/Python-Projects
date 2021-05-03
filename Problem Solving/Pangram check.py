"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""


def checkIfPangram( sentence):

    chars = "abcdefghijklmnopqrstuvwxyz"

    for c in chars:
        if c not in sentence:
            return False
    return True

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram("leetcode"))