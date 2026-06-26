from objects.character import PersonagemBase

class Mago(PersonagemBase):
    def __init__(self,nome='',nivel=0):
        super().__init__(nome,nivel)
        self._classe = "Mago"

    @property
    def habilidade_especial(self):
        return f"Aumenta a eficiência de mana em 50% por 3 turnos"

    def __str__(self):
        return f"{super().__str__()}\nClasse: Mago\nHabilidade: {self.habilidade_especial}"