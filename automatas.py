# Autómata

# Q = {q0,q1,q2,q3} conjunto de estados
# F = {q3}Estados Finales
# Lenguaje inicie en 0, termine en 1
estado = 'q0'
entrada =''
estado_final ="q3"
palabra = '0010101001'
transciciones = [
    ['q0','1','q2'],
    ['q0','0','q1'],
    ['q1','1','q3'],
    ['q1','0','q1'],
    ['q3','0','q1'],
    ['q3','1','q3']
]
# for i in range(len(palabra)):
#     print("#"+str(i)+"-"+palabra[i])
    
def buscar_transicion(estado,entrada, transciciones):
    newEstado = ""
    for i in range(len(transciciones)):
        if estado == transciciones[i][0] and entrada == transciciones[i][1]:
            return transciciones[i][2]
        # else:
        #     return "No existe transcisión para esta Entrada/Estado"

for i in range(len(palabra)):
    entrada = palabra[i]
    estado  =buscar_transicion(estado,entrada,transciciones)

if (estado == estado_final):
    print("Palabra Aceptada =)")
else:
    print("Palabra Rechazada =(")
#print("Estado:" +estado +  " - Entrada:" +  entrada)
