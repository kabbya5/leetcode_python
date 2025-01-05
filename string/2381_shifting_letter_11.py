def shiftingLetters(s:str, shifts:list[list[int]])-> str:
    n = len(s)
    shift = [0] * (n+ 1)
 
    for start, end, direction in shifts:
        if direction == 1:
            shift[start] += 1
            shift[end + 1] -= 1
        else:
            shift[start] -= 1
            shift[end + 1] += 1
        print(shift)

    for i in range(1, n):
        shift[i] += shift[i -1]
        print(shift)
    
    result = []

    for i in range(n):
        new_char = chr(((ord(s[i]) -ord('a') + shift[i]) % 26) + ord('a'))
        result.append(new_char)

    return ''.join(result)

s = "dztz"
shifts = [[0,0,0],[1,1,1]]
print(shiftingLetters(s, shifts))