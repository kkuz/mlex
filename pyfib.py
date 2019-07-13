def getfib(n):
   if n < 2:
      return n
   else:
      return getfib(n-2) + getfib(n-1)

for i in range(11):
   print(getfib(i))