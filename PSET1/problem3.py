"""
Problem 3: Alphabetical Substrings

Assume `s` is a string of lower case characters.

Write a program that prints the longest substring of `s` in which the letters
occur in alphabetical order. For example, if `s = 'azcbobobegghakl'`,
then your program should print:
`Longest substring in alphabetical order is: beggh`

In the case of ties, print the first substring. For example, if `s = 'abcbcd'`,
then your program should print:
`Longest substring in alphabetical order is: abc`
"""


subS = ''
print "s = " + s
for x in range(len(s)-1):
    tmpS = s[x]
    for y in range(x+1, len(s)):
        if tmpS[-1] <= s[y]:
            tmpS = tmpS + s[y]
        else:
            break
    if len(tmpS) > len(subS):
        subS = tmpS
print "Longest substring in alphabetical order is: " + subS
