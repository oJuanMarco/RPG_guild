from limpar import limpa_tela

def listar_aventureiros(guilda):
    limpa_tela()
    if guilda.personagens:
        guilda.listar_personagens()
    else:
        print("Nenhum aventureiro registrado ou apto à combate\n")
    input()