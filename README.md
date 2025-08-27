# ⏱️ Terminal Pomodoro
![license](https://img.shields.io/badge/license-MIT-blue)
![python-version](https://img.shields.io/badge/python-3.10%2B-yellow)

## 📖 Sobre o Projeto
Esta é uma implementação funcional de um timer Pomodoro interativo para terminal, desenvolvido com Python com objetivo de aprendizado e prática de programação orientada a objetos.

### 🍅 Sobre a Técnica Pomodoro
A Técnica [Pomodoro](https://www.pomodorotechnique.com/welcome/) é um método de gerenciamento do tempo criado no final dos anos 1980 pelo italiano Francesco Cirillo, que tinha como objetivo aumentar sua produtividade nos estudos universitários usando um cronômetro de cozinha em forma de tomate (pomodoro, em italiano).

O método consiste em dividir o trabalho ou estudo em blocos de tempo chamados pomodoros, cada um de 25 minutos de foco total em uma tarefa. Após cada pomodoro, faz-se uma pausa curta de 5 minutos e, após quatro ciclos, uma pausa maior de 15 a 30 minutos. A técnica exige o uso de um cronômetro e uma lista de tarefas, além de evitar interrupções nesses períodos.

A eficácia do método está baseada em estudos que mostram que pausas regulares ajudam a manter o foco e a produtividade por períodos prolongados. Além do benefício direto na realização de tarefas, o Pomodoro também contribui para diminuir a sensação de sobrecarga e para criar uma relação saudável com o tempo.

## ✨ Funcionalidades
- Execução diretamente no terminal, com menu interativo e controle via teclado;
- Ciclos do método Pomodoro gerenciados e contabilizados de maneira simples e intuitiva;
- Alerta sonoro discreto no início e fim de cada fase;
- Possibilidade de personalização das fases, tempos e ciclo;

## 🖼️ Demonstração
### 📌 Menu Inicial
Neste menu, é possível iniciar diretamente uma das 3 fases do ciclo ditando 1, 2 ou 3 no teclado, entrar no menu interativo de Configurações (tecla S), ler as informações sobre o método e sobre a aplicação (tecla A), e finalizar a aplicação (tecla Q).

<img width="620" height="200" alt="pt1" src="https://github.com/user-attachments/assets/c7145144-0348-48f3-ad96-5a9e3cffed45" />

### 📌 Fase Ativa (Foco)
Aqui são mostradas as informações da fase em execução, além do menu de ações: Pausar (tecla P), Retomar a execução após Pausa (tecla R), Finalizar a fase atual e retornar ao menu inicial (tecla F) e encerrar a execução do programa (tecla Q)

<img width="648" height="233" alt="pt2" src="https://github.com/user-attachments/assets/07f7a98f-0bb5-40e5-8a98-9f10f3efcbec" />

### 📌 Menu de personalização de tempos e fases
Permite retornar às configurações iniciais, ou personalizar os tempos e nomes de cada uma das 3 fases, além da quantidade de ciclos de 'Foco' antes de um 'Descanso longo'.

<img width="698" height="238" alt="pt3" src="https://github.com/user-attachments/assets/1918354f-e4ca-4733-8fc9-ecb8d2883db9" />

### 📌 Contabilização dos tempos e resumo final
Ao finalizar a execução, são mostrados os tempos acumulados de cada fase durante a execução do programa.

<img width="687" height="222" alt="pt4" src="https://github.com/user-attachments/assets/dbbdcc7c-fb0c-4d9a-b231-fd814f664622" />

## 🚀 Como Executar

### Execução direta
Faça o download do arquivo PomodoroTerminal.exe presente neste repositório. Execute a aplicação com duplo clique. Uma janela com o prompt de comando será aberta com o programa já em execução.

### Execução via terminal
Faça o download do arquivo PomodoroTerminal.exe, presente na pasta _dist_. Abra o prompt de comando e navegue até a pasta onde está o arquivo e execute 
```
.\PomodoroTerminal.exe
```
A aplicação será executada no próprio prompt.

Ao executar esta aplicação, será criado no mesmo diretório um arquivo chamado _config.json_, que armazena as configurações de execução do programa.


### Execução do projeto
Pré-requisitos:
Python 3.10 ou superior
```
#Clonar o repositório
git clone https://github.com/seu-usuario/terminal-pomodoro.git

#Entrar no diretório
cd terminal-pomodoro

#Ativar o ambiente virtual (opcional)
#source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# instalar as dependências do projeto:
pip install -r requirements.txt

### Executar
python main.py
```

## 📌 Próximos Passos

- Salvar histórico das sessões em arquivo .csv;
- Gerar relatórios de produtividade e estatísticas a partir do histórico;

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.
