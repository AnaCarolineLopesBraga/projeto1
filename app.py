import os
restaurantes=[{'nome': 'Tempero Salgado', 'categoria': 'Salgada','ativo':False}, 
              {'nome': 'Tempero Mineiro', 'categoria': 'Mineira','ativo':True},
              {'nome': 'Sushi Nadya', 'categoria': 'Japonesa','ativo':False}
              ]

def exibir_nome_do_programa():
  
    print("𝕔𝕒𝕓𝕖𝕔̧𝕒 𝕕𝕖 𝕘𝕖𝕝𝕠")

def exibir_opções():
    print("1-cadastrar restaurante")
    print("2-listar restaurante")
    print("3-ativar restaurante")
    print("4-encerrar programa")
       
def Encerrando_programa():
    exibir_subtitulo("encerrando programa")
    
def opção_invalida():
    print('Opção invalida"!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante'''

    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante ={'nome': nome_do_restaurante,'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
      input("\nDigite qualquer tecla para voltar ao menu principal")
      main()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def escolher_opção():
    try:
       
        opção = int(input("escolha uma opção:"))
        print('a opção escolhida foi:',opção)



        if opção == 1:
                cadastrar_novo_restaurante()
        elif opção == 2:
              listar_restaurantes()
        elif opção == 3:
                print("ativar restaurante")
        elif opção == 4:
                Encerrando_programa()
        else:
                opção_invalida()
    except:
          
          opção_invalida()
def main():
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opções()
        escolher_opção()

if __name__ == '__main__':
    main()