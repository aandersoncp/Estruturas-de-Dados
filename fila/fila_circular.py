import numpy as np 

class FilaCircular:

	def __init__(self, tamanho):
		self.tamanho = tamanho
		self.inicio = 0
		self.fim = -1
		self.numero_elementos = 0
		self.valores = np.empty(self.tamanho, dtype=int)

	def fila_vazia(self):
		return self.numero_elementos == 0

	def fila_cheia(self):
		return self.numero_elementos == self.tamanho

	def imprimir(self):
		print(f"Início: {self.inicio}")
		print(f"Fim: {self.fim}")
		if self.inicio < self.fim:
			for i in range(self.inicio, self.fim + 1):
				print(self.valores[i])
		else:
			for i in range(self.inicio, self.tamanho):
				print(self.valores[i])
			for i in range(self.fim + 1):
				print(self.valores[i])
		print("---")

	def enfileirar(self, valor):
		if self.fila_cheia():
			print("Fila cheia!")
			return
		if self.fim == self.tamanho -1:
			self.fim = -1
		self.fim += 1 
		self.valores[self.fim] = valor
		self.numero_elementos += 1

	def desenfileirar(self):
		if self.fila_vazia():
			print("Fila vazia!")
			return
		temp = self.valores[self.inicio]
		self.inicio += 1
		if self.inicio == self.tamanho:
			self.inicio = 0
		self.numero_elementos -= 1
		return temp

fila = FilaCircular(5)
fila.enfileirar(9)
fila.enfileirar(5)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.enfileirar(6)
fila.imprimir()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.imprimir()
fila.enfileirar(10)
fila.enfileirar(13)
fila.enfileirar(14)
fila.imprimir()
