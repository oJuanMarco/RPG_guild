from limpar import limpa_tela
from objects.mission import Missao

def listar_missoes():
    limpa_tela()
    Missao.listar_missoes()
    limpa_tela()
