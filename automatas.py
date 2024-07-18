import sys

# DEFINIENDO EL AUTÓMATA

class Automata:
    transiciones: ()
    estados: []
    finales: []
    alfabeto:[]
    inicial:''
    estado_actual = ''; 
    
    def __init__(self,inicial, finales, transiciones,estados,alfabeto):
        self.inicial = inicial;
        self.finales = finales; 
        self.transiciones = transiciones; 
        self.estados = estados; 
        self.alfabeto = alfabeto; 

    def siguiente_estado(automata,estado,entrada):
        for i in range(len(automata.transiciones)):
            if estado == automata.transiciones[i][0] and entrada == automata.transiciones[i][1]:
                #return transciciones[i][2]
                return (automata.transiciones[i][2])
    
    def valida_palabra(automata, estado_actual,palabra):
        longitud = len(palabra)
        for i in range(longitud):
            try:
                band = automata.alfabeto.index(palabra[i])
            except ValueError:
                print("Entrada: ", palabra[i],  "no pertenece al Alfabeto")
            if estado_actual == '':
                estado_actual = inicial;
            #realiza el movimiento de estados
            estado_actual = automata.siguiente_estado(estado_actual,palabra[i])
        return estado_actual
        
#llamada a la clase               
transiciones= [['q1','a','q2'],
                ['q2','b','q5'],
                ['q3','a','q3'],
                ['q4','b','q2'],
                ['q5','b','q1']]
estados= ['q0','q1','q2','q3','q4']
finales= ['q0','q1']
alfabeto=['a','b']
inicial="q1"

#creación de instancia
automata = Automata(inicial, finales, transiciones,estados,alfabeto)
#print(automata.siguiente_estado('q2','a'))
try:
    finales.index(automata.valida_palabra(inicial,'abba'))
    print("Palabra válida")
except ValueError:
    print ("Palabra no aceptada")

