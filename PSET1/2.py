'''
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print:
'Number of times bob occurs is: 2'
'''

s = 'azcbobobegghakl'
bob = 'bob'
numberOfBobs = 0
pos = 0

for pos in range(len(s)-2):
    if s[pos:pos+3] == 'bob':
        numberOfBobs = numberOfBobs + 1
print "Number of times bob occurs: %i" % numberOfBobs
