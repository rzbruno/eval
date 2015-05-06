import sys

def calc(operator, a, b):
   if operator == '*': return a*b
   elif operator == '/': return a/b
   elif operator == '+': return a+b

#recursive (stack) evaluate expression
def prefix(expression):
   for token in expression:
      if token.isdigit():
         del expression[0]
         return int(token)
      elif token in '/ * +':
         del expression[0]
         first = prefix(expression)
         second = prefix(expression)
         return calc(token, first, second)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(prefix(test.split()))
test_cases.close()