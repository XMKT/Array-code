# достает значение используя код [0,1,2] или "012"
def GetValueWithCode(array,code): 
	try:
		value = array
		for i in code:
			value = value[int(i)]

		return value
	except:
		print("Значение кода " + str(code) + " - не существует")

# меняет местами ключи и значения
def InvertDict(CodeDict):
	key = list(CodeDict.keys())
	val = list(CodeDict.values())
	NewDict = {}
	for i in key:
		NewDict[CodeDict[i]]=i
	return NewDict

# создает словарь из массива( используеться для расчленения детей ;) )
def index(array):
	result = {}
	num = 0
	for i in array:
		result[str(num)]=i
		num = num + 1
	return result

# функция которая ищет детей уровня(ответвления)
# принимает и возвращает словарь
def Branches(MyDict):
	for i in MyDict:
		val = MyDict[i]
		if isinstance(val,list):
			NewDict = index(val)
			MyDict[i]=NewDict
	return MyDict

# функция помогает перебраться на следующий уровень, изменяя ключи, добавляя в них ссылку на родителя
# принимает и возвращает словарь
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

# функция создающая код
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
	return MainDict
