############################### Listas ###############################
#Indice -> Posição que o elemento está em relação a lista

Lista = [1, 4, 3, 2, 7, 8, 5, 6, 9, 10] #Números -> Para ordenar .sort()
      #  0  1  2  3  4  5  6  7  8  9   ->Index/Indice

Outra_lista = [12, 13, 14, 15]

#Concatena as listas
Lista_Final = Lista + Outra_lista

#Função .sort()
Lista.sort()

#Adicionar elementos a lista .append()
Lista.append(11)

#Adicionar elementos com o .insert()
Lista.insert(0, 25)

#Remover os elementos com o .remove()
Lista.remove(Lista[0])

#Remover os elementos com o .pop()
Lista.pop()

#Criar uma lista de tupla?
lista_de_tupla = [(1,2,3,4),
                  (1,2,4,5,6),
                  (12,3,4,56,)]

lista_de_lista =[[[1,2,3,4,5],[10,11,12,13]],
                  [[6,7,8,9,10]]]


############################### Tuplas ###############################

tupla = ("Luizinho", "Leleo", "João Ricardo", "Yuta", "Heitor")

#Método utilizado para contar quantas vezes um elemento aparece dentro da tupla
tupla.count("Luizinho")

#Método utilizado para retornar a posição que um elemento aparece dentro da tupla
tupla.index("Yuta")

############################### Dicionário ###############################
#            palavra : significado
dicionario = {"Luiz" : "Graça",
              "João Ricardo" : "Gomes",
              "Miguel" : "Santos",
              "Bruna" : "Gelonezze",
              }

############################### Parte prática ###############################
Lista_de_notas = [6, 5, 7.5, 7, 5, 6]

#sum é a função de soma -> Soma todos os elementos inteiros ou flutuantes em uma lista
#len é a função que conta quantos elementos tem detro de uma lista, tupla e dicionário
Media = sum(Lista_de_notas) / len(Lista_de_notas)

print(f"A média das suas notas são: {Media}")





