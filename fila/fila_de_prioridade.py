import numpy as np

# Fila de priodidade de mínimo
# Fila : [5, 3, 1]
# Enfileirar(2): [5, 3, 2, 1]
# Desenfileirar: [5, 3, 2]  

class FilaPrioridade:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.numero_de_elementos = 0
        self.valores = np.empty(self.tamanho, dtype=int)
    
    def fila_vazia(self):
        return self.numero_de_elementos == 0
    
    def fila_cheia(self):
        return self.numero_de_elementos == self.tamanho
    
    def enfileirar(self, valor):
        if self.fila_cheia():
            print("Fila cheia!")
            return
        
        if self.numero_de_elementos == 0:
            self.valores[self.numero_de_elementos] = valor
            self.numero_de_elementos += 1
        else:
            x = self.numero_de_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_de_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('Fila vazia!')
            return

        valor = self.valores[self.numero_de_elementos - 1]
        self.numero_de_elementos -= 1
        return valor
    
    def imprimir(self):
        for i in range(self.numero_de_elementos):
            print(self.valores[i])
        print("---")

fila = FilaPrioridade(5)
fila.enfileirar(3)
fila.enfileirar(5)
fila.imprimir()
fila.enfileirar(2)
fila.imprimir()
fila.enfileirar(4)
fila.imprimir()
fila.desenfileirar()
fila.imprimir()
fila.enfileirar(1)
fila.imprimir()
fila.enfileirar(10)
fila.imprimir()