# ⚔️ Sistema de Guilda RPG

> 🇧🇷 Português | [🇺🇸 English below](#️-rpg-guild-system)

---

Sistema de gerenciamento de guilda em terminal, com cadastro de aventureiros, missões dinâmicas e mecânica de combate baseada em atributos e aleatoriedade.

Projeto autoral desenvolvido de forma independente — a ideia foi sugerida por um mentor como desafio de aprendizado, mas toda a lógica, arquitetura e construção do código foram desenvolvidas de forma completamente autoral.

---

## 🚀 Tecnologias & Conceitos

- **POO completa** com herança, polimorfismo, ABC e `@abstractmethod`
- **`@property`** como implementação de método abstrato nas subclasses
- **`@classmethod`** e **`@staticmethod`** aplicados com propósito real
- **`isinstance()`** para validação de tipo na entrada da guilda
- **`setattr()`** para atribuição dinâmica de atributos
- **Dicionário de lambdas** para instanciar classes dinamicamente
- **`match/case`** no menu principal com `case _` como fallback
- **`try/except`** com exceções específicas (`ValueError`, `IndexError`)
- **`random.randint`** para mecânica de combate com bônus de nível
- **Separação de responsabilidades** em módulos (`classes/`, `functions/`, `objects/`)
- **Compatibilidade de SO** com `os.name`

---

## 🗂️ Estrutura do Projeto

```
GUILDARPG/
├── classes/
│   ├── archer.py       # Classe Arqueiro
│   ├── warrior.py      # Classe Guerreiro
│   └── wizard.py       # Classe Mago
├── functions/
│   ├── checkin.py      # Cadastro de aventureiro
│   ├── close.py        # Encerramento do sistema
│   ├── do_mission.py   # Execução de missão
│   ├── list.py         # Listagem de aventureiros
│   ├── list_missions.py# Listagem de missões
│   └── signup_mission.py # Cadastro de missão
├── objects/
│   ├── character.py    # Classe base abstrata (PersonagemBase)
│   ├── guild.py        # Classe Guilda
│   └── mission.py      # Classe Missao
├── limpar.py           # Utilitário de limpeza de tela
└── main.py             # Ponto de entrada da aplicação
```

---

## 🎮 Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| **Cadastro de aventureiro** | Cria Guerreiro, Mago ou Arqueiro com nome, nível e descrição opcional |
| **Listagem de aventureiros** | Exibe aventureiros ativos com classe, nível e ouro acumulado |
| **Cadastro de missão** | Define nome, descrição, recompensa e dificuldade (1 a 5) |
| **Listagem de missões** | Exibe missões disponíveis com status de conclusão |
| **Fazer missão** | Mecânica de combate com sorteio, bônus de nível e consequências reais |
| **Nível & Ouro** | Aventureiro ganha +1 nível e recompensa em ouro ao vencer |
| **Derrota** | Aventureiro é desativado da guilda em caso de falha |

---

## ▶️ Como executar

```bash
git clone https://github.com/oJuanMarco/RPG_guild
cd guildarpg
python main.py
```

> Requer Python 3.10+ para `match/case`

---

## 👤 Autor

**Juan Marco**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/ojuanmarco/)
[![GitHub](https://img.shields.io/badge/GitHub-Perfil-181717?style=flat&logo=github)](https://github.com/oJuanMarco)

---
---

# ⚔️ RPG Guild System

> [🇧🇷 Português acima](#️-sistema-de-guilda-rpg) | 🇺🇸 English

---

A terminal-based guild management system featuring adventurer registration, dynamic missions, and a combat mechanic driven by character attributes and randomness.

An independent authorial project — the idea was suggested by a mentor as a learning challenge, but all logic, architecture, and code were developed entirely by the author.

---

## 🚀 Technologies & Concepts

- **Full OOP** with inheritance, polymorphism, ABC and `@abstractmethod`
- **`@property`** as abstract method implementation in subclasses
- **`@classmethod`** and **`@staticmethod`** applied with real purpose
- **`isinstance()`** for type validation on guild entry
- **`setattr()`** for dynamic attribute assignment
- **Lambda dictionary** to dynamically instantiate classes
- **`match/case`** in the main menu with `case _` as fallback
- **`try/except`** with specific exceptions (`ValueError`, `IndexError`)
- **`random.randint`** for combat mechanic with level bonus
- **Separation of concerns** across modules (`classes/`, `functions/`, `objects/`)
- **Cross-platform compatibility** via `os.name`

---

## 🗂️ Project Structure

```
GUILDARPG/
├── classes/
│   ├── archer.py       # Archer class
│   ├── warrior.py      # Warrior class
│   └── wizard.py       # Wizard class
├── functions/
│   ├── checkin.py      # Adventurer registration
│   ├── close.py        # System shutdown
│   ├── do_mission.py   # Mission execution
│   ├── list.py         # Adventurer listing
│   ├── list_missions.py# Mission listing
│   └── signup_mission.py # Mission registration
├── objects/
│   ├── character.py    # Abstract base class (PersonagemBase)
│   ├── guild.py        # Guild class
│   └── mission.py      # Mission class
├── limpar.py           # Screen clear utility
└── main.py             # Application entry point
```

---

## 🎮 Features

| Feature | Description |
|---|---|
| **Register adventurer** | Creates Warrior, Wizard or Archer with name, level and optional description |
| **List adventurers** | Displays active adventurers with class, level and accumulated gold |
| **Register mission** | Defines name, description, reward and difficulty (1 to 5) |
| **List missions** | Displays available missions with completion status |
| **Do mission** | Combat mechanic with random rolls, level bonus and real consequences |
| **Level & Gold** | Adventurer gains +1 level and gold reward on victory |
| **Defeat** | Adventurer is deactivated from the guild on failure |

---

## ▶️ How to run

```bash
git clone https://github.com/oJuanMarco/RPG_guild
cd guildarpg
python main.py
```

> Requires Python 3.10+ for `match/case`

---

## 👤 Author

**Juan Marco**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/ojuanmarco/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/oJuanMarco)
