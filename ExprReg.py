import re 
lista = ['adadfa nelsonboche@gmail.com.gt','nelson1@hotmail.com.edu','nelson.com',
            'nelson@boche.com.gt']
#patron = r'[a-zA-Z]+@[a-zA-Z]+(.[a-zA-Z])+'
patron = r'\w+@\w+(\.[a-zA-Z]+)+$'


p = re.compile(patron)
m = p.search(lista[0])
print(m.group())

def evaluar(lista, patron):
    p = re.compile(patron)
    
    for i in range(len(lista)):
        m = p.search(lista[i])
        if m:
            print("▲ ",m.group())
        #else:
        #    print("▼ ",m.group())

evaluar(lista,patron)
