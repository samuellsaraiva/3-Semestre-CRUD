'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha'''
''' CRUD (acrónimo do inglês Create, Read, Update and Delete) são as quatro
operações básicas (inclui, consulta, atualiza e apaga os dados) utilizadas
em bases de dados relacionais (RDBMS) fornecidas aos utilizadores do sistema. 
- Desenvolva o programa usando lista com as funções main com repetição, menu,  
create, read, update e delete para simular um CRUD. Neste exercício, use nomes.
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
A função read não recebe nada e não retorna nada. Mostra todos os itens da lista.
A função update não recebe nada e não retorna nada. Lê os dados necessários 
(índice e o novo nome) e substitui (altera) um item da lista. 
A função delete não recebe nada e não retorna nada.  Lê o item (nome) que será 
excluído e apaga da lista.                 ----- '''
''' ----- ALTERAÇÕES:
- Na função menu, inclua a msg: "Opção inválida, tente novamente." 
E só sai da função menu se o usuário digitar uma das opções válidas.
Ela deve aceitar letra maiúscula ou minúscula.
Dicas: use while e um if dentro do while com msg erro                        '''
def menu():
    l_opcoes = ['c', 'r', 'u', 'd', 's']
    opcao=''
    while opcao not in l_opcoes:                          # [not] in, contido em
        print('c - create')
        print('r - read')
        print('u - update')
        print('d - delete')
        print('s - sair')
        opcao = input('Opção: ').lower()
        if  opcao not in l_opcoes:
            print('Opção inválida, tente novamente.')
    return opcao
def create():
    nome = input('Nome: ')
    lista.append(nome)
'''- Na função read, se a lista estiver vazia, mostre a msg: "Lista vazia."
Mostre todos os itens na vertical.
Mostre todos os itens na vertical com o íncice.   '''
def read():
    if len(lista):                        # if len(lista) != 0:           # if lista:
        print(lista)                                    # Na horizontal
        for v in lista:                                # Na vertical, sem índice
           print(v)
        ct = 0                                           # Na vertical, com índice e usando ct
        for v in lista:
            print(ct, ' – ', v)
            ct += 1
        for indice, v in enumerate(lista):    # Na vertical com índice e sem ct
            print(indice, ' - ', v)
    else:
        print('Lista vazia.')
'''- No update, se lista vazia, mostre msg "Lista vaiza."
Senão mostre os itens da lista.
Se posição não existe, msg erro. Use try ... except      '''
def update():
    if len(lista):                        # if len(lista) != 0:           # if lista:
        read()
        p = int(input("Qual posição: "))
        novo_nome = input("Novo nome: ")
        try:
            lista[p] = novo_nome  # lista.pop(p)
                                                # lista.inserrt(p, novo_nome)
        except IndexError as e:
            print("Erro IndexError: ", e)
        except Exception as e:
            print("Erro Exception: ", e)
    else:
        print(f'Lista vazia.')
'''- No delete, se lista vazia, mostre msg "Lista vaiza."
Senão mostre os itens da lista.
Verifique se valor está na lista. Se valor não existe, msg erro     '''
def delete():
    if len(lista):
        read()
        v = input("Qual nome: ")
        if v in lista:
            lista.remove(v)
        else:
            print(f'O {v} não está na lista.')
    else:
        print(f'Lista vazia.')
# def delete():
#     v = input("Qual nome: ")
#     lista.remove(v)
if __name__ == '__main__':    # main <tab>
    lista = []
    while True:
        retorno = menu()
        if retorno == 'c':
            create()
        elif retorno == 'r':
            read()
        elif retorno == 'u':
            update()
        elif retorno == 'd':
            delete()
        else:
            break
''' ----- ALTERAÇÕES: 
- Na função menu, inclua msg:  "Opção inválida, tente novamente." 
E só sai da função menu se o usuário digitar uma das opções válidas.
Ela deve aceitar letra maiúscula ou minúscula   
Dicas: use while, if com msg erro                          
- Na função read, mostre todos os itens na vertical.
Mostre todos os itens na vertical com o íncice.
Se a lista estiver vazia, mostre a msg "Lista vazia."     
- No update, se lista vazia, mostre msg "Lista vaiza."
Senão mostre os itens da lista.
Se posição não existe, msg erro. Use try ... except
- No delete, se lista vazia, mostre msg "Lista vaiza."
Senão mostre os itens da lista.
Verifique se valor está na lista. Se valor não existe, msg erro
'''