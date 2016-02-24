"""
Problem 2: Counting 'bob's

Assume `s` is a string of lower case characters.

Write a program that prints the number of times the string `'bob'` occurs in
`s`. For example, if `s = 'azcbobobegghakl'`, then your program should print:
`Number of times bob occurs is: 2`
"""


numberOfBobs = 0
for pos in range(len(s)-2):
    if s[pos:pos+3] == 'bob':
        numberOfBobs += 1
print "Number of times bob occurs: %i" % numberOfBobs
