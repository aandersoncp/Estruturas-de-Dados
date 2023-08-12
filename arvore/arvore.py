class No:

    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.esquerda = None
        self.direita = None
    
    def mostrar_no(self):
        print(self.valor)

class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
    
    def arvore_vazia(self):
        if self.raiz == None:
            print("Arvore vazia!")
            return True
        return False

    def inserir(self, valor):
        no = No(valor)
        if self.arvore_vazia():
            self.raiz = no
            print("---")
        else:
            atual = self.raiz
            while atual != None:
                temp = atual
                if atual.valor >= valor:
                    atual = atual.esquerda
                else:
                    atual = atual.direita
            no.pai = temp
            if temp.valor >= valor:
                temp.esquerda = no 
            else:  
                temp.direita = no 
    
    def percorrer_em_ordem(self, no):
        if no == None:
            return
        atual = no
        self.percorrer_em_ordem(no.esquerda)
        no.mostrar_no()
        self.percorrer_em_ordem(no.direita)

    def imprimir(self):
        self.percorrer_em_ordem(self.raiz)
        print("---")

    def minimo(self):
        if self.arvore_vazia():
            return
        atual = self.raiz
        while atual.esquerda != None:
            atual = atual.esquerda
        print(f"Valor mínimo: {atual.valor}")
        print("---")
    
    def maximo(self):
        if self.arvore_vazia():
            return
        atual = self.raiz
        while atual.direita != None:
            atual = atual.direita
        print(f"Valor máximo: {atual.valor}")
        print("---")
    





tree = ArvoreBinariaBusca()
tree.inserir(10)
tree.inserir(5)
tree.imprimir()
tree.inserir(4)
tree.imprimir()
tree.inserir(12)
tree.inserir(6)
tree.imprimir()
tree.minimo()
tree.maximo()