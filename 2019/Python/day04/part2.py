input = "128392-643281"
minNum, maxNum = input.split("-")



def hasTwoAdjacent(number):
	num = str(number)
	if num[0] == num[1] and num[1] != num[2]:
		return True
	if num[len(num)-1] == num[len(num)-2] and num[len(num)-2] != num[len(num)-3]:
		return True
	for i in range(1, len(num)-2):
		if num[i] == num[i+1]:
			if num[i] != num[i-1] and num[i] != num[i+2]:
				return True
	return False
	
def alwaysGoingUp(number):
	num = str(number)
	for i in range(0,len(num)-1):
		if int(num[i]) > int(num[i+1]):
			return False
	return True
		

def checkNum(num):
	if hasTwoAdjacent(num) and alwaysGoingUp(num):
		return True
	return False


howmany = 0

for numb in range(int(minNum),int(maxNum)):
	if checkNum(numb):
		howmany += 1
		
print(howmany)
	
