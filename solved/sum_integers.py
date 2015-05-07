import sys

sumx = 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
   sumx += int(test)
test_cases.close()

print(sumx)
