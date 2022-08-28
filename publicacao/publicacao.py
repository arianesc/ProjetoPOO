class Publicacao:
	def __init__(self, id, titulo, texto, categoria):
		self.id = id
		self.titulo = titulo
		self.texto = texto
		self.categoria = categoria

	def __str__(self):
		return f"{self.id}-{self.titulo}"

