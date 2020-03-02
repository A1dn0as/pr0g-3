T = 1
F = 0
symbol = '* '
AB = '*   A   *   B   *  A|B  *'
first = (symbol+'F '+symbol+ 'F '+symbol+ 'T '+ symbol)
second = (symbol+'F '+symbol+ 'T '+symbol+ 'F '+ symbol)
third = (symbol+'T '+symbol+ 'F '+symbol+ 'F '+ symbol)
fourth = (symbol+'T '+symbol+ 'T '+symbol+ 'F '+ symbol)
length = (len(first)-1)* symbol

print(length)
print(AB)
print(length)
print(*first)
print(length)
print(*second)
print(length)
print(*third)
print(length)
print(*fourth)
print(length)