from usuario.usuario import Usuario
from arquivo import Arquivo

class NUsuario:
	id = 0
	usuarios = []

	@classmethod
	def cadastrar_usuario(cls, nome, senha):
		cls.id += 1
		# criar usuario
		usuario = Usuario(cls.id, nome, senha) 
		cls.usuarios.append(usuario)
		# cadastrar no arquivo
		dados = {"id":usuario.id,
						 "nome":usuario.nome,
						 "senha":usuario.senha
						}
		
		Arquivo.adicionar_dados("usuarios.txt", dados)
		return True

	
	@classmethod
	def listar_usuarios(cls):
		return cls.usuarios

	@classmethod
	def recarregar_usuarios_do_banco(cls):
		id = 0
		usuarios_json = Arquivo.ler("usuarios.txt")
		for usuario in usuarios_json:
			usuario_existe = cls.buscar_usuario(usuario["id"])
			if usuario_existe is None:
				novo_usuario = Usuario(usuario["id"], usuario["nome"], usuario["senha"])
				cls.usuarios.append(novo_usuario)
		
			if usuario["id"] > id:
				id = usuario["id"]
		cls.id = id
		

	
	@classmethod
	def buscar_usuario(cls, usuario_id):
		for obj in cls.usuarios:
			 if obj.id == usuario_id:
				 return obj
		return
	
	
	@classmethod
	def excluir(cls, usuario):
		atual = cls.buscar_usuario(usuario.id)
		cls.usuarios.remove(atual)
		Arquivo.deletar_dado("usuarios.txt", usuario)

	@classmethod
	def autenticar(cls, nome, senha):
		for user in cls.usuarios:
			if user.nome == nome and user.senha == senha:
				return user
		return False
		
	
	@classmethod
	def publicacoes_curtidas(cls, usuario):
		pass

