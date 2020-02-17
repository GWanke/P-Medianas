class Vertice():
	def __init__(self):
		 	self.indice = None
		 	self.x = None
		 	self.y = None
		 	self.demanda = None
		 	self.capacidade = None
	def __str__(self):
		return "indice: {} capacidade: {} x: {} y: {} demanda: {}".format(self.indice,self.capacidade,self.x,self.y,self.demanda)