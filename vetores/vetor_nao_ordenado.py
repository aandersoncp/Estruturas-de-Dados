import numpy as np

class Vetor:
	
	def __init__(self, tamanho):
		self.tamanho = tamanho
		self.ultimaPosicao = -1
		self.valores = np.empty(self.tamanho, dtype=int)

	def imprimir(self):
		if self.ultimaPosicao == -1:
			print("Vetor está vazio!")
		else:
			for i in range(self.ultimaPosicao + 1):
				print(self.valores[i])
			print("--")

	def inserir(self, valor):
		if self.ultimaPosicao < self.tamanho - 1:
			self.ultimaPosicao += 1 
			self.valores[self.ultimaPosicao] = valor 
		else:
			print("Vetor cheio!")

	def buscar(self, valor):
		for i in range(self.ultimaPosicao + 1):
			if self.valores[i] == valor:
				return i
		return -1

	def excluir(self, valor):
		posicao = self.buscar(valor)
		if posicao > -1 and posicao != self.ultimaPosicao - 1:
			for i in range(posicao, self.ultimaPosicao):
				self.valores[i] = self.valores[i + 1] 
		self.ultimaPosicao -= 1


vetor = Vetor(5)
vetor.imprimir()
vetor.inserir(4)
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
vetor.imprimir()		