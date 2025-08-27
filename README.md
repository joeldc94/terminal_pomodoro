# ⏱️ Terminal Pomodoro

## 📖 Sobre o Projeto

Este é um timer Pomodoro interativo para terminal, desenvolvido com Python com foco em prática e aprendizado de programação orientada a objetos.
O objetivo principal é consolidar conceitos fundamentais, como:

- POO (Programação Orientada a Objetos) → classes, encapsulamento e responsabilidade clara.
- Controle interativo por teclado → pausar, retomar e finalizar fases em tempo real.
- Manipulação de terminal → atualização dinâmica de informações.
- Estrutura modular → organização limpa do código.

## ✨ Funcionalidades

✔️ Ciclos completos de Pomodoro, com tempos configuráveis:
- Foco (tempo configurável)
- Descanso curto
- Descanso longo

✔️ Controle por teclado em tempo real:
- P → Pausar
- R → Retomar
- F → Finalizar fase
- Q → Encerrar tudo

✔️ Menu interativo no terminal
✔️ Acúmulo de tempo real por fase (mesmo após acabar, continua contando até finalizar manualmente)
✔️ Troca manual da próxima fase (quando nenhuma está ativa)
✔️ Interface limpa e responsiva no terminal
✔️ Arquitetura orientada a objetos com separação clara de responsabilidades

## 🖼️ Demonstração

### 📌 Menu Inicial (Idle)

(Insira aqui um print do menu inicial, aguardando escolha de fase)

### 📌 Fase Ativa (Foco)

(Insira aqui um print com a fase ativa rodando e contador atualizado)

### 📌 Menu Interativo

(Insira aqui um print mostrando as opções durante a execução)

## 📂 Estrutura do Projeto
terminal_pomodoro/
│
├── main.py                # Arquivo principal para execução
├── pomodoro/
│   ├── session.py         # Controle da sessão Pomodoro
│   ├── phase.py           # Lógica das fases (foco, descanso)
│   ├── timer.py           # Controle do tempo e contagem
│   ├── console.py         # Manipulação da interface no terminal
│   └── ...
└── README.md

## 🚀 Como Executar
Pré-requisitos

Python 3.10 ou superior

(Opcional) Ambiente virtual: python -m venv venv

### Instalação
#Clonar o repositório
git clone https://github.com/seu-usuario/terminal-pomodoro.git

#Entrar no diretório
cd terminal-pomodoro

#Ativar o ambiente virtual (opcional)
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### Executar
python main.py

## ⚙️ Configurações

Você pode alterar os tempos padrão (em segundos) diretamente na classe Phase:

FOCUS_DURATION = 1500      # 25 minutos
SHORT_BREAK = 300          # 5 minutos
LONG_BREAK = 900           # 15 minutos


## 📌 Próximos Passos

✅ Salvar histórico das sessões em arquivo ou banco de dados.

✅ Gerar relatórios de produtividade.

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.