class Publicacao:
	def __init__(self, id, titulo, texto):
		self._id = id
		self._titulo = titulo
		self._texto = texto

	def __str__(self):
		return f"{self.id}-{self.titulo}"

