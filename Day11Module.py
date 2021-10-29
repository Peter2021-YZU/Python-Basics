class ClassTime(object):
    def __init__(self, hour=0, minutes=0, seconds=0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def setTime(self, h, m, s):
        if h < 0 or h >= 24:
            self.hour = 0
        else:
            self.hour = h
        if m < 0 or m >= 60:
            self.minutes = 0
        else:
            self.minutes = m
        if s < 0 or s >= 60:
            self.seconds = 0
        else:
            self.seconds = s

    def printUniversal(self):
        print('{:02}'.format(self.hour), ':', '{:02}'.format(self.minutes), ':', '{:02}'.format(self.seconds))

    def printStandard(self):
        if self.hour == 12 or self.hour == 0:
            self.hour = 12
        else:
            self.hour = self.hour % 12
        if self.hour < 12:
            AMorPM = 'PM'
        else:
            AMorPM = 'AM'
        print(self.hour, ":", '{:02}'.format(self.minutes), ":", '{:02}'.format(self.seconds), AMorPM)
