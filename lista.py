# Etapa 1 - Criar uma lista com os nomes de 5 objetos
objetos = ["shampoo", "condicionador", "máscara", "finalizador", "óleo reparador"]
print("lista de objetos criada")
# Etapa 2 - Adicione mais um objeto ao final da lista
objetos.append("perfume de cabelo")
print("objeto adicionado a lista")
# Etapa 3 - Acesse o objeto que está na segunda posição
segundo_objeto = objetos[1]
print(f"objeto 2 acessado - {segundo_objeto}")
# Etapa 4 - Remova um objeto da lista
objetos.remove('óleo reparador')
print('óleo reparador removido da lista de objetos')
# Etapa 5 - Exiba o tamanho da lista
len(objetos)
print(len(objetos))
# Etapa 6 - Mostre todos os itens com um laço for
for objeto in objetos:
    print(objeto)
# Etapa 7 - Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("cadeira removida da lista de objetos")
else:
    objetos.append("cadeira")
    print("cadeira adicionada a lista de objetos")
# Etapa 8 - Ordene a lista em ordem alfabética
objetos.sort()
print(objetos)
# Etapa 9 - Exiba o primeiro e o último objeto
primeiro_objeto = objetos[0]
print(primeiro_objeto)
ultimo_objeto = objetos[5]
print(ultimo_objeto)
# Etapa 10 - Limpe toda a lista
objetos.clear()
print(objetos)