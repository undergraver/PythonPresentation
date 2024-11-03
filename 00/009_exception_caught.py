s1 = input("dividend:")
s2 = input("divisor:")

f1 = float(s1)
f2 = float(s2)

try:
    res = f1/f2
#except: # < we can use this method if don't want cathing the exception
except Exception as e:
       print("Exception caught:"+str(e))
       res = "Invalid input"

print("The result is:"+str(res))