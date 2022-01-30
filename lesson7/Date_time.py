
import datetime

class Clock:

    def __init__(self):
        self.clock=datetime.datetime.now().strftime("%H:%M:%S")

class Calendar:
    def __init__(self):
        self.calendar=datetime.date.today().strftime('%d/%m/%y')

class Date_Time(Clock, Calendar):
    def __init__(self):
        Clock.__init__(self)
        Calendar.__init__(self)
        print(((self.calendar)),(self.clock))
        print(str(self.calendar),str(self.clock))

obj=Date_Time()
