def convert(s:str, numRows:int)->str:
    if numRows == 1 or numRows >= len(s):
        return s 
    
    rows = [''] * numRows 
    current_row = 0 
    direction = 1 

    for char in s:
        rows[current_row] += char
        current_row += direction 
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1 

    return "".join(rows) 


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))