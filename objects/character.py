from abc import ABC, abstractmethod

class PersonagemBase(ABC):
    def __init__(self,nome='',nivel=0):
        self._nome=nome.title()
        self._nivel=nivel
        self._descricao = ""
        self._ouro = 0
        self._ativo=False

    def __str__(self):
        return f"Personagem: {self._nome}\nNível: {self._nivel}"

    @abstractmethod
    def habilidade_especial(self):
        pass

    def ativar_personagem(self):
        self._ativo = not self._ativo