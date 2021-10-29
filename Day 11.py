from Day11Module import ClassTime




t = ClassTime()
# print the properties of my object
t.printUniversal() # 00 : 00 : 00
t.printStandard() # 12: 00 : 00 AM



t.setTime(13, 27, 6) # change the time
t.printUniversal() # 13 : 27 : 06
t.printStandard() # 1: 27 : 06 PM

t.setTime(99, 99, 99) # after attempting invalid settings, my object will ouput the initial values
t.printUniversal() # 00 : 00 : 00
t.printStandard() # 12: 00 : 00 AM
