# НЕ ИЗМЕНЯЕМЫЕ (Не Сохраняемые)
y='abc'
z=y  #y и z ссылаются на один объект 'abc', но изменить его по ссылке не смогут
z.upper() # не сработает, т.к неизменяемый объект
w=z.upper() # срабоатает
print(y, id(y))
print(z, id(z))
print(w, id(w))
p='abc'
o='abc'
print(p, id(p))
print(o, id(o))
print(w, id(w))
D= [1,2,3,4,5,6,7,8,9]
for i in D:
    print(i, id)
def fff():
    return
fff()