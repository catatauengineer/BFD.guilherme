dicionario_vazio={}
 
 ### acessando itens
dicionario = {"nome" : "catatau",
              "idade" : 21 
  




 }
# print(dicionario.get("nome")) # pegando item pra o diocnario

#add itens oa diconario
dicionario["profissão"] = "desnvolvedor"
print(dicionario)

# uptade
dicionario.uptade({"Idade" : 25})
print(dicionario)
 # usando o pop na biblioteca
dicionario.pop("Idade")
dicionario.popitem() # apaga o ultimo item
 # usando o clear no dicionario
dicionario.clear()
print(dicionario)
 # usando del no dicionario
del dicionario[" nome da chave"]
nome_funcionarios=["fred","joao","maria"]
diconario_aleatorio={
"nomes" : nome_funcionarios,


}