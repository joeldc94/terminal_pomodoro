import time
from rich.console import Console
from rich.live import Live
from rich.text import Text
from utils.get_keypress import get_keypress

from .pomodoro_session import PomodoroSession
from .config_file import ConfigFile

class PomodoroCLI:
    def __init__(self):
        self.session = PomodoroSession()
        self.is_running = True
        self.console = Console()
        self.config = ConfigFile()

    def show_idle_menu(self):
        settings = self.config.settings
        self.console.clear()
        self.console.print("🍅 Pomodoro Terminal 🍅")
        # mostra a última fase, caso exista
        if(self.session.phase_history and self.session.phase_history[-1]): 
            last_phase = self.session.phase_history[-1]
            self.console.print(f"📊 Última sessão: {last_phase.label} | Tempo: {last_phase.get_formatted_elapsed_time()}\n")
            
        self.console.print("Menu de Fases:")
        self.console.print(f"[1] Iniciar {settings['work']['label']}\t|\t[2] {settings['short_break']['label']}\t|\t[3] {settings['long_break']['label']}\n[S] Configurações\t|\t[Q] Sair\n")
        self.console.print("Nenhuma fase ativa. Escolha uma opção:")

    def show_final_message(self):
        settings = self.config.settings
        self.console.clear()        
        self.console.print("🍅 Pomodoro Terminal 🍅")
        #
        self.console.print("\n📊 [strong]Resumo da sessão:[strong/]")
        self.console.print(f"🧠 Tempo total em {settings['work']["label"]}:\t{self.session.get_time_str('work')}")
        self.console.print(f"😌 Tempo total em {settings['short_break']["label"]}:\t{self.session.get_time_str('short_break')}")
        self.console.print(f"🛌 Tempo total em {settings['long_break']["label"]}:\t{self.session.get_time_str('long_break')}")
        #
        self.console.print("\n👋 Até a próxima!\n")
        
    def render_status(self):
        phase = self.session.current_phase
        
        if not phase or not hasattr(phase, "get_formatted_elapsed_time"):
            return f"⏹️ Nenhuma fase ativa no momento.\n\nPressione:\n[F] Iniciar nova fase\n[Q] Sair\n\n {self.session.phase_history[0]}\n{self.session.current_phase}"
    
        elapsed = phase.get_formatted_elapsed_time()
        status = 'Em pausa' if phase.is_paused else 'Executando'
        
        elapsed_seconds = phase.get_elapsed_time()
        isFinished = phase.is_running and not phase.is_paused and elapsed_seconds and elapsed_seconds >= phase.duration_seconds
        finishedMessage = f"✅ Fase '{phase.label}' finalizada ({phase.duration_minutes} minutos)." if isFinished else ""

        content = (
            "🍅 Pomodoro Terminal 🍅\n\n"
            "Controles: [P] Pausar  [R] Retomar  [F] Finalizar  [Q] Sair\n\n"
            f"⏱️ Fase: {phase.label}\n"
            f"Duração: {phase.duration_minutes} minutos\n"
            f"Status: {status}\n"
            f"Tempo: {elapsed}\n"
            f"{finishedMessage}\n"
        )
        return content

    def run_phase(self, phase_name):
        # inicia a fase com as configurações recebidas
        phase_config = self.config.settings[phase_name]
        self.session.start_phase(phase_name, phase_config["label"], phase_config["color"], phase_config["duration"])
        current_phase = self.session.current_phase
        # limpa o terminal
        self.console.clear()

        last_render = ""

        with Live(Text(self.render_status()), console=self.console, refresh_per_second=4) as live:
            while current_phase != None and self.is_running:
                time.sleep(0.25)

                current_render = self.render_status()
                if current_render != last_render:
                    live.update(Text(current_render))
                    last_render = current_render

                key = get_keypress()
                if key == 'p':
                    self.session.pause_phase()
                elif key == 'r':
                    self.session.resume_phase()
                elif key == 'f':
                    self.session.finalize_phase()
                    break
                elif key == 'q':
                    self.session.finalize_phase()
                    self.is_running = False
                    break

    def run(self):
        show_menu = True
        while self.is_running:
            if not self.session.current_phase:
                if(show_menu):
                    self.show_idle_menu()
                    show_menu = False
                key = get_keypress()
                if key == '1':
                    self.run_phase("work")
                    show_menu = True
                elif key == '2':
                    self.run_phase("short_break")
                    show_menu = True
                elif key == '3':
                    self.run_phase("long_break")
                    show_menu = True
                elif key == 's':
                    self.console.clear()
                    self.config.interactive_setup()
                    show_menu = True
                elif key == 'q':
                    self.is_running = False
                
            time.sleep(0.2)  # reduz uso de CPU

        self.show_final_message()