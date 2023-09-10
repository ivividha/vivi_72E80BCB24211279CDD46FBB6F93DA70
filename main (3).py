#leap year
def checkLeap(year):
#checking if the given year is leap year
if((year % 400 == 0) and
   (year % 100 != 0) or
   (year % 4 == 0 )):
  print("the given year is a leap           year");
#else it is not a leap year
else:
  print("the given year is not a            leap year");
#taking input year from user
year = int(input("enter the                           number"))
#printing result
checkLeap(year)