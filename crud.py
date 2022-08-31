from arquivo import Arquivo

class Crud:
	
	@classmethod
	def criar(cls, obj, lista_do_objeto, dados, nome_do_arquivo):
		lista_do_objeto.append(obj)
		Arquivo.adicionar_dados(nome_do_arquivo, dados)
		return True
	
	
	@classmethod
	def deletar(cls, obj, lista_do_objeto, nome_do_arquivo):
		if obj is not None:
			lista_do_objeto.remove(obj)
			Arquivo.deletar_dado(nome_do_arquivo, obj)
			return
		print(f"Objeto {obj} não deletado")
		
	@classmethod
	def pesquisar(cls, obj_id, lista_do_objeto):
		for obj in lista_do_objeto:
			if obj.id == obj_id:
				return obj
		return