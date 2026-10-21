# 🎰 Text-Based Slot Machine in Python

Uma simulação interativa de máquina caça-níqueis jogada via linha de comandos (CLI), desenvolvida em Python. O projeto explora conceitos fundamentais de modularização de código, estruturas de dados aninhadas, transposição de matrizes e tratamento de exceções.

---

## 📌 Funcionalidades

- **Gestão de Saldo e Apostas**: Depósito inicial dinâmico, escolha de linhas (1 a 3) e validação de limites de aposta por linha com cálculo de retorno financeiro líquido.
- **Validação Robusta de Entrada**: Tratamento de tipos e valores inválidos (`ValueError`) com laços de repetição contínuos para garantir execução sem falhas.
- **Algoritmo de Sorteio Ponderado**: Distribuição de símbolos com pesos/frequências distintas (`symbol_count`) e extração controlada via listas temporárias sem repetição excessiva por coluna.
- **Transposição Matricial em Tempo Real**: Renderização no terminal das colunas verticais como fileiras horizontais formatadas visualmente com barras divisórias (`|`).
- **Verificação de Vitória com `for...else`**: Algoritmo limpo para validação de símbolos coincidentes por linha e aplicação de multiplicadores diferenciados por raridade.

---

## 🧠 Conceitos Técnicos Aplicados

- **Estruturas de Dados**: Listas aninhadas (matrizes 3x3), dicionários para mapeamento de raridade e valores de multiplicadores.
- **Fluxo Idiomático em Python**: Cláusula `for...else` para evitar *flags* booleanas na verificação de sequências vencedoras.
- **Operador Splat (`*`)**: Desempacotamento de iteráveis para exibição formatada das linhas premiadas.
- **Arquitetura Modular**: Separação clara de responsabilidades em funções independentes (`deposit`, `get_slot_machine_spin`, `print_slot_machine`, `check_winnings`, `spin`, `main`).

---

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Passos

1. Clone este repositório:
   ```bash
   git clone https://github.com/MarceloWSP/slot-machine-python.git
   cd slot-machine-python

    Execute o ficheiro principal:
    Bash

    python main.py

🎮 Exemplo de Uso
Plaintext

What would you like to deposit? $100
Current balance is $100.
Press enter to play (q to quit): 
Enter the amount of lines to bet on 1-3: 2
What would you like to bet? $10
You are betting $10 on 2 lines. Total bet is equal to $20

D | D | D
B | A | C
C | D | A

You won $20.
You won on lines: 1
Current balance is $100.
Press enter to play (q to quit): q
You left with $100.

📚 Créditos e Referências

Projeto desenvolvido como exercício prático de aprendizagem ativa baseado no tutorial Learn Python With This ONE Project! do canal Tech With Tim, com refatoração para tratamento de exceções com try/except e implementação das rotinas de transposição matricial.

https://www.youtube.com/watch?v=th4OBktqK1I&t=2868s