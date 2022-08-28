from usuario.usuario import Usuario
from arquivo import Arquivo
from crud import Crud

class NUsuario:
	id = 0
	usuarios = []

	@classmethod
	def inserir(cls, nome, senha):
		cls.id += 1 
		obj = Usuario(cls.id, nome, senha)  # cria objeto 
		dados = {"id":obj.id,
						 "nome":obj.nome,
						 "senha":obj.senha
						} # cria dict com os dados que vão para o arquivo
		Crud.criar(obj, cls.usuarios, dados, "usuarios.txt") # adiciona usuario na lista e no arquivo
		return True
	
	@classmethod
	def listar_usuarios(cls):
		return cls.usuarios
		
	@classmethod
	def pesquisar(cls, usuario_id):
		return Crud.pesquisar(usuario_id, cls.usuarios)
	
	@classmethod
	def excluir(cls, usuario):
		Crud.deletar(usuario, cls.usuarios, "usuarios.txt")
	
	@classmethod
	def autenticar(cls, nome, senha):
		for user in cls.usuarios: # percorre a lista de usuarios
			if user.nome == nome and user.senha == senha: # verifica se os dados são iguais aos de algum usuario do banco
				return user
		return False
		
	
	@classmethod
	def recarregar_usuarios_do_banco(cls):
		id = 0
		usuarios_json = Arquivo.ler("usuarios.txt")
		for usuario in usuarios_json:
			usuario_existe = cls.pesquisar(usuario["id"])
			if usuario_existe is None:
				novo_usuario = Usuario(usuario["id"], usuario["nome"], usuario["senha"])
				cls.usuarios.append(novo_usuario)
		
			if usuario["id"] > id:
				id = usuario["id"]
		cls.id = id


	
	@classmethod
	def publicacoes_curtidas(cls, usuario):
		pass