from datetime import datetime
from .pomodoro_phase import PomodoroPhase
from .sound import Sound
from .config_file import ConfigFile

class PomodoroSession:
    def __init__(self, cycles_config: int) -> None:
        self.cycles_config = cycles_config
        self.current_phase: PomodoroPhase | None = None
        self.next_phase: str = "work"
        self.phase_history: list[PomodoroPhase] = []
        self.cycles_count: int = 0
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
        self.set_next_phase()
        Sound().play_start()

    def set_next_phase(self) -> None:
        if self.current_phase == None:
            self.next_phase = "work"
        elif self.current_phase.name == "short_break":
            self.next_phase = "work"
        elif self.current_phase.name == "long_break":
            self.next_phase = "work"
        elif self.current_phase.name == "work":
            
            work_phases_count = 1 # inicia em 1 pois conta a fase atual
            short_break_phases_count = 0
            long_break_phases_count = 0
            
            for phase in self.phase_history[::-1]:
                if(phase.name == "work"): work_phases_count += 1
                elif(phase.name == "short_break"): short_break_phases_count += 1
                elif(phase.name == "long_break"): long_break_phases_count += 1
                
                if(work_phases_count >= self.cycles_config):
                    break
            
            if(work_phases_count < self.cycles_config):
                self.next_phase = "short_break"
            elif(long_break_phases_count > 0):
                self.next_phase = "short_break"
            else:
                self.next_phase = "long_break"
        
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

        Sound().play_finish()
        
        self.current_phase.finalize()
        elapsed = self.current_phase.get_elapsed_time()

        if "work" in self.current_phase.name.lower():
            self.total_work_time += elapsed
            self.cycles_count += 1
        elif "short_break" in self.current_phase.name.lower():
            self.total_short_break_time += elapsed
        elif "long_break" in self.current_phase.name.lower():
            self.total_long_break_time += elapsed
            
        self.phase_history.append(self.current_phase)
        self.current_phase = None

    def alert_phase_end(self):
        """Toca som de alerta de que o tempo da fase acabou (fim automático)."""
        Sound().play_end()
        
    def _format_time(self, seconds: float) -> str:
        from datetime import timedelta
        return str(timedelta(seconds=int(seconds)))
    
    def get_time_str(self, phase: str) -> str:
        if(phase == "work"): return self._format_time(self.total_work_time)
        elif(phase == "short_break"): return self._format_time(self.total_short_break_time)
        elif(phase == "long_break"): return self._format_time(self.total_long_break_time)
        else: return ""