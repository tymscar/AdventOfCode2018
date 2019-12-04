input = "128392-643281"
minNum, maxNum = input.split("-")



def hasTwoAdjacent(number):
	num = str(number)
	for i in range(0,len(num)-1):
		if num[i] == num[i+1]:
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
	
