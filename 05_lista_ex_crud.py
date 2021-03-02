'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha'''
def menu():
    l_opcoes = ['c', 'r', 'u', 'd', 's']
    print('c - create')
    print('r - read')
    print('u - update')
    print('d - delete')
    print('s - sair')
    opcao=''
    while opcao not in l_opcoes:                          # [not] in, contido em
        opcao = input('Opção: ').lower()
        if  opcao not in l_opcoes:
            print('Opção inválida, tente novamente.')
    return opcao
''' - Na função create, colocar um menu com três opções: 
[p] - Incluir vários nomes em posições específicas da lista
[f] - Incluir vários nomes sempre no final da lista.
[s] - Sair
Colocar mensagem de erro: "Opção inválida"        
Funcionar com letra minúscula ou maiúscula       ----- '''
# def create():
#     nome = input('Nome: ')
#     lista.append(nome)
def create():
    print('[p] - Posição')
    print('[f] - Final')
    print('[s] - Sair')
    opcao = input('Opção: ').lower()
    if opcao == 'p':
        i = int(input("Posição ou [-1] pra sair: "))
        while i != -1:
            nome = input('Nome: ')
            lista.insert(i, nome)                                # lista.insert(indice, valor)
            i = int(input("Posição ou [-1] pra sair: "))
    elif opcao == 'f':
        nome = input('Nome ou <enter> para sair: ')
        while nome != '':
            lista.append(nome)
            nome = input('Nome ou <enter> para sair: ')
    elif opcao == 's':
        pass                                        # Passa por esta linha e não faz nada.
    else:
        print("Opção inválida")
def read():
    # if len(lista):       # if len(lista) != 0:      # if lista != []      # if lista:
    if lista_nao_vazia():
    #     print(lista)                                    # Na horizontal
    #     for v in lista:                                # Na vertical, sem índice
    #        print(v)
    #     ct = 0                                           # Na vertical, com índice e usando ct
    #     for v in lista:
    #         print(ct, ' – ', v)
    #         ct += 1
        for indice, v in enumerate(lista):    # Na vertical com índice e sem ct
            print(indice, ' - ', v)
    # else:
    #     print('Lista vazia.')
'''  - Na função update, colocar um menu com três opções: 
[p] - Atualizar usando uma posição específica da lista e o novo nome. 
[n] - Atualizar usando o nome na lista e o novo nome. 
[s] - Sair
Colocar mensagem de erro: "Opção inválida" 
Obs.: para evitar erro, faça crítica antes de atualizar.        '''
def update():
    if lista_nao_vazia():
    # if len(lista):       # if len(lista) != 0:      # if lista != []      # if lista:
        read()
        print('[p] - Posição')
        print('[n] - Nome')
        print('[s] - Sair')
        opcao = input('Opção: ').lower()
        if opcao == 'p':
            p = int(input("Qual posição: "))
            n_n = input("Novo nome: ")
            try:                                                                       # Tenta executar
                lista[p] = n_n                             # lista.pop(p)
                                                                   # lista.insert(p, n_n)
            except IndexError as e:                                       # Se erro de índice
                print("Erro IndexError: ", e)
            except Exception as e:
                print("Erro Exception: ", e)
        elif opcao == 'n':
            n_l = input('Nome da lista: ')
            if n_l in lista:                                # operador in, n_l pertence a lista
                i = lista.index(n_l)
                n_n = input('Nome novo: ')
                lista[i] = n_n
            else:
                print(f'O {n_l} não está na lista')
        elif opcao == 's':
            pass
        else:
            print('Opção inválida')
    # else:
    #     print('Lista vazia.')
''' - Na função delete, colocar um menu com três opções: 
[p] - Apagar usando uma posição específica da lista. 
[n] - Apagar usando o nome na lista. 
[s] - Sair
Colocar mensagem de erro: "Opção inválida" 
Obs.: para evitar erro, faça crítica antes de apagar.        '''
def delete():
    # if len(lista):       # if len(lista) != 0:      # if lista != []      # if lista:
    if lista_nao_vazia():
        read()
        # print('[p] - Posição') # Substituir os três prints por um único print numa linha
        # print('[n] - Nome')
        # print('[s] - Sair')
        print('[p] - Posição\n[n] - Nome\n[s] - Sair')
        opcao = input('Opção: ')
        if opcao == 'p':
            posicao = int(input("Qual posição: "))
            tam = len(lista)
            if posicao <= tam - 1:
                del lista[posicao]
            else:
                print(f'Posição {posicao} não existe')
        elif opcao == 'n':
            nome = input("Qual nome: ")
            if nome in lista:
                lista.remove(nome)
            else:
                print(f'O {nome} não está na lista.')
        elif opcao == 's':
            pass
        else:
            print('Opção inválida')
#    else:
#        print('Lista vazia.')
def lista_nao_vazia():                                                                  # Solução 1
    if len(lista):       # if len(lista) != 0:      # if lista != []      # if lista:
        nao_vazia = True
    else:
        nao_vazia = False
        print('Lista vazia.')
    return nao_vazia
def lista_nao_vazia():                                                                  # Solução 2
    situacao = bool (lista)
    if not situacao:
        print('Lista vazia.')
    return situacao
if __name__ == '__main__':
    lista = []
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
''' 
def lista_nao_vazia():                    # Solução 2
    situacao = bool (lista)
    if not situacao:
        print('Lista vazia.')
    return situacao
 ---
 def menu():                                  # Solução 2
    print("[c] - Create\n[r] - Read\n[u] - Update\n[d] - Delete\n[s] - Sair\n")
    opcoes = ['c', 'r', 'u', 'd', 's']
    while True:
        opcao = input('Diga sua opção: ').lower()
        if opcao not in opcoes:
            print('Inválida!')
            continue
        else:
            break
    return opção

 '''

