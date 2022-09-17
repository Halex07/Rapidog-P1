from colas.nodo import Nodo


class Cola:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def empty(self):
        return self.primero == None

    def push(self, ingrediente):
        if self.empty():
            self.primero = self.ultimo = Nodo(ingrediente)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(ingrediente)


    def mostrar(self):
        aux = self.primero

        if self.empty():
            print("No hay pedidos pendientes en HotDog Rapidog")
        else:
            while aux != None:

                if(aux.ingrediente == 'Salchicha'):
                    tiempo = 2
  
                if(aux.ingrediente == 'Chorizo'):
                    tiempo = 3
                if(aux.ingrediente == 'Salami'):
                    tiempo = 1.5
                if(aux.ingrediente == 'Longaniza'):
                    tiempo = 4
                if(aux.ingrediente == 'Costilla'):
                    tiempo = 6
                print("HotDog de ", aux.ingrediente, '  ', tiempo, " min", "\n")
                aux = aux.siguiente
                
                
            
                      
            
    def first(self):
        aux = self.primero
        if self.empty():
            print("No existen ordenes pendientes en cola")
        else:
            if aux.ingrediente == 'Salchicha':
                    tiempo = 2  
            print("HotDog de ", aux.ingrediente, tiempo, "min")

            if aux.ingrediente == 'Chorizo':
                    tiempo = 3  
            print("HotDog de ", aux.ingrediente, tiempo, "min")

    def pop(self):
        if self.empty():
            print("No existen ordenes  en  cola...")
        else:
            self.primero = self.primero.siguiente
            input("Orden entregado con exito...")
