import numpy as np
import math

class VetorOrdenado:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.ultimaPosicao = -1
        self.valores = np.empty(self.tamanho, dtype=int)

    def imprimir(self):
        if self.ultimaPosicao == -1:
            print("Vetor vazio!")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(self.valores[i])
            print("---")
    
    def buscar(self, valor):
        for i in range(self.tamanho + 1):
            if self.valores[i] == valor:
                return i 
        return -1
    
    def excluir(self, valor):
        posicao = self.buscar(valor)
        if posicao > -1 and posicao != self.ultimaPosicao - 1:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
        self.ultimaPosicao -= 1

    def buscar_posicao(self, valor):
        if self.ultimaPosicao == -1:
            return -1
        i = 0
        while i <= self.ultimaPosicao and self.valores[i] < valor:
            i += 1
        return i
    
    def inserir(self, valor):

        posicao = self.buscar_posicao(valor)

        if self.ultimaPosicao == self.tamanho:
            print("Vetor cheio")
        elif self.ultimaPosicao == -1:
            self.valores[0] = valor
            self.ultimaPosicao += 1
        else:
            for j in range(self.ultimaPosicao, posicao - 1, -1):
                self.valores[j + 1] = self.valores[j]
            self.valores[posicao] = valor
            self.ultimaPosicao += 1 

    """def busca_binaria(self, valor):
        inicio = 0
        fim = self.tamanho
        while inicio <= fim:
            meio = math.ceil((fim - inicio)/2)
            if self.valores[meio] == valor:
                return meio
            elif self.valores[meio] < valor:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1"""

            


vetor = VetorOrdenado(5)
vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(6)
vetor.inserir(7)
posicao = vetor.busca_binaria(2)
print(posicao)
"""vetor.imprimir()
vetor.inserir(3)
vetor.imprimir()
vetor.inserir(6)
vetor.inserir(5)
vetor.inserir(2)
vetor.imprimir()
vetor.excluir(6)
vetor.imprimir()"""
"""vetor.inserir(4)
vetor.imprimir()
vetor.inserir(3)
vetor.imprimir()
vetor.inserir(2)
vetor.imprimir()
vetor.inserir(5)
vetor.imprimir()
vetor.inserir(6)
vetor.imprimir()
vetor.inserir(0)
vetor.excluir(4)
vetor.imprimir()"""

#for j in range(2, - 2, -1):
#    print(j)