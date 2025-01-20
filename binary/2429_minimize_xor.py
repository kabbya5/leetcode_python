def minimizeXor( num1: int, num2: int) -> int:
  
  count1 = bin(num1).count('1');
  count2 = bin(num2).count('1')
  if count2 > count1:
    result = num1 
    for i in range(32):
      if(count1 == count2 ):
        break 
      if(result & (1 << i) == 0):
        retsult |= (1 << i)
        count+= 1 
        
    return result
    
  elif count2 < count1:
    result = num1 
    
    for i in range(32):
        if count1 == count2:
            break 
        if result & (1 << i):
            result &=~(1 << i) 
            count1 -= 1 
    return result 
    
  return num1
  
num1 = 3
num2 = 5

print(minimizeXor(num1, num2))