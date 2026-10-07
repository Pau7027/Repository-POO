# ⚔️ Jogo de Batalha

Jogo de batalha por turnos, desenvolvido na disciplina de Programação
Orientada a Objetos. O jogador escolhe uma classe e enfrenta uma
sequência de inimigos até chegar ao chefe final.

O jogo possui **duas interfaces** que compartilham as mesmas classes e a
mesma lógica de batalha:

| Interface | Comando                            | Dependência |
|-----------|------------------------------------|-------------|
| Terminal  | `python -m src.main`               | nenhuma     |
| Pygame    | `python -m src.interface_pygame`   | `pygame-ce` |

## Requisitos

- Python 3.10 ou superior
- pytest (testes)
- pygame-ce (somente para a versão Pygame)

## Instalação

```bash
git clone <url-do-repositorio>
cd <nome-da-pasta>
python -m venv .venv
.venv\Scripts\activate         # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

> **Atenção:** o projeto usa `pygame-ce`, e não `pygame`. Os dois pacotes
> entram em conflito. Se você já tem o `pygame` instalado, rode
> `pip uninstall pygame` antes de instalar o `pygame-ce`.

## Como jogar

Execute sempre **na raiz do projeto**, com `-m`, porque o código usa
imports relativos (`from .personagem import ...`):

```bash
python -m src.main              # versão terminal
python -m src.interface_pygame  # versão gráfica (Pygame)
```

### Fluxo do jogo

1. Escolha a classe do personagem (no terminal você também digita o nome).
2. Na versão Pygame, escolha também a skin (cor) do personagem.
3. Enfrente 3 batalhas em sequência: Goblin → Orc → Dragão Ancião.
4. Após cada vitória (exceto a última) você ganha uma Poção de Vida.
5. Se você morrer ou fugir, o jogo termina.

### Ações em batalha

| Ação        | Descrição                                          |
|-------------|----------------------------------------------------|
| Atacar      | Ataque normal contra o inimigo                     |
| Usar item   | Consome um item do inventário                      |
| Magia       | Apenas o Mago. Custa 20 de mana (começa com 100)   |
| Fugir       | Encerra a batalha e o jogo                         |

Usar item sem itens, ou usar magia sem mana, **não gasta o turno**.

## Personagens

| Classe    | Vida | Ataque | Defesa | Especial                               |
|-----------|------|--------|--------|----------------------------------------|
| Guerreiro | 120  | 20     | 15     | Mais vida e defesa                     |
| Mago      | 80   | 30     | 5      | Magia com 1,5x de ataque e mana        |
| Arqueiro  | 90   | 25     | 8      | Ataque com flecha                      |

## Inimigos

| Inimigo       | Vida | Ataque | Defesa |
|---------------|------|--------|--------|
| Goblin        | 100  | 15     | 5      |
| Orc           | 150  | 25     | 10     |
| Dragão Ancião | 250  | 35     | 15     |

## Regras de combate

- Dano real = `ataque - defesa` do alvo.
- O dano mínimo é sempre 1.
- A vida nunca fica negativa nem passa da vida máxima.
- A Poção de Vida recupera 30 de vida (limitada à vida máxima).

## Estrutura do projeto

```
.
├── src/
│   ├── personagem.py         # Classe abstrata Personagem + escolher_personagem()
│   ├── guerreiro.py          # Guerreiro(Personagem)
│   ├── mago.py               # Mago(Personagem)
│   ├── arqueiro.py           # Arqueiro(Personagem)
│   ├── inimigo.py            # Inimigo(Personagem)
│   ├── orc.py                # Orc(Inimigo)
│   ├── chefe_final.py        # ChefeFinal(Inimigo)
│   ├── item.py               # Item (abstrata) e Pocao_de_vida
│   ├── batalha.py            # Lógica dos turnos de batalha
│   ├── main.py               # Interface de terminal
│   └── interface_pygame.py   # Interface gráfica (Pygame)
├── tests/
│   └── test_personagem.py
├── requirements.txt
└── README.md
```

### Diagrama de herança

```
Personagem (abstrata)
├── Guerreiro
├── Mago
├── Arqueiro
└── Inimigo
    ├── Orc
    └── ChefeFinal

Item (abstrata)
└── Pocao_de_vida
```

### Como as interfaces compartilham a lógica

A classe `Batalha` tem dois conjuntos de métodos:

- **Terminal:** `iniciar()` e `usar_item()`, que usam `input()`.
- **Interface gráfica:** `jogador_atacar()`, `jogador_usar_item()`,
  `jogador_usar_magia()`, `turno_inimigo()` e `terminou()`, que não usam
  `input()`.

Assim, personagens, inimigos e itens são reaproveitados sem alteração, e
só a interface muda.

## Testes

```bash
pytest
pytest -v     # mais detalhes
```

## Fluxo de desenvolvimento

- Cada funcionalidade possui uma **issue**.
- Cada issue é desenvolvida em uma **branch própria** (ex.: `feature/ataque-guerreiro`).
- Não desenvolver diretamente na `main`.

```bash
git checkout -b feature/ataque-guerreiro
git add .
git commit -m "feat: implementa ataque do guerreiro"
git push -u origin feature/ataque-guerreiro
```

Depois do push, abra um Pull Request no GitHub.

Regras do Pull Request:
- Deve ser revisado por outro aluno.
- Os testes devem passar antes do merge.

## Solução de problemas

| Problema | Solução |
|----------|---------|
| `ImportError: attempted relative import...` | Execute com `python -m src.main` na raiz, e não `python main.py` |
| Erro ao instalar o `pygame` ("building wheels") | Use `pip install pygame-ce` |
| `AttributeError: 'Batalha' object has no attribute 'jogador_atacar'` | Atualize `src/batalha.py` com os métodos `jogador_*` |

## Autores

- Paulo Enrique Pérez González
- Thiago Laurino Silva