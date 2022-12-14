import json 

class Arquivo:
	def adicionar_dados(nome, dado):
		with open(nome) as arquivo:
			listObj = json.load(arquivo)
		listObj.append(dado)
		with open(nome, 'w') as json_file:
		    json.dump(listObj,
									json_file,
		              indent=4,  
		              separators=(',',': '))
	
	def ler(nome):
		with open(nome) as f:
			myjson = json.load(f)
		return myjson 

	def deletar_dado(nome, dado):
		with open(nome, 'r') as arquivo:
			my_list = json.load(arquivo)
			for idx, obj in enumerate(my_list):
				if obj['id'] == dado.id:
					my_list.pop(idx)
		
		with open(nome, 'w') as arquivo:
			arquivo.write(json.dumps(my_list, indent=2))