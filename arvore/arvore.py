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
        else:
            atual = self.raiz
            while atual != None:
                temp = atual
                if atual.valor >= valor:
                    atual = atual.esquerdo
                else:
                    atual = atual.direito
            no.pai = temp
            if temp.valor >= no:
                temp.esquerda = no 
            else:  
                temp.direita = no 
    
    def percorrer_em_ordem(self):
        atual = self.raiz
         
