from curtida.curtida import Curtida
from crud import Crud
from arquivo import Arquivo
from publicacao.Npublicacao import NPublicacao
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
	def listar_curtidas_de_uma_publicacao(cls, pub):
		curtidas = []
		for curtida in cls.curtidas:
			if pub.id == curtida.publicacao:
				curtidas.append(curtida)
		
		return curtidas
		
	@classmethod
	def curtidas_de_um_usuario(cls, usuario):
		curtidas = []
		for curtida in cls.curtidas:
			if curtida.quem_curtiu_id == usuario.id:
				curtidas.append(curtida)
		return curtidas
			
		
	@classmethod
	def pesquisar(cls, obj_id):
		return Crud.pesquisar(obj_id, cls.curtidas)
	
	@classmethod
	def verificar_curtida(cls, pub, usuario_logado):
		for curtida in cls.curtidas:
			if curtida.publicacao == pub.id and curtida.quem_curtiu_id == usuario_logado.id:
				return False
		return True

	
	@classmethod
	def recarregar_curtidas_do_banco(cls):
		id = 0
		curtidas_json = Arquivo.ler("curtidas.txt")
		for curtida in curtidas_json:
			curtida_existe = cls.pesquisar(curtida["id"])
			if curtida_existe is None:
				nova_curtida = Curtida(curtida["id"], curtida["publicacao"], curtida["quem_curtiu_id"])
				cls.curtidas.append(nova_curtida)
			if curtida["id"] > id:
				id = curtida["id"]
		cls.id = id
