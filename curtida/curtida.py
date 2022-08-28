class Curtida:
	def __init__(self, id, publicacao, quem_curtiu_id):
		self.id = id
		self.publicacao = publicacao
		self.quem_curtiu_id = quem_curtiu_id

	def __str__(self):
		return f"{self.id} - {self.publicacao}"