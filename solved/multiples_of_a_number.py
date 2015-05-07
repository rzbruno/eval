import sys
test_cases = open(sys.argv[1], 'r')
temp=x=n=it=0
line = []
for test in test_cases:
    line = test.split(',')
    if (line[0]!='' and line[0]!='\n'):
        x = int(line[0])
        n = int(line[1])
        it = 1
        while(True):
            temp = it*n
            if (n == 0 or temp > x and temp != 0):
                print(temp)
                break
            elif (x==n):
                print(n)
                break
            it+=1
test_cases.close()
