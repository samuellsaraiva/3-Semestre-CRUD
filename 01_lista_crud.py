'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha'''
''' CRUD (acrónimo do inglês Create, Read, Update and Delete) são as quatro
operações básicas (criação, consulta, atualização e destruição de dados) utilizadas
em bases de dados relacionais (RDBMS) fornecidas aos utilizadores do sistema. 
Neste exercício, use nomes.
Menu:
c - create (inserir um item)
r -read     (mostrar toda a lista)
u - update (substituir um item)
d - delete  (remover um item)
s  - sair
Crie as funções: main com repetição, menu, create, read, update e delete
A função main gerencia todo o programa, ou seja, todas as funções serão chamadas da função main
A função create ler um valor e insere na lista.
A função read mostra toda a lista.
A função update ler os dados  necessários e altera o valor da lista. 
A função delete ler o item que será excluído e apaga da lista.             ---- '''
def menu():
    print('c - create')
    print('r - read')
    print('u - update')
    print('d - delete')
    print('s - sair')
    o = input('Opção: ')
    return o
def create():
    n = input('Nome: ')
    l.append(n)
def read():
    #print(l)                    # Na horizontal
    for v in l:                  # Na vertical
        print(v)
# ...
if __name__ == '__main__':
    l = []
    while True:
        pass
# ...