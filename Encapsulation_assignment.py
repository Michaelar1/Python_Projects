# It seems to me that protected and private functions/attributes would best be served for values that would not normally be changed, like the date of something

class Timekeeping:
    def __init__(self):
        self._weekday = 'Saturday' #    set protected value of _weekday to 'Saturday'

obj = Timekeeping()
obj._weekday = 'Wednesday' #    change protected value of _weekday to 'Wednesday'
print(obj._weekday)

class todaysDate:
    def __init__(self):
        self.__date = 'March 18, 2023' #    This is a private value for today's date

    def getPrivate(self): 
        print(self.__date)

    def setPrivate(self, private):  #   This function can change the private value
        self.__date = private


obj = todaysDate()
obj.getPrivate()
obj.setPrivate('April 1, 2023')
obj.getPrivate()
