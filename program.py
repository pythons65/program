import index as id
import time as t
e = False
while e == False: 
  code = input("PY_RT > ")
  id.stru(code)
  array = code.split()
  if array[0] == code:
    pass  
  else:
    b = 0 # 4

    for i in range(0,len(array),1):
      try:
        a = float(array[i])# 5
    
        b = b + a# b = 4 + 5 
      except:
        a = array[i]   
    print(b)   
  t.sleep(1)  
