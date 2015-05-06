import sys

def check(number):
	if number < 0 or number > 100: return "This program is for humans"
	elif number >= 0 and number <= 2: return "Still in Mama's arms"
	elif number >= 3 and number <= 4: return "Preschool Maniac"
	elif number >= 5 and number <= 11: return "Elementary school"
	elif number >= 12 and number <= 14: return "Middle school"
	elif number >= 15 and number <= 18: return "High school"
	elif number >= 19 and number <= 22: return "College"
	elif number >= 23 and number <= 65: return "Working for the man"
	elif number >= 66 and number <= 100: return "The Golden Years"
	
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(check(int(test)))
test_cases.close()
