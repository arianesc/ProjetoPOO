import json 

class Arquivo:

	# def criar(nome, dado):
	# 	arquivo = open(f'{nome}', 'w')
	# 	arquivo.write(dado)
	# 	arquivo.close()
	
	
	def adicionar_dados(nome, dado):
		with open(nome) as fp:
			listObj = json.load(fp)
		listObj.append(dado)
		with open(nome, 'w') as json_file:
		    json.dump(listObj, json_file, 
		                        indent=4,  
		                        separators=(',',': '))

	
	def ler(nome):
		with open(nome) as f:
			myjson = json.load(f)
		return myjson 

	def deletar_dado(nome, dado):
		with open(nome, 'r') as f:
			my_list = json.load(f)
			for idx, obj in enumerate(my_list):
				if obj['id'] == dado.id:
					my_list.pop(idx)
		
		with open(nome, 'w') as f:
			f.write(json.dumps(my_list, indent=2))