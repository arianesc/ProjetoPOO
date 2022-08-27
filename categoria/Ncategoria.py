from categoria.categoria import Categoria
from arquivo import Arquivo

class NCategoria:
	id = 0
	categorias = []
	
	@classmethod
	def inserir(cls, nome):
		cls.id += 1
		# criar categoria
		c = Categoria(cls.id, nome)
		cls.categorias.append(c)
		# cadastrar no arquivo
		dados = {"id":c.id,
						 "nome":c.nome}
		Arquivo.adicionar_dados("categorias.txt", dados)
		return True

	
	@classmethod
	def recarregar_categorias_do_banco(cls):
		id = 0
		categorias_json = Arquivo.ler("categorias.txt")
		for categoria in categorias_json:
			categoria_existe = cls.pesquisar(categoria["id"])
			if categoria_existe is None:
				nova_categoria = Categoria(categoria["id"], categoria["nome"])
				cls.categorias.append(nova_categoria)
			if categoria["id"] > id:
				id = categoria["id"]
				
		cls.id = id

	
	@classmethod
	def listar(cls):
		return cls.categorias
		
	
	@classmethod
	def pesquisar(cls,c_id):
		for obj in cls.categorias:
			 if obj.id == c_id:
				 return obj
		return
		
	
	@classmethod
	def excluir(cls,c_id):
		atual = cls.pesquisar(c_id)
		cls.categorias.remove(atual)
		Arquivo.deletar_dado("categorias.txt", atual)
