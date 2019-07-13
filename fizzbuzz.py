#Approach 1
def checkX(denom):
   return lambda x : x % denom == 0 

mf3 = checkX(3)
mf5 = checkX(5)
numiter = 20
outtext3 = "fizz"
outtext5 = "buzz"

for i in range(1, numiter+1):
   outtext = ""
   if mf3(i) and mf5(i):
      outtext = outtext3 + outtext5
   elif mf3(i):
      outtext = outtext3
   elif mf5(i):
      outtext = outtext5
   print('Number ' + str(i) + " - " + outtext)

#Approach 2
def checkX2(denom, outtext):
   return lambda x: outtext if x % denom == 0 else ""

mf3 = checkX2(3, "fizz")
mf5 = checkX2(5, "buzz")

for i in range(1, numiter + 1):
   txt = mf3(i) + mf5(i)
   print(i if not txt else txt)
#   if not txt: print(i) 
#   else: print(txt)