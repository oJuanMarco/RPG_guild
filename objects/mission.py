class Missao:
    missoes = []

    def __init__(self,nome='',descricao='',recompensa_ouro=0,nivel=0):
        self._nome=nome.title()
        self._descricao=descricao
        self._recompensa_ouro=recompensa_ouro
        self._nivel=nivel
        self._status = False
        Missao.missoes.append(self)

    def __str__(self):
        return f"Missão: {self._nome}/ Nível: {self._nivel}\nDescrição: {self._descricao}\nRecompensa: {self._recompensa_ouro} ouros\n Status: {self.status}"
    
    @property
    def status(self):
        return "☑" if self._status else "☒"

    @classmethod
    def listar_missoes(cls):
        if cls.missoes:
            for missao in cls.missoes:
                print(f"Missão (lvl {missao._nivel}): {missao._nome} {missao.status}")
                print(f"Descrição: {missao._descricao}")
                print(f"Recompensa: {missao._recompensa_ouro} ouro(s)")
                print()
            input()
        else:
            input("Nenhuma missão cadastrada")
    
    def concluir_missao(self):
        self._status = not self._status
