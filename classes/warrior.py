from objects.character import PersonagemBase

class Guerreiro(PersonagemBase):
    def __init__(self,nome='',nivel=0):
        super().__init__(nome,nivel)
        self._classe = "Guerreiro"

    @property
    def habilidade_especial(self):
        return f"Aumenta dano físico por 3 turnos"

    def __str__(self):
        return f"{super().__str__()}\nClasse: Guerreiro\nHabilidade: {self.habilidade_especial}"