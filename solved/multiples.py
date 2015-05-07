import sys
test_cases = open(sys.argv[1], 'r')
temp=x=n=it=fim=0
line = []
for test in test_cases:
    line = test.split(',')
    if (line[0]!='' and line[0]!='\n'):
        x = int(line[0])
        n = int(line[1])
        if (n<0):
            n = n*(-1)
        fim = n**2
        it = fim*(-1)
        while(it<=fim):
            temp = it*n
            if (n == 0 or temp > x and temp != 0):
                print(temp)
                break
            elif (x==n):
                print(n)
                break
            it+=1
test_cases.close()
