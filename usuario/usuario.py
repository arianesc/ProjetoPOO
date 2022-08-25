class Usuario:
	def __init__(self, id, nome, senha):
		self._id = id
		self._nome = nome
		self._senha = senha

	def __str__(self):
		return f"{self.id}-{self.nome}"

	

	