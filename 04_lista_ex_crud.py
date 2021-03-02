'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha'''
''' CRUD (acrónimo do inglês Create, Read, Update and Delete) são as quatro
operações básicas (inclui, consulta, atualiza e apaga os dados) utilizadas
em bases de dados relacionais (RDBMS) fornecidas aos utilizadores do sistema. 
- Desenvolva o programa com as funções main com repetição, menu, create, 
read, update e delete para simular um CRUD. Neste exercício, use nomes.
A função main gerencia todo o programa usando uma estrutura de repetição, 
ou seja, todas as funções serão chamadas da função main. 
A função menu não recebe nada, apresenta as quatro operações do CRUD,  
lê a opção do usuário  e retorna  a opção digitada pra função main:
    c - create (inserir um item)
    r -read     (mostrar toda a lista)
    u - update (substituir um item)
    d - delete  (remover um item)
    s  - sair
    Digite sua opção: 
A função create não recebe nada e não retorna nada. Lê um nome e insere na lista.
A função read não recebe nada e não retorna nada. Mostra toda a lista.
A função update não recebe nada e não retorna nada. Lê os dados necessários 
e substitui (altera) um item da lista. 
A função delete ler o item (nome) que será excluído e apaga da lista.             ---- '''
def menu():
    print('c - create')
    print('r - read')
    print('u - update')
    print('d - delete')
    print('s - sair')
    opcao = input('Opção: ')
    return opcao
def create():
    n = input('Nome: ')
    l.append(n)
def read():
    print(l)  # Na horizontal
def update():
    p = int(input("Qual posição: "))
    v = input("Novo noome: ")
    l[p] = v
def delete():
    v = input("Qual valor: ")
    l.remove(v)
if __name__ == '__main__':
    l = []
    while True:
        r = menu()
        if r == 'c':
            create()
        elif r == 'r':
            read()
        elif r == 'u':
            update()
        elif r == 'd':
            delete()
        else:
            break
