from curtida.curtida import Curtida
from crud import Crud
class NCurtida:
	id = 0
	curtidas = []
	
	@classmethod
	def curtir(cls, publicacao, quem_curtiu_id):
		cls.id += 1
		obj = Curtida(cls.id, publicacao.id, quem_curtiu_id)
		dados = {"id": cls.id, "publicacao": publicacao.id, "quem_curtiu_id": quem_curtiu_id}
		Crud.criar(obj, cls.curtidas, dados, "curtidas.txt")
		return True

	@classmethod
	def listar_curtidas_de_uma_publicacao(pub):
		curtidas = []
		for curtida in cls.curtidas:
			if pub.id == curtida.publicacao:
				curtidas.append(curtida)
		
		return curtidas

	@classmethod
	def pesquisar(pub):
		
