#factorial of a number using recursion.


def recur_factorial(n):
  if n == 1:
    return n
  else:
    return n * recur_factorial(n - 1)


num = 2
#check the num is negative
if num < 0:
  print("sorry,the factorial does     not exist for negative number")
elif num == 0:
  print("the factorial of 0 is 1")
else:
  print("the   factorial of", num, "is", recur_factorial(num))
