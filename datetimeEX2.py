#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      jd0919889
#
# Created:     31/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def createDate():
    global currentDate
    currentDate = datetime.datetime.now()
    global month
    month = currentDate.month
    global day
    day - currentDate.day
    global year
    year = currentDate.year
    global hour
    hour = currentDate.hour
    global minute
    minute = currentDate.minute
    global date
    date = str(year) + "." + str(month) + "." + str(day) + "." + str(hour) + "." + str(minute) + "."

def getName():
    global name
    name = input("What is your name?: ")

createDate()
getName
print("CaveGame-%s-%s" % (name, date))