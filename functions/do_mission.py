from limpar import limpa_tela
from objects.mission import Missao
from objects.guild import Guilda
import random

def fazer_missao(guilda):
    limpa_tela()
    print("Escolha qual das missões deseja fazer, se não, informe '0':\n ")
    
    missoes_disponiveis = []
    personagens_disponiveis = []

    for missao in Missao.missoes:
        if not missao._status:
            missoes_disponiveis.append(missao)
            print(f"{len(missoes_disponiveis)}.{missao._nome} (lvl {missao._nivel})")

    if missoes_disponiveis:
        while True:
            try:
                escolha_de_missao = int(input("\n"))
                if escolha_de_missao == 0:
                    input("Saindo...")
                    return
                    break
                elif missoes_disponiveis[escolha_de_missao-1] in Missao.missoes and escolha_de_missao>0:
                    input(f"Missão escolhida: {missoes_disponiveis[escolha_de_missao-1]._nome}")
                    break
                else:
                    print("Informe um número correspondente á lista")
            except ValueError:
                print("Informe ao menos um número")
            except IndexError:
                print("Informe um número correspondente á lista")
        
        index_missao = Missao.missoes.index(missoes_disponiveis[escolha_de_missao-1])
        limpa_tela()

        for personagem in guilda.personagens:
            if personagem._ativo:
                personagens_disponiveis.append(personagem)
                print(f"{len(personagens_disponiveis)}.{personagem._nome} (lvl.{personagem._nivel}) - {personagem._classe}")


        while True:
            saida = 0
            escolha_de_personagem = input("\nQual aventureiro deseja levar pra essa aventura? (Informe o nome)\n").lower().title()

            for personagem in personagens_disponiveis:
                if escolha_de_personagem == personagem._nome:
                    print(f"\nAventureiro escolhido: {escolha_de_personagem}")
                    saida += 1
                    break
            
            if saida != 0:
                for personagem in guilda.personagens:
                    if escolha_de_personagem == personagem._nome:
                        index_personagem = guilda.personagens.index(personagem)
                
                nivel_missao = Missao.missoes[index_missao]._nivel
                nivel_personagem = guilda.personagens[index_personagem]._nivel

                if nivel_missao > nivel_personagem:
                    input("Nivel insuficiente, tente outro")
                    break 
                else:
                    numero_personagem = random.randint(0,10)
                    numero_personagem += 1 if nivel_personagem >= (nivel_missao + 10) else numero_personagem
                    numero_missao = random.randint(1,7)
                    
                    if numero_personagem>=numero_missao:
                        print(f"Numero do jogador: {numero_personagem}")
                        print(f"Numero do PC: {numero_missao}")
                        
                        if nivel_personagem >= (nivel_missao + 10):
                            print ("Bônus de nível")
                        
                        Missao.missoes[index_missao].concluir_missao()
                        guilda.personagens[index_personagem]._nivel += 1
                        guilda.personagens[index_personagem]._ouro += Missao.missoes[index_missao]._recompensa_ouro

                        print("\nMissão concluída!")
                        print(f"Recompensa: {Missao.missoes[index_missao]._recompensa_ouro} ouro(s)")
                        print(f"{guilda.personagens[index_personagem]._nome} +1 lvl")
                        input()
                        break
                    else:    
                        print(f"Numero do jogador: {numero_personagem}")
                        print(f"Numero do PC: {numero_missao}")
                        guilda.personagens[index_personagem].ativar_personagem()
                        input("\nMissão falha, aventureiro derrotado em combate")
                        break
            else:
                print("Informe o nome de algum dos aventureiros disponiveis\n")
    else:
        input("Sem missões no momento, volte outro dia")

    limpa_tela()