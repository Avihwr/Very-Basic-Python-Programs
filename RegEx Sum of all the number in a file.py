import re

hand = open(r'D:\PythonProjects\test files\test.txt')
lst=list()
for line in hand:
    line = line.rstrip()
    ft = re.findall('[0-9]+',line)
    lst = lst + ft
print(lst)


sum=0
for s in lst:
    sum = sum + int(s)
print(sum)