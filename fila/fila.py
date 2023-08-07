import numpy as np 

class Fila:

	def __init__(self, tamanho):
		self.tamanho = tamanho
		self.head = -1
		self.tail = -1
		self.numero_elementos = 0
		self.valores = np.empty(self.tamanho, dtype=int)

	def fila_vazia(self):
		if self.numero_elementos == 0:
			return True
		return False

	def fila_cheia(self):
		if self.numero_elementos == self.tamanho:
			return True
		return False

	def imprimir(self):
		if self.head < self.tail:
			for i in range(self.tail, self.tamanho):
				print(self.valores[i])
			for i in range(self.head):
				print(self.valores[i])
		else:
			for i in range(self.tail, self.head + 1):
				print(self.valores[i])

	def inserir(self, valor):
