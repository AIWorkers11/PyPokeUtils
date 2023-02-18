class Ability():
    def __init__(
        self,
        name:str = "",
		effect:str = "",):
        self.__name:str = name
        self.__effect:str = effect
    def getEffctData(self):
        return [
            self.__name,
            self.__effect
		]

class Status():
    def __init__(self,
        values = [0,0,0,0,0,0]
    ):
        self.__values = []
        print(len(values))
        for i in range(6):
            if len(values)-1 < i:
                self.__values.append(0)
            else:
                self.__values.append(values[i])
    def getStatusValue(self,index=None):
        if index == None:
            return self.__values
        else:
            return self.__values[index]
