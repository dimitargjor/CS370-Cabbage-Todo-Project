import UtilFunctions
from datetime import datetime
from datetime import date
import Read


import ColorSelection

def prTest(skk): 
    print("\033[94m {}\033[00m" .format(skk))

prTest("Hello")
ColorSelection.prCyan("Hello")
ColorSelection.prGreen("Hello")
print (u'\u02E3')
print(u'\u00D7')
print("x")
"""
tempDate = "04/06/2022"   

today = date.today()

temp = today.strftime("%m/%d/%Y")
print (temp)
print (tempDate)

dns = datetime.strptime(temp, "%m/%d/%Y")
input = datetime.strptime(tempDate, "%m/%d/%Y")

if (dns > input):
    print ("Passed")
else:
    print ("Fail")

workbook = UtilFunctions.getWorkbook()

print (Read.read(workbook))

worksheet = workbook.active
statColumn = "c"
overdue = '\u2613'

todayDate = date.today()
todayString = todayDate.strftime("%m/%d/%Y")
today = datetime.strptime(todayString, "%m/%d/%Y")

for cell in worksheet["A"]:

    currRow = cell.row
    if currRow > 1:
        #print(currRow)
        parsedDate = datetime.strptime(cell.value, "%m/%d/%Y")

        if(parsedDate < today):

        # worksheet[statColumn + str(currRow)] = overdue
            print(worksheet["A" + str(currRow)].value)"""

