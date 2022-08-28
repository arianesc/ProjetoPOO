from publicacao.publicacao import Publicacao
from crud import Crud
from arquivo import Arquivo

class NPublicacao:
	id = 0
	publicacoes = []
	
	@classmethod
	def inserir(cls, titulo, texto, categoria, autor_id):
		cls.id += 1
		obj = Publicacao(cls.id, titulo, texto, categoria, autor_id)
		dados = {"id": cls.id, "titulo": titulo, "texto": texto, "categoria": categoria, "autor_id":autor_id}
		Crud.criar(obj, cls.publicacoes, dados, "publicacoes.txt")
		return True

	
	@classmethod
	def pesquisar(cls, obj_id):
		return Crud.pesquisar(obj_id, cls.publicacoes)
	
	@classmethod
	def atualizar(self, p):
		pass

	@classmethod
	def listar(cls):
		return cls.publicacoes

	@classmethod
	def listar_minhas_publicacoes(cls, autor_id):
		minhas_publicacoes = []
		for pub in cls.listar():
			if pub.autor_id == autor_id:
				minhas_publicacoes.append(pub)
		return minhas_publicacoes
			
				
	@classmethod			
	def listar_publicacoes_dos_outros(cls, autor_id):
		publicacoes = []
		for pub in cls.listar():
			if pub.autor_id != autor_id:
				publicacoes.append(pub)
		return publicacoes
			
		
	@classmethod
	def excluir(cls, obj):
		Crud.deletar(obj, cls.publicacoes, "publicacoes.txt")

	@classmethod
	def recarregar_publicacoes_do_banco(cls):
		id = 0
		publicacoes_json = Arquivo.ler("publicacoes.txt")
		
		for publicacao in publicacoes_json:
			publicacao_existe = cls.pesquisar(publicacao["id"])
			if publicacao_existe is None:
				nova_publicacao = Publicacao(publicacao["id"], publicacao["titulo"], publicacao["texto"], publicacao["categoria"], publicacao["autor_id"])
				
				cls.publicacoes.append(nova_publicacao)
			
			if publicacao["id"] > id:
				id = publicacao["id"]
		cls.id = id

	@classmethod
	def listar_curtidas(cls, p):
		pass