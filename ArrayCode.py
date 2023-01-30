# достает значение используя код
def GetValueWithCode(array,code): # переделать
	try:
		value = array
		for i in code:
			value = value[i]

		return value
	except:
		print("Значение кода " + str(code) + " - не существует")

def index(array):
	result = {}
	num = 0
	for i in array:
		result[str(num)]=i
		num = num + 1
	return result

def Branches(MyDict):
	for i in MyDict:
		val = MyDict[i]
		if isinstance(val,list):
			NewDict = index(val)
			MyDict[i]=NewDict
	return MyDict

def GoOnLevel(MyDict):
	NewDict = {}
	for i in MyDict:
		value = MyDict[i]

		if True != isinstance(value,dict) and True != isinstance(value,list):# НУЖНО ДРУГОЕ
			NewDict[i]=value
		else:
			for n in value:
				NewDict[i+n] = value[n]
	return NewDict

# команда создающая код
# возвращает словарь
def CreateCode(array):
	MainDict = index(array)
	bebra = True
	while (bebra):
		a = Branches(MainDict)
		a = GoOnLevel(a)
		if a == MainDict:
			bebra = False
		MainDict = a

CreateCode(a)







