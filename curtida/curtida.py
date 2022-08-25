class Curtida:
	def __init__(self, id, publicacao, quem_curtiu_id):
		self._id = id
		self._publicacao = publicacao
		self._quem_curtiu_id = quem_curtiu_id

	def __str__(self):
		return f"{self.id} - {self.publicacao}"