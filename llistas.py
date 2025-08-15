frutas = ["banana", "laranja","jaca","jaca"]
frutas.append("manga")
frutas.insert(0,"limão")
salada_de_fruta = frutas
# fruta = "manga"
# frutas.insert(5, "limao")
# print(frutas)
#temperos=["pimenta","sal"]
#frutas+=temperos
# print (frutas[:])
# print (temperos)
 
 #######3remover 
#frutas.pop(1)
#print (frutas.clear())
######## ordenar lista
# frutas.sort(reverse= True)
# print(frutas)
# ######## copi\r lista
# fruta= "morango"
# morango_do_amor= fruta
# ##### copiar lista
#salada_de_frutas = []
#salada_de_fruta=frutas.copy()
# for fruta in frutas:
#     salada_de_fruta.append(fruta)
#     print(fruta)
#     print(salada_de_fruta)
# print(id(frutas))
# 
salada_de_fruta= ["maça"]
print(frutas)
print(frutas.index("jaca"))
idx_jaca=frutas.index("jaca")
frutas.pop(idx_jaca)
print(frutas) 