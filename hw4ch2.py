# 4. A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them.
# The moment of the first timestamp occurred before the moment of the second timestamp.
# (6, 1, 30, 6, 2, 10 result 40 sec.)


hours1 = int(input("Enter hours: "))
minutes1 = int(input("Enter minutes: "))
seconds1 = int(input("Enter seconds: "))
hours2 = int(input("Enter hours: "))
minutes2 = int(input("Enter minutes: "))
seconds2 = int(input("Enter seconds: "))


print("The result between first timestamp and second timestamp is "
      + str(((hours2 - hours1) * 36000) + ((minutes2 - minutes1) * 60) + (seconds2 - seconds1)) + " seconds.")