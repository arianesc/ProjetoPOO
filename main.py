# from usuario.usuario import Usuario
from usuario.Nusuario import NUsuario

class Program:
	usuario_autenticado = None
	
	def main():
		Program.atualizar_dados()
		
		if Program.usuario_autenticado is None:
			print("--- Bem-vindx! ---")
			print()
			op = 0
			while op != 99:
				try:
					op = Program.menu()
					if op == 1: Program.login()
					if op == 2 : Program.cadastrar_usuario()
				except Exception as erro:
							print(erro)
		else:
			Program.main_usuario()
	
	
	
	
	def menu():
		print("----- MENU -----")
		print("  01 - Login")
		print("  02 - Cadastro")
		print("Opção: ", end="")
		return int(input())

	
	
	def atualizar_dados():
		NUsuario.recarregar_usuarios_do_banco()
		
	
	""" USUARIO"""
	
	def login():
		print("Nome:")
		nome = input()
		print("Senha:")
		senha = input()
		aut = NUsuario.autenticar(nome, senha)
		
		if aut is False:
			print(f"{nome} não cadastrado")
			return
		
		print(f"Bem vindx {nome}")
		Program.usuario_autenticado = aut
		
		return Program.main_usuario()
	
	
	
	
	def cadastrar_usuario():
		print("-- INSIRA SEUS DADOS PARA CADASTRO --")
		nome = input("Nome: ")
		senha = input("Senha: ")
		NUsuario.cadastrar_usuario(nome, senha)
		# return Program.listar_usuarios()
	
	# def listar_usuarios():
	# 	print("-- LISTA DE USUARIOS --")
	# 	lista = NUsuario.listar_usuarios()
	# 	for usuario in lista:
	# 		print(f"{usuario} - {usuario['nome']}")

	
	
	def excluir_usuario():
		usuario = Program.usuario_autenticado		
		NUsuario.excluir(usuario)
		print(f"{usuario.nome} foi deletado")
		Program.usuario_autenticado = None
		# excluir usuario do arquivo
		return Program.main()
		
	
	
	def logout():
		Program.usuario_autenticado = None
		return Program.main()
		
	
	
	def main_usuario():
		op = 0
		while op != 99:
			try:
				op = Program.menu_usuario()
				if op == 1: Program.excluir_usuario()
				if op == 2: Program.logout()

			except Exception as erro:
						print(erro)
		pass

	# def main_visitante():
	# 	pass
		
	# """MENUS"""
	# def menu():
	# 	pass

	
	
	def menu_usuario():
		print("----- MENU DO USUARIO -----")
		print("  01 - excluir conta")
		print("  02 - logout")

		print("Opção: ", end="")
		return int(input())

	# def menu_visitante():
	# 	pass

	
	# """CATEGORIA"""
	# def categoria_inserir():
	# 	pass

	# def categoria_atualizar():
	# 	pass

	# def categoria_listar():
	# 	pass

	# def categoria_excluir():
	# 	pass

	
	# """PUBLICACAO"""
	# def publicacao_inserir():
	# 	pass
	
	# def publicacao_atualizar():
	# 	pass
	
	# def publicacao_listar():
	# 	pass
	
	# def publicacao_excluir():
	# 	pass

	# def curtir_publicacao():
	# 	pass




if __name__ == "__main__":
  Program.main()