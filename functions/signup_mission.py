from objects.mission import Missao
from limpar import limpa_tela
import random

def cadastrar_missão():
    limpa_tela()
    print("***Cadastro de missões***")
    while True:
        descricao = input("Descreva qual será a missão da vez para nossos aventureiros!: \n")
        if descricao:
            break
        else:
            print("Informe oque será feito")

    while True:
        nome = input("\nDê um título à missão: ")
        if len(nome)<10:
            input("Seja criativo, tente denovo!")
        else:
            break
    
    while True:
        try:
            recompensa = int(input("\nQuanto oferecerá de recompensa por isso em ouro? (Dificuldades maiores, recompensas maiores, mas você decide!): \n"))
            break
        except:
            print("Informe somente a quantia por gentileza")

    print("\nAgora informe o nivel de dificuldade da missão:")
    print("1.Simples (Qualquer um pode fazer)")
    print("2.Fácil (Um aventureiro iniciante resolve)")
    print("3.Médio (Há perigo real envolvido)")
    print("4.Difícil (É necessário certa experiência)")
    print("5.Extremo (Casos de destruição de cidades)")
    
    while True:
        try:
            nivel = int(input("\nE então? De 1 a 5, em qual dificuldade se encontra sua missão?\n"))
            match nivel:
                case 1:
                    nivel = random.randint(1,5)
                    missao = Missao(nome,descricao,recompensa,nivel)
                    break
                case 2:
                    nivel = random.randint(6,15)
                    missao = Missao(nome,descricao,recompensa,nivel)
                    break
                case 3:
                    nivel = random.randint(15,30)
                    missao = Missao(nome,descricao,recompensa,nivel)
                    break
                case 4:
                    nivel = random.randint(31,80)
                    missao = Missao(nome,descricao,recompensa,nivel)
                    break
                case 5:
                    nivel = random.randint(81,100)
                    missao = Missao(nome,descricao,recompensa,nivel)
                    break
                case _:
                    print("Informe um número de 1 a 5")
        except:
            print("Informe somente o dígito correspondente")

    input("\nMissão registrada com sucesso!")
    limpa_tela()