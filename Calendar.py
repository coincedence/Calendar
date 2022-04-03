from calendar import month


class MyCalendar:

    daysOfTheWeek = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday",  "Monday", "Tuesday", ]

    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
        self.dayOfTheWeekOffset = 0

        self.setTheNameOfTheDay()       


        

    def prev(self):
        if(self.day == 1):
            if(self.month == 3):
                if(self.year % 4 != 0):
                    self.day = 28
                else:
                    self.day = 29
            elif(self.month % 2 == 1):
                self.day = 30
            else:
                self.day = 31

            if(self.month != 1):
                self.month -= 1
            else:
                self.month = 12
                self.year -= 1
        else:
            self.day -= 1
        self.setTheNameOfTheDay()

    def next(self):
        if(self.month == 2):
            if(self.day == 28):
                if(self.year % 4 != 0):
                    self.day = 1
                    self.month += 1
                else:
                    self.day+= 1
            elif(self.day == 29):
                self.day = 1
                self.month += 1
        elif(self.month % 2 == 1):
            if(self.day == 31):
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        else:
                if(self.day == 30):
                    self.day = 1
                    if(self.month==12):
                        self.month = 1
                        self.year += 1
                    else:
                        self.month += 1
                else:
                    self.day += 1
        self.setTheNameOfTheDay();

    def setTheNameOfTheDay(self):
        dayOfTheWeekOffset = (self.year - 1992) * 365 + (self.year - 1992)//4
        for i in range(1, self.month):
            if(i % 2 == 1):
                dayOfTheWeekOffset += 31
            elif(i == 2):
                if(self.year % 4 != 0):
                    dayOfTheWeekOffset += 28
                else:
                    dayOfTheWeekOffset += 29
            else:
                dayOfTheWeekOffset += 30


        dayOfTheWeekOffset += self.day
        dayOfTheWeekOffset = dayOfTheWeekOffset % 7
        
        self.nameOfTheDay = self.daysOfTheWeek[dayOfTheWeekOffset]
        self.dayOfTheWeekOffset = dayOfTheWeekOffset

    def setDay(self, day:int):
        if(day>30):
            if(self.month %2 == 1):
                self.day = 31
            elif(self.month == 2):
                if(self.year %4 == 0):
                    self.day = 29
                else:
                    self.day = 28
            else:
                self.day = 30
        else:
            self.day = day
        self.setTheNameOfTheDay()

    def setToTheBegginingOfTheWeek(self):
        offset = self.dayOfTheWeekOffset - 5
        if(offset < 0):
            offset += 7

        
        for i in range(0, offset):
            self.prev()


    def print(self):
        print(self.nameOfTheDay + " " + str(self.day) + " " + str(self.month) + " "+ str(self.year))






