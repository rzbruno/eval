import sys

l = []

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
   l.append(int(test))
test_cases.close()

print(sum(l))
