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

    def buscar(self, valor):
        atual = self.raiz
        while atual != None:
            if atual.valor > valor:
                atual = atual.esquerda
            elif atual.valor < valor:
                atual = atual.direita
            else: 
                return atual
        return atual

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

    def sucessor(self, valor):
        no = self.buscar(valor)
        if no != None:
            if no.direita != None:
                print(f"Sucessor de {valor}: {self.minimo(no.direita).valor}")
                return self.minimo(no.direita)
            else:
                temp = no.pai
                while temp != None and no == temp.direita:
                    no = temp
                    temp = temp.pai
                if temp != None:
                    print(f"Sucessor de {valor}: {temp.valor}")
                else:
                    print("Não possui sucessor!")
                return temp
    def antecessor(self, valor):
        no = self.buscar(valor)
        if no != None:
            if no.esquerda != None:
                print(f"Antecessor de {valor}: {self.maximo(no.esquerda).valor}")
                return self.maximo(no.esquerda)
            else:
                temp = no.pai
                while temp != None and no == temp.esquerda:
                    no = temp
                    temp = temp.pai
                if temp != None:
                    print(f"Antecessor de {valor}: {temp.valor}")
                else:
                    print("Não possui sucessor!")
                return temp              

    def minimo(self, no):
        if self.raiz == no and no == None:
            self.arvore_vazia()
            return
        atual = no
        while atual.esquerda != None:
            atual = atual.esquerda
        return atual
    
    def mostrar_minino(self):
        print(f"Valor mínimo: {self.minimo(self.raiz).valor}")
        print("---")
   
    def maximo(self, no):
        if self.raiz == no and no == None:
            self.arvore_vazia()
            return
        atual = no
        while atual.direita != None:
            atual = atual.direita
        return atual

    def mostrar_maximo(self):
        print(f"Valor máximo: {self.maximo(self.raiz).valor}")
        print("---")  

    def transplantar(self, substituido, substituto):
        if substituido.pai == None:
            self.raiz = substituto
        else:
            if substituido == substituido.pai.esquerda:
                substituido.pai.esquerda = substituto
            else:
                substituido.pai.direita = substituto
        if substituto != None:
            substituto.pai = substituido.pai
    
    def remover(self, valor):
        if self.arvore_vazia():
            return
        no = self.buscar(valor)
        if no != None:
            if no.esquerda == None:
                self.transplantar(no, no.direita)
            else:
                if no.direita == None:
                    self.transplantar(no, no.esquerda)
                else:
                    temp = self.minimo(no.direita)
                    if temp.pai != no:
                        self.transplantar(temp, temp.direita)
                        temp.direita = no.direita
                        temp.direita.pai = temp
                    self.transplantar(no, temp)
                    temp.esquerda = no.esquerda
                    temp.esquerda.pai = temp
                    

tree = ArvoreBinariaBusca()
tree.inserir(10)
tree.inserir(8)
tree.inserir(15)
tree.inserir(7)
tree.inserir(9)
tree.inserir(5)
tree.inserir(13)
tree.inserir(17)
tree.inserir(14)
tree.inserir(12)
tree.imprimir()
tree.remover(10)
