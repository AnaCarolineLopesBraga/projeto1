import os
restaurantes=[{"nome": "𝕔𝕒𝕓𝕖𝕔̧𝕒 𝕕𝕖 𝕘𝕖𝕝𝕠", "categoria": "almoço", 'ativo':True},
              {"nome": "WWII", "categoria":"lanches", "ativo":False},
              {"nome": "TI", 'categoria':"bar", "ativo":False}]

def exibir_nome_do_programa():
  
    print("𝕔𝕒𝕓𝕖𝕔̧𝕒 𝕕𝕖 𝕘𝕖𝕝𝕠")

def exibir_opções():
    print("1-cadastrar restaurante")
    print("2-listar restaurante")
    print("3-ativar restaurante")
    print("4-encerrar programa")
       
def Encerrando_programa():
    exibir_subtitulo("encerrando programa")
    voltar_ao_menu_principal()
    
def opção_invalida():
    print('Opção invalida"!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo("cadastrando novo restaurante")
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar:')
    restaurantes.append(nome_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
      input("\nDigite qualquer tecla para voltar ao menu principal")
      main()

def listar_restaurantes():
    exibir_subtitulo("listando restaurantes")

    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        print(f' - .{nome_restaurante}')
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