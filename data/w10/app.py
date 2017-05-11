import sys
sys.path.append("./w10")
import alldef

a=3
b=2

add = alldef.addend (a,b)   #加運算
minus = alldef.minus (a,b) #減運算
tines  = alldef. tines (a,b)    #乘運算
divided = alldef.divided (a,b)  #除運算

print('加運算=', add)
print('減運算=', minus)
print('乘運算=', tines)
print('除運算=', divided)