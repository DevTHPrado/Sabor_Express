import os 

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] 

def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do nosso programa (aplicativo)'''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções do nosso programa'''
    print('1. Cadastar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app(): 
    '''Essa função é responsável por encerrar o nosso programa'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Essa função é responsável por não deixar o programa encerrar após ele selecionar uma opção (a não ser a 4) e retornar o usuário ao menu principal'''
    input('\nDigite uma tecla para voltar para o menu')
    main()

def opcao_invalida():
    '''Essa função é responsável para que o programa não deixar o programa dar erro caso o usuário digite uma opção incorreta'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtítulo do nosso programa após as opções serem escolhidas, e mostra-las dentro de uma caixnha de *'''
    os.system('cls') 
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar todo o restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    ''' 
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} 
    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável para listar os restaurantes cadastrados em nosso programa, mostrar a categoria de cada um e se está com o status ativo ou desativado, ele mostra em uma tabela para facilitar a visualização'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status') 
    for restaurante in restaurantes: 
        nome_restaurante = restaurante['nome'] 
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') 

    input('\nDigite uma tecla pata voltar ao menu principal')
    main()

def alterar_estado_restaurante():
    '''Essa função é responsável por alterar o estado do restaurante, de ativo para desativado ou de desativado para ativo. e caso o usuário coloque o nome incorreto do restaurante, ele evita que o programa de erro informando que o restuarante não foi encontrado e voltando para o menu principal'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] 
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável pela parte em que o usuário escolhe a opção que ele quer, seja 1, 2, 3 ou 4, caso ele digite uma opção diferente dessas, o programa informa que a opção escolhida é inválida'''
    try: 
        opcao_escolhida = int(input('Escolha um opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

    '''esse codigo poderia ser feito com o comando 'match' da seguinte forma: opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção inválida!')'''

def main(): 
    '''Essa função é a principal função do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__': 
    main()