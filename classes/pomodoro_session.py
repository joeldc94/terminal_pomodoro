from datetime import datetime
from .pomodoro_phase import PomodoroPhase

class PomodoroSession:
    def __init__(self) -> None:
        self.current_phase: PomodoroPhase | None = None
        self.phase_history: list[PomodoroPhase] = []
        self.total_work_time = 0
        self.total_short_break_time = 0
        self.total_long_break_time = 0
        
    def start_phase(self, name: str, label: str, color: str, duration_minutes: int) -> None:
        """Inicia uma nova fase com o nome e duração especificados."""
        if self.current_phase:
            print(f"⚠️ Finalize a fase atual antes de iniciar outra.")
            return
        
        self.current_phase = PomodoroPhase(name, label, color, duration_minutes)
        self.current_phase.start()
            
    def pause_phase(self) -> None:
        if self.current_phase:
            self.current_phase.pause()
        else:
            print("⚠️ Nenhuma fase ativa para pausar.")
            
    def resume_phase(self) -> None:
        if self.current_phase:
            self.current_phase.resume()
        else:
            print("⚠️ Nenhuma fase ativa para retomar.")
            
    def finalize_phase(self) -> None:
        """Finaliza a fase atual e registra o tempo acumulado."""
        if not self.current_phase:
            print("⚠️ Nenhuma fase ativa para finalizar.")
            return

        self.current_phase.finalize()
        elapsed = self.current_phase.get_elapsed_time()

        if "work" in self.current_phase.name.lower():
            self.total_work_time += elapsed
        elif "short_break" in self.current_phase.name.lower():
            self.total_short_break_time += elapsed
        elif "long_break" in self.current_phase.name.lower():
            self.total_long_break_time += elapsed
            
        self.phase_history.append(self.current_phase)
        self.current_phase = None
        
    def show_summary(self) -> None:
        """Mostra o tempo acumulado por tipo de fase."""
        print("\n📊 Resumo da sessão:")
        print(f"🧠 Tempo total de foco: {self._format_time(self.total_work_time)}")
        print(f"😌 Descanso curto:      {self._format_time(self.total_short_break_time)}")
        print(f"🛌 Descanso longo:      {self._format_time(self.total_long_break_time)}")

    def _format_time(self, seconds: float) -> str:
        from datetime import timedelta
        return str(timedelta(seconds=int(seconds)))
    
    def get_time_str(self, phase: str) -> str:
        if(phase == "work"): return self._format_time(self.total_work_time)
        elif(phase == "short_break"): return self._format_time(self.total_short_break_time)
        elif(phase == "long_break"): return self._format_time(self.total_long_break_time)
        else: return ""