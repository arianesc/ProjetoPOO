from curtida.curtida import Curtida

class NCurtida:
	curtidas = []
	
	@classmethod
	def curtir(cls, publicacao, quem_curtiu_id):
		cls.id += 1
		obj = Curtida(cls.id, publicacao, quem_curtiu_id)
		dados = {"id": cls.id, "publicacao": publicacao, "quem_curtiu_id": quem_curtiu_id}
		Crud.criar(obj, cls.curtidas, dados, "curtidas.txt")
		return True


	@classmethod
	def listar_curtidas():
		pass
