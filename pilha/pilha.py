
import numpy as np

class Pilha:

	def __init__(self, tamanho):
		self.tamanho = tamanho
		self.topo = -1
		self.valores = np.empty(self.tamanho, dtype=int)

	def pilha_cheia(self):
		if self.topo == self.tamanho:
			return True
		return False

	def pilha_vazia(self):
		if self.topo == -1:
			return True
		return False

	def inserir(self, valor):
		if self.pilha_cheia():
			return
		else:
			self.topo += 1
			self.valores[self.topo] = valor

	def remover(self):
		if self.pilha_vazia():
			return
		else:
			self.topo -= 1

	def imprimir(self):
		if self.pilha_vazia():
			return
		else:
			for i in range(self.topo + 1):
				print(self.valores[i])
			print("---")


pilha = Pilha(5)
pilha.inserir(1)
pilha.inserir(3)
pilha.inserir(0)
pilha.inserir(10)
pilha.imprimir()
pilha.remover()
pilha.imprimir()
pilha.remover()
pilha.imprimir()






