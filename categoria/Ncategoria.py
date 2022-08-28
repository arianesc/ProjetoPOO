from categoria.categoria import Categoria
from arquivo import Arquivo
from crud import Crud

class NCategoria:
	id = 0
	categorias = []
	
	@classmethod
	def inserir(cls, nome):
		cls.id += 1
		obj = Categoria(cls.id, nome)  # cria objeto
		dados = {"id": 1, "nome": nome} # cria dict para o banco
		Crud.criar(obj, cls.categorias, dados,  "categorias.txt")  # adiciona objeto na lista e no banco
		return True

	@classmethod
	def listar(cls):
		return cls.categorias 
		
	@classmethod
	def pesquisar(cls, c_id):
		return Crud.pesquisar(c_id, cls.categorias) 

	@classmethod
	def excluir(cls, obj):
		Crud.deletar(obj, cls.categorias, "categorias.txt")
		
	@classmethod
	def recarregar_categorias_do_banco(cls):
		id = 0 # zera variavel id
		categorias_json = Arquivo.ler("categorias.txt") # lê arquivo categorias
		for categoria in categorias_json:
			categoria_existe = cls.pesquisar(categoria["id"]) # pega o id do banco e verifica se já existe um objeto com esse id
			if categoria_existe is None: # Se não existir, cria novo objeto com os dados
				nova_categoria = Categoria(categoria["id"], categoria["nome"])
				cls.categorias.append(nova_categoria)
			if categoria["id"] > id:  # logica para pegar o proximo id
				id = categoria["id"]
		cls.id = id