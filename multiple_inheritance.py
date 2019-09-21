""" 
Following code is inspired from:
    
    https://www.python-course.eu/python3_multiple_inheritance.php

"""
class Clock:
    """ 
    Class to set time of a clock. Parameters must be:
    
        hours: 0-23
        minutes, seconds: 0-60

    """

    def __init__(self, hours:int, minutes:int, seconds:int=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, val):
        if val>23 or val<0 or type(val) != int:
            raise TypeError("Hours must be in range 0-23 "
                          + "and of type int")
        else:
            self.__hours = val
    
    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, val):
        if val > 60 or val < 0 or type(val) != int:
            raise TypeError("Minutes must be in range 0-60 "
                          + "and of type int")
        else:
            self.__minutes = val

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, val):
        if val>60 or val<0 or type(val) != int:
            raise TypeError("Seconds must be in range 0-60 "
                          + "and of type int")
        else:
            self.__seconds = val

    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes}, {self.seconds})"

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def tick(self):
        """
        This method let's the clock tick. That means that for each
        time that the function tick is being called, the clock passes
        by one second.

        e.g.:

        >>> Clock(12,31,32).tick()
        >>> Clock(12,31,33


        >>> time = Clock(23, 59, 59)
        >>> print(time.tick())
        00:00:00

        """

        if self.seconds != 59:
           self.seconds += 1
        else:
            self.seconds = 0

            if self.minutes != 59:
                self.minutes += 1
            else:
                self.minutes = 0

                if self.hours != 23:
                    self.hours += 1
                else:
                    self.hours = 0


class Calendar:
    """
    Class to set date in format year.month.day. Parameters must be:

        year: >=0
        month: 0-12
        day: <=31 on month (1, 3, 5, 7, 8, 10, 12)
             <=29 on month 2 for leap years
             <=28 on month 2 for not leap years
             <=30 on the remaining months
    
    When calendar object is on str() format it will show the date
    in the corresponding date_syle. To change the date_style you
    have to change the class attribute.e.g.:
    >>> Calendar.date_style = "American"
    """
    date_style = "British"

    def __init__(self, year:int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if type(val)==int:
            self.__year = val
        else:
            raise TypeError("Year must be of type int")

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, val):
        if type(val)==int and val>=0 and val<=12:
            self.__month = val
        else:
            raise TypeError("Month must be in range 0-12 and "
                          + "of type int")

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, val):
        thirty_one_days = (1, 3, 5, 7, 8, 10, 12)
        if type(val)==int:
            # checks if the month has 31 days or 30 days or less
            if self.month in thirty_one_days and val<=31:
                self.__day = val
            else:
                # checks if month is a february and if year is a
                # leap year
                if self.month==2 and self.isleap(self.year):
                    if val <= 29:
                        self.__day = val
                    else:
                        raise TypeError("Day must be 29 or less on "
                                      + "leap years")
                else:
                    if val < 30:
                        self.__day = val
                    else:
                        raise TypeError("Day mus be 30 or less")
        else:
            raise TypeError("Day must be of type int")

    def __repr__(self):
        return f"Calendar({self.year}, {self.month}, {self.day})"

    def __str__(self):
        if Calendar.date_style == "British":
            return f"{self.day}.{self.month}.{self.year}"
        elif Calendar.date_style == "American":
            return f"{self.month}.{self.day}.{self.year}"
        else:
            return f"{self.year}.{self.month}.{self.day}"


    @staticmethod
    def isleap(year):
        """
        This method checks if the parameter year is a leap year or
        not.

        e.g.:
        >>> date = Calendar(1984, 4, 17)
        >>> date.isleap(date.year)
        True
        >>> Calendar.isleap(date.year)
        True
        >>> date2 = Calendar(2041, 2, 1)
        >>> date2.isleap(date2.year)
        False
        >>> Calendar.isleap(date2.year)
        False
        """
        if year%4 == 0:
            return True
        elif year%100 == 0:
            return False
        elif year%400 == 0:
            return True
        else:
            return False

    def advance(self):
       """
       This menthod when called, advances the calendar by one day.

       e.g.:

       >>> date = Calendar(2000, 2, 28)
       >>> date.advance()
       >>> date.advance()
       >>> date
       Calendar(2000, 3, 1)
       >>> date = Calendar(1999, 12, 31)
       >>> date.advance()
       >>> date
       Calendar(2000, 1, 1)
       """
       try:
           self.day += 1
       except TypeError:
           try:
               self.month += 1
               self.day = 1
           except TypeError:
               self.year += 1
               self.month = 1
               self.day = 1


class CalendarClock(Calendar, Clock):
    def __init__(self, year, month, day, hours, minutes, seconds=0):
        Calendar.__init__(self, year, month, day)
        Clock.__init__(self, hours, minutes, seconds)

    def __repr__(self):
        return f"CalendarClock({self.year}, {self.month}, " \
             + f"{self.day}, {self.hours}, {self.minutes}, " \
             + f"{self.seconds})"

    def __str__(self):
        return f"{Clock.__str__(self)} {Calendar.__str__(self)}"

    def tick(self):
        """
        This method compbines the method Clock.tick(self) with 
        Calendar.advance(self). When a CalendarClock instance
        has hours, minutes, seconds set to 23,59,59, and the tick
        method gets called, the calander advances by one.

        e.g.:

        >>> time = CalendarClock(2000, 2, 28, 23, 59, 59)
        >>> time.tick()
        >>> time
        CalendarClock(2000, 2, 29, 0, 0, 0)
        >>> time = CalendarClock(1984, 4, 17, 14, 32)
        >>> time.tick()
        >>> time
        CalendarClock(1984, 4, 17, 14, 32, 1)
        """
        if Clock.__repr__(self) == 'Clock(23, 59, 59)':
            Clock.tick(self)
            Calendar.advance(self)
        else:
            Clock.tick(self)
