'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha'''
''' Façam este programa:
- Crie um programa que leia vários números, armazene-os numa lista e depois 
mostre estas informações:
Quantidade de elementos armazenados na lista;
Soma dos valores da lista
Maior valor da lista
Menor valor da lista
Leia um valor e verificar se ele está na lista
No item anterior, mostre também a posição (índice) do valor encontrado na pesquisa
Mostre a lista na ordem crescente
Insira o valor 33 na posição (índice) 2 da lista
Mostre a lista na ordem decrescente
Média dos valores da lista
Porcentagem dos números maiores que dez na lista.
 Dica: porcentagem = uma parte dividido pelo todo vezes 100    -----'''
if __name__ == '__main__':              # main <tab>
    l = []                                         # Cria uma lista vazia
    #l = list()                                  # Cria uma lista vazia, declaração usando a classe list
    print('Digite [0] pra sair')
    while True:
        v = int(input("Valor: "))
        if v == 0:                                       # Condicção de saída
            break                                        # Sai de uma estrutura de repetição
        l.append(v)                                    # Acrescenta o valor v no final da lista.
    # Final do while
print('Quantidade de elementos da lista:', len(l))
print('Soma:', sum(l))
print('Maior valor: ', max(l))
print('Menor valor:', min(l))
pesquisa = int(input("Valor da pesquisa: "))
if pesquisa in l:                              # O operador in retorna True ou False
    print("Valor encontrado.")
    posicao = l.index(pesquisa)
    print('Posição da pesquisa:', posicao)
else:
    print("Valor não encontrado.")
#print(2 in l)
# print(9 in l)
l.sort()                            #l.sort(reverse=False)
print('Lista na ordem crescente: ', l)
l.insert(2, 33)
print(l)
# l.reverse()                            # Errado
# print(l)
l.sort(reverse=True)               # Certo, ordem decrescente
print('Descendente: ', l)
# Média dos valores da lista
print('Média: ', sum(l)/len(l))
# Porcentagem dos números maiores que dez na lista: uma parte dividido por todos vezes 100    -----'''
# Teste 1:  l = [1, 33]                        porcentagem 50
# Teste 2:  l = [1, 2, 33]                    porcentagem 33.3
count = 0                                            # Solução 1
for i in l:
    if i > 10:
        count += 1
porc = count * 100 / len(l)
print("Porcentagem de nmr maior q 10: ", porc)
# Refaça o programa anterior sem usar o contador (count)
l_maior_10=[]                                      # Solução 2
for v in l:
    if v > 10:
        l_maior_10.append(v)
porc = len(l_maior_10) / len(l) * 100           # porc = len(l_maior_10) * 100 / len(l)
print("Porcentagem de nmr maior q 10: ", porc)
'''
---
    l = [1, 3, 2, 3]  # Valores para teste
    # l = list(1, 3, 2, 3)  # declaração explicita com mesmo resultado do que o código anterior
    # Erro nessa linha anterior: TypeError: list() takes at most 1 argument (4 given)
---
Organizar os dois arquivos de teoria de lista na ordem crescente.
l.index(), tratar msg erro
l.sum(), l vazia, tratar msg erro
try ... except
---
Depois fazer este exercício:
CRUD (acrónimo do inglês Create, Read, Update and Delete) são as quatro
operações básicas (criação, consulta, atualização e destruição de dados) utilizadas
em bases de dados relacionais (RDBMS) fornecidas aos utilizadores do sistema. '''