# from usuario.usuario import Usuario
from usuario.Nusuario import NUsuario
from categoria.Ncategoria import NCategoria
from publicacao.Npublicacao import NPublicacao
from curtida.Ncurtida import NCurtida

"""
PENDENCIA:
- Excluir publicação
- Editar publicação
- Excluir curtida ?
- Listar publicações que eu curti
- Visão do visitante
"""

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
		NCategoria.recarregar_categorias_do_banco()		
		NPublicacao.recarregar_publicacoes_do_banco()
		NCurtida.recarregar_curtidas_do_banco()
	
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
		NUsuario.inserir(nome, senha)
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
				if op == 3: Program.categoria_inserir()
				if op == 4: Program.categoria_excluir()
				if op == 5: Program.categoria_listar()
				if op == 6: Program.publicacao_inserir()
				if op == 7: Program.main_publicacoes()

			except Exception as erro:
						print(erro)
		pass
	
	
	
	def menu_usuario():
		print("----- MENU DO USUARIO -----")
		print("  01 - excluir conta")
		print("  02 - logout")
		print("  03 - Adicionar categoria")
		print("  04 - Remover categoria ")
		print("  05 - Listar categorias")
		print("  06 - Adicionar publicacao")
		print("  07 - Listar publicacões")
		print("Opção: ", end="")
		return int(input())

	
	# """CATEGORIA"""
	
	"""CATEGORIA"""
	
	def categoria_inserir():
		nome = input("nome: ")
		NCategoria.inserir(nome)

	
	
	def categoria_listar():
		print("-- LISTA DE CATEGORIAS --")
		lista = NCategoria.listar()
		for c in lista:
			print(f"{c.id} - {c.nome}")
		

	
	
	def categoria_excluir():
		Program.categoria_listar()
		c_id = int(input("insira o id da cateoria que quer excluir: "))
		obj = NCategoria.pesquisar(c_id)
		NCategoria.excluir(obj)

	
	# """PUBLICACAO"""
	
	"""PUBLICACAO"""

	
	def publicacao_inserir():
		titulo = input("titulo: ")
		texto = input("texto: ")
		categoria = int(input("categoria: "))
		NPublicacao.inserir(titulo, texto, categoria, Program.usuario_autenticado.id)
	
	# def publicacao_atualizar():
	# 	pass
	
	
	def listar_publicacoes_dos_outros():
		lista = NPublicacao.listar_publicacoes_dos_outros(Program.usuario_autenticado.id)
		for pub in lista:
			print(f"{pub.id} - {pub.titulo}")
		Program.publicacao_pesquisar()

	
	def listar_minhas_publicacoes():
		lista = NPublicacao.listar_minhas_publicacoes(Program.usuario_autenticado.id)
		for pub in lista:
			print(f"{pub.id} - {pub.titulo}")
		Program.publicacao_pesquisar()

	
	def publicacao_pesquisar():
		p = int(input("Insira o ID de qual publicação deseja ler: "))
		pub = NPublicacao.pesquisar(p)
		if pub is not None:
			Program.ler_publicacao(pub)
		else:
			print("Publicação não encontrada")

	
	
	def ler_publicacao(pub):
		print(f"titulo: {pub.titulo}")
		print(f"texto: {pub.texto}")
		print(f"id: {pub.id}")
		print(f"autor_id: {pub.autor_id}")	
		curtidas = NCurtida.listar_curtidas_de_uma_publicacao(pub)
		qtd_curtidas = len(curtidas)
		print(f"Essa publicação tem {qtd_curtidas} curtidas!")
		Program.main_leitura_publicacoes(pub)

	
	def main_leitura_publicacoes(pub):
		op = 0
		while op != 99:
			try:
				op = Program.menu_leitura_publicacoes()
				if op == 1: Program.curtir_publicacao(pub)
				if op == 2: Program.main_publicacoes()
					
			except Exception as erro:
						print(erro)
		pass
	
	
	def menu_leitura_publicacoes():
		print("----- MENU DE PUBLICACOES -----")
		print("  01 - Curtir")
		print("  02 - Sair ")		
		print("Opção: ", end="")
		return int(input())

	
	def main_publicacoes():
		op = 0
		while op != 99:
			try:
				op = Program.menu_publicacoes()
				if op == 1: Program.listar_minhas_publicacoes()
				if op == 2: Program.listar_publicacoes_dos_outros()
				if op == 3: Program.main()

			except Exception as erro:
						print(erro)
		pass
	
	
	
	def menu_publicacoes():
		print("----- MENU DE PUBLICACOES -----")
		print("  01 - Minha publicações")
		print("  02 - Publicações dos outros")
		print("  03 - Voltar para o menu do usuario")
		
		print("Opção: ", end="")
		return int(input())
		
	# def publicacao_excluir():
	# 	pass

	
	def curtir_publicacao(pub):
		verificar = NCurtida.verificar_curtida(pub, Program.usuario_autenticado)
		if verificar is False:
			print("Você ja curtiu essa publicação")
		elif pub.autor_id == Program.usuario_autenticado.id:
			print("Você não pode curtir sua propria publicação")
		else:
			NCurtida.curtir(pub, Program.usuario_autenticado.id)
			

if __name__ == "__main__":
  Program.main()




	