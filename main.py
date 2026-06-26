from limpar import limpa_tela

from objects.guild import Guilda
from objects.mission import Missao

from functions.list import listar_aventureiros
from functions.checkin import cadastrar_aventureiro
from functions.close import encerrar
from functions.signup_mission import cadastrar_missão
from functions.list_missions import listar_missoes
from functions.do_mission import fazer_missao

#insira os imports abaixo

def main():
    try:
        while True:
            nome = input("Para começar informe o nome que deseja dar à sua guilda: ")
            if len(nome)>4:
                guilda = Guilda(nome)
                break
            else:
                input("Nome inválido, seja mais criativo!")
                limpa_tela()
        
        #Insira as instâncias logo abaixo
        
        while True:
            limpa_tela()

            print("""
            █▄▄ █▀▀ █▀▄▀█   █░█ █ █▄░█ █▀▄ █▀█   ▄▀█   █▀▀ █░█ █ █░░ █▀▄ ▄▀█   █▀▄ █▀▀
            █▄█ ██▄ █░▀░█   ▀▄▀ █ █░▀█ █▄▀ █▄█   █▀█   █▄█ █▄█ █ █▄▄ █▄▀ █▀█   █▄▀ ██▄

                        ▄▀█ █░█ █▀▀ █▄░█ ▀█▀ █░█ █▀█ █▀▀ █ █▀█ █▀█ █▀               
                        █▀█ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ██▄ █ █▀▄ █▄█ ▄█
            """)

            print(f"Registro: Guilda {guilda}\n".center(90))
            print("Oque deseja fazer?".center(90))
            
            opcao = input("""
            1.Fazer missão
            2.Listar aventureiros
            3.Cadastrar aventureiros
            4.Listar missões
            5.Cadastrar missão
            6.Fechar guilda\n
            """).lower()

            match opcao:
                case "fazer missão":
                    fazer_missao(guilda)
                case "listar aventureiros":
                    listar_aventureiros(guilda)
                case "cadastrar aventureiros":
                    cadastrar_aventureiro(guilda)
                case "listar missões":
                    listar_missoes()
                case "cadastrar missão":
                    cadastrar_missão()
                case "fechar guilda":
                    encerrar()
                    break
                case _:
                    limpa_tela()
                    input("Opção inválida")
    except:
        limpa_tela()
        print("Erro encontrado")
if __name__ == "__main__":
    main()