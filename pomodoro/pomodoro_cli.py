import time
from datetime import timedelta
from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.table import Table
from utils.get_keypress import get_keypress

from .pomodoro_session import PomodoroSession
from .config_file import ConfigFile

class PomodoroCLI:
    def __init__(self):
        self.config = ConfigFile()
        self.session = PomodoroSession(cycles_config=self.config.settings.get("cycles", 4))
        self.is_running = True
        self.console = Console()
        self.MENU_OPTIONS = {
            "1": "work",
            "2": "short_break",
            "3": "long_break"
        }        
        self.COLORS = {
            "work": "red",
            "short_break": "blue",
            "long_break": "green"
        }

    def show_about_message(self):        
        self.console.clear()
        self.console.print("🍅 Pomodoro Terminal 🍅", style="bold red")
        self.console.print("─" * 63, style="dim")
        self.console.print("Sobre a Técnica Pomodoro:", style="bold")        
        self.console.print('A técnica Pomodoro foi criada pelo italiano Francesco Cirillo, no final dos anos 1980, para ajudar no foco e na produtividade. Ela consiste em dividir o trabalho em períodos de 25 minutos de foco total, chamados "Pomodoros", intercalados com descansos curtos de 5 minutos. Após completar quatro Pomodoros, faz-se uma pausa maior, de 15 minutos. Essa alternância entre concentração e descanso mantém o cérebro focado na tarefa, evitando o cansaço e ajudando a restaurar a energia e a atenção.')
        self.console.print("─" * 63, style="dim")
            
        input("Pressione [ENTER] para continuar...")
        
        self.console.clear()
        self.console.print("🍅 Pomodoro Terminal 🍅", style="bold red")
        self.console.print("─" * 63, style="dim")            
        self.console.print("Sobre o Pomodoro Terminal:", style="bold")        
        self.console.print('O Pomodoro Terminal é uma aplicação simples, desenvolvida como um exercício didático em Python. Nela, implementei um temporizador para a técnica Pomodoro, utilizando o terminal como interface com o usuário.\nA aplicação monitora o tempo das três fases da técnica, emitindo um alerta sonoro discreto ao final de cada fase e indicando a próxima etapa, que inicia mediante comando do usuário. Os tempos e nomes das fases podem ser personalizados no menu "Configurações", adaptando-se às suas preferências.\nAo encerrar uma sessão, o programa exibe um resumo do tempo total acumulado em cada fase, oferecendo uma visão clara do seu desempenho.')
        self.console.print("─" * 63, style="dim")
        
        input("Pressione [ENTER] para continuar...") 
        
        self.console.clear()
        self.console.print("🍅 Pomodoro Terminal 🍅", style="bold red")
        self.console.print("─" * 63, style="dim") 
        self.console.print("Sobre o Autor:", style="bold")        
        self.console.print('Joel De Conto, Engenheiro de Controle e Automação e desenvolvedor iniciante. https://github.com/joeldc94/')
        self.console.print("─" * 63, style="dim")
            
        input("Pressione [ENTER] para voltar ao Menu inicial...") 
            
        self.show_idle_menu()
                
    def show_idle_menu(self):
        settings = self.config.settings
        self.console.clear()
        
        # Cabeçalho (igual ao render_status)
        self.console.print("🍅 Pomodoro Terminal 🍅", style="bold red")
        self.console.print("─" * 63, style="dim")
        
        # Última sessão, se existir
        if self.session.phase_history and self.session.phase_history[-1]:
            last_phase = self.session.phase_history[-1]
            self.console.print("📊 ", style="cyan", end="")
            self.console.print("Última sessão: ", style="dim", end="")
            self.console.print(f"{last_phase.label}", style="bold " + self.COLORS[last_phase.name], end="")
            self.console.print(" | Tempo: ", style="dim", end="")
            self.console.print(f"{last_phase.get_formatted_elapsed_time()}", style="cyan")
            self.console.print("─" * 63, style="dim")
        
        
        self.console.print("⌨️  ", style="yellow", end="")
        self.console.print("Nenhuma fase ativa. Escolha uma opção:", style="dim")
        
        # Menu de fases
        self.console.print("Fases: ", style="dim", end="")
        
        # Opções de fases
        self.console.print("[1] ", style="bold white", end="")
        self.console.print(f"{settings['work']['label']}", style="bold " + self.COLORS["work"], end="")
        self.console.print(" | ", style="dim", end="")
        
        self.console.print("[2] ", style="bold white", end="")
        self.console.print(f"{settings['short_break']['label']}", style="bold " + self.COLORS["short_break"], end="")
        self.console.print(" | ", style="dim", end="")
        
        self.console.print("[3] ", style="bold white", end="")
        self.console.print(f"{settings['long_break']['label']}", style="bold " + self.COLORS["long_break"], end="\n")
        
        # Outras opções (configurações, sobre e sair)
        self.console.print("Outras opções: ", style="dim", end="")
        self.console.print("[S] ", style="bold", end="")
        self.console.print("Configurações", style="bold", end="")
        self.console.print(" | ", style="dim", end="")
        
        self.console.print("[A] ", style="bold", end="")
        self.console.print("Sobre", style="bold", end="")
        self.console.print(" | ", style="dim", end="")
                
        self.console.print("[Q] ", style="bold", end="")
        self.console.print("Sair", style="bold", end="\n")
        self.console.print("─" * 63, style="dim")
        
    def show_final_message(self):
        settings = self.config.settings
        self.console.clear()
        self.console.print("🍅 Pomodoro Terminal 🍅", style="bold red")
        self.console.print("─" * 63, style="dim")

        self.console.print("[bold underline]📊 Resumo da sessão:[/bold underline]\n")

        table = Table(show_header=False, box=None)
        table.add_column("Fase", style="bold")
        table.add_column("Tempo", style="cyan")

        table.add_row(f"🧠 {settings['work']['label']}", self.session.get_time_str('work'))
        table.add_row(f"😌 {settings['short_break']['label']}", self.session.get_time_str('short_break'))
        table.add_row(f"🛌 {settings['long_break']['label']}", self.session.get_time_str('long_break'))

        self.console.print(table)
        self.console.print("\n[bold green]👋 Até a próxima![/bold green]\n")

    def render_status(self):
        phase = self.session.current_phase
        
        # Sem fase ativa
        if not phase or not hasattr(phase, "get_formatted_elapsed_time"):
            content = Text()
            content.append("🍅 Pomodoro Terminal 🍅\n", style="bold red")
            content.append("\n⏹️  ", style="yellow")
            content.append("Nenhuma fase ativa no momento\n\n", style="bold")
            content.append("Pressione: ", style="dim")
            content.append("[F] ", style="bold green")
            content.append("Nova fase  |  ", style="dim")
            content.append("[Q] ", style="bold red")
            content.append("Sair", style="dim")
            return content
        
        elapsed = phase.get_formatted_elapsed_time()
        status_emoji = "⏸️" if phase.is_paused else "▶️"
        status_color = "yellow" if phase.is_paused else "cyan" 
        status_text = "Em pausa" if phase.is_paused else "Executando"
        isFinished = phase.is_finished()

        # Cabeçalho
        content = Text()
        content.append("🍅 Pomodoro Terminal 🍅\n", style="bold red")
        content.append("─" * 63 + "\n", style="dim")
        
        # Controles (sempre visível)
        content.append("Controles: ", style="dim")
        content.append("[P] ", style="bold")
        content.append("Pausar", style="bold")
        content.append(" |  ", style="dim")
        content.append("[R] ", style="bold")
        content.append("Retomar", style="bold")
        content.append(" |  ", style="dim")
        content.append("[F] ", style="bold")
        content.append("Finalizar", style="bold")
        content.append(" | ", style="dim")

        content.append("[Q] ", style="bold")
        content.append("Sair\n", style="bold")
        content.append("─" * 63 + "\n", style="dim")

        # Informações da fase
        content.append("Fase: ", style="dim")
        content.append(f"{phase.label}\n", style="bold " + self.COLORS[phase.name])
        
        content.append("Duração: ", style="dim")
        content.append(f"{phase.duration_minutes} minutos\n", style="cyan")
                
        content.append("Tempo: ", style="dim")
        content.append(f"{elapsed}\n", style="cyan")
        
        content.append(f"{status_emoji}  Status: ", style="dim")
        content.append(f"{status_text}\n", style=status_color)

        # Mensagem especial quando a fase termina
        if isFinished:
            overtime_seconds = phase.get_elapsed_time() - phase.duration_seconds
            overtime_str = str(timedelta(seconds=max(0, int(overtime_seconds))))
            
            content.append("─" * 63 + "\n", style="dim green")
            content.append("✅ ", style="bold green")
            content.append("Fase finalizada! ", style="bold green")
            
            content.append("Tempo extra: ", style="bold yellow")
            content.append(f"{overtime_str}\n", style="yellow")
            
            content.append("[ESPAÇO] ", style="bold bright_yellow")
            content.append("para iniciar: ", style="dim")
            content.append(f"{self.config.settings[self.session.next_phase]['label']}\n", style="italic " + self.COLORS[self.session.next_phase])
            
            content.append("(O tempo continua contando até você finalizar)\n", style="dim italic")
            content.append("─" * 63, style="dim green")

        return content

    def _handle_phase_keypress(self, phase, is_finished):
        key = get_keypress()
        if key == 'p':
            self.session.pause_phase()
        elif key == 'r':
            self.session.resume_phase()
        elif key == 'f':
            self.session.finalize_phase()
            return False  # encerra fase
        elif key == ' ' and is_finished:
            self.session.finalize_phase()
            self.next_phase_to_run = self.session.next_phase
            return False
        elif key == 'q':
            self.session.finalize_phase()
            self.is_running = False
            return False
        return True  # continua rodando fase

    def run_phase(self, phase_name):
        # Inicia a fase com as configurações recebidas
        phase_config = self.config.settings[phase_name]
        self.session.start_phase(phase_name, phase_config["label"], self.COLORS[phase_name], phase_config["duration"])
        current_phase = self.session.current_phase

        self.console.clear()
        last_render = None
        next_phase_to_run = None

        with Live(self.render_status(), console=self.console, refresh_per_second=4) as live:
            while current_phase and self.is_running:
                time.sleep(0.25)

                # Alerta sonoro se fase terminou pela primeira vez
                if current_phase.should_alert_finish():
                    self.session.alert_phase_end()

                current_render = self.render_status()
                if current_render != last_render:
                    live.update(current_render)
                    last_render = current_render

                # Processa a entrada do usuário
                keep_running = self._handle_phase_keypress(
                    current_phase, is_finished=current_phase.is_finished()
                )
                
                # Se o handler retorna False, é hora de encerrar o loop da fase
                if not keep_running:
                    # Atualiza possível próxima fase se finalizou com espaço
                    next_phase_to_run = getattr(self, "next_phase_to_run", None)
                    # Remove atributo para evitar resíduo
                    if hasattr(self, "next_phase_to_run"):
                        delattr(self, "next_phase_to_run")
                    break

        return next_phase_to_run
                  
    def run(self):
        show_idle_menu = True
        while self.is_running:
            if show_idle_menu:
                self.show_idle_menu()
                show_idle_menu = False  # só exibe na transição
            key = get_keypress().lower()
            phase = self.MENU_OPTIONS.get(key)
            if phase:
                while phase and self.is_running:
                    next_phase = self.run_phase(phase)
                    phase = next_phase
                show_idle_menu = True   # volta ao menu após as fases
            elif key == 's':
                self.console.clear()
                self.config.interactive_setup()
                self.session.cycles_config = self.config.settings.get("cycles", 4)
                show_idle_menu = True  # sempre mostra menu após mexer nas configs
            elif key == 'a':
                self.console.clear()
                self.show_about_message()
                show_idle_menu = True  # sempre mostra menu após mexer nas configs
            elif key == 'q':
                self.is_running = False
                break
            time.sleep(0.2)
        self.show_final_message()                      