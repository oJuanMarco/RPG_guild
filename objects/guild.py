from objects.character import PersonagemBase

class Guilda:
    personagens = []
    missoes = []

    def __init__(self,nome):
        self._nome=nome

    def __str__(self):
        return f"{self._nome}"

    def adicionar_personagem(self,personagem):
        if isinstance(personagem,PersonagemBase):
            self.personagens.append(personagem)


    @classmethod
    def listar_personagens(cls):
        for personagem in cls.personagens:
            if personagem._ativo:
                print(f"{personagem._nome} | Nível: {personagem._nivel} | Classe: {personagem._classe} | Ouro : {personagem._ouro}")
                if personagem._descricao != "":
                    print(f"Descrição : {personagem._descricao}\n")
                else:
                    print()