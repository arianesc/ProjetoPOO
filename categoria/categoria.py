class Categoria:
	def __init__(self, id, nome):
		self._id = id
		self._nome = nome

	def __str__(self):
		return f"{self.id} - {self.nome}"