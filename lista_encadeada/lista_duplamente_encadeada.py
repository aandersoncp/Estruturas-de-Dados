class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None
    
    def mostrar_no(self):
        print(self.valor)

class ListaDuplamenteEncadeado:
    
    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        if self.primeiro == None:
            print("Lista vazia.")
            return True
        return False
    
    def inserir(self, valor):
        no = No(valor)
        if self.lista_vazia() != True:
            temp = self.primeiro
            no.proximo = temp
            temp.anterior = no
        self.primeiro = no

    def buscar(self, valor):
        if self.lista_vazia():
            return
        atual = self.primeiro
        while atual != None and atual.valor != valor:
            atual = atual.proximo
        return atual

    def excluir(self, valor):
        if self.lista_vazia():
            return
        
        no = self.buscar(valor)
        if no == self.primeiro:
            self.primeiro.proximo.anterior = None
            self.primeiro = self.primeiro.proximo
        elif no != None:
            if no.proximo != None:
                no.proximo.anterior = no.anterior
            no.anterior.proximo = no.proximo
    
    def imprimir(self):
        if self.lista_vazia():
            return
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
        print("---")

lista = ListaDuplamenteEncadeado()
lista.inserir(2)
lista.inserir(3)
lista.inserir(5)
lista.imprimir()
lista.excluir(3)
lista.imprimir()