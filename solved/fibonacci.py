import sys

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print (str(f(int(test))))
test_cases.close()
