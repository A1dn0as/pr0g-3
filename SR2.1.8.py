A = 0
B = 0
C = 0
symbol = '* '


def tab(A, B, C):
    return int(((A and B) == (B and C)) or (C or A))


first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(length)
print('*   A   *   B   *   C   *   f   *')
print(length)
print(line)
print(length)
A = 0
B = 0
C = 1
first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)
A = 0
B = 1
C = 0

first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)

A = 0
B = 1
C = 1
first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)
A = 1
B = 0
C = 0
first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)
A = 1
B = 0
C = 1
first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)

A = 1
B = 1
C = 0
first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)

A = 1
B = 1
C = 1
first = tab(A, B, C)
line = (symbol+ '  ' + str(A)+ '   '+ symbol + '  ' + str(B) + '   ' + symbol + "  " + str(C)+'   ' + symbol +'  '+ str(first)+"   "+symbol)
length =(len(line)-17)* symbol
print(line)
print(length)
