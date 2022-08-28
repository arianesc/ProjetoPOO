class Publicacao:
	def __init__(self, id, titulo, texto, categoria, autor_id):
		self.id = id
		self.titulo = titulo
		self.texto = texto
		self.categoria = categoria
		self.autor_id = autor_id

	def __str__(self):
		return f"{self.id}-{self.titulo}"

