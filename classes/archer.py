from objects.character import PersonagemBase

class Arqueiro(PersonagemBase):
    def __init__(self,nome='',nivel=0):
        super().__init__(nome,nivel)
        self._classe = "Arqueiro"

    @property
    def habilidade_especial(self):
        return f"Aumenta a quantidade de disparos em 25% por 3 turnos"

    def __str__(self):
        return f"{super().__str__()}\nClasse: Arqueiro\nHabilidade: {self.habilidade_especial}"