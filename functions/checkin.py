from limpar import limpa_tela
from classes.warrior import Guerreiro
from classes.wizard import Mago
from classes.archer import Arqueiro

def cadastrar_aventureiro(guilda):
    limpa_tela()
    
    classes = {
        "mago": Mago,
        "guerreiro": Guerreiro,
        "arqueiro": Arqueiro
    }

    nome=input("Informe o nome do aventureiro: ").lower().title()

    while True:
        print("Informe a classe de aventureiro: ")
        classe = input(""" 
        1.Mago
        2.Guerreiro
        3.Arqueiro\n
        """).lower()

        verifica = classes.get(classe)

        if verifica:
            personagem = verifica(nome,1)
            while True:
                condicao = input("Deseja adicionar descrição ao aventureiro? (s/n):\n")
                if condicao == "s":
                    descricao = input("Descrição: ")
                    atributo = "_descricao"
                    novo_atributo = descricao
                    setattr(personagem,atributo,novo_atributo)
                    break
                elif condicao == "n":
                    break
                else:
                    print("Informe somente 's' ou 'n'\n")
            guilda.adicionar_personagem(personagem)
            personagem.ativar_personagem()
            break
        else:
            print("Classe inválida")
            continue
    
    limpa_tela()
    print("Aventureiro criado com sucesso!\n")
    print(personagem)
    input()