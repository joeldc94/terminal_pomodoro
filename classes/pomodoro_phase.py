from datetime import datetime, timedelta

# classe que representa uma única fase do pomodoro
# Responsável por:
# - Iniciar a contagem de tempo
# - Manter o tempo decorrido mesmo com pausas
# - Permitir Pausa, retomada e finalização
# - Fornecer o tempo total acumulado ao final
class PomodoroPhase:
    def __init__(self, name: str, label: str, color: str, duration_minutes: int) -> None:
        """
        :param name: Nome da fase (ex: 'work', 'short_break', 'long_break')
        :param label: Rótulo da fase (ex: 'Foco', 'Descanso Curto', 'Descanso Longo')
        :param default_duration: Duração padrão em segundos
        """
        self.name = name
        self.label = label
        self.color = color
        self.duration_minutes = duration_minutes
        self.duration_seconds = duration_minutes * 60
        #
        self.start_time = None
        self.pause_time = None
        self.end_time = None
        #
        self.elapsed_seconds = None
        self.is_running = False
        self.is_paused = False
        
    def start(self) -> None:
        """Inicia a contagem da fase."""
        self.start_time = datetime.now()
        self.is_running = True
        self.is_paused = False
        #print(f"\n▶️\tIniciando fase: {self.name} ({self.default_duration // 60} minutos)")
        
    def pause(self) -> None:
        """Pausa a contagem da fase."""
        if self.is_running and not self.is_paused:
            self.pause_time = datetime.now()
            self.is_paused = True
            self.is_running = False
            #print(f"\n⏸️\tFase '{self.name}' pausada.")
            
    def resume(self) -> None:
        """Retoma a contagem da fase após uma pausa."""
        if self.pause_time and self.is_paused:
            now = datetime.now()
            pause_duration = (now - self.pause_time).total_seconds()
            self.start_time += timedelta(seconds=(pause_duration))
            self.is_paused = False
            self.is_running = True
            #print(f"\n▶️\tFase '{self.name}' retomada.")
            
    def finalize(self) -> None:
        """Finaliza a contagem da fase e calcula o tempo decorrido."""
        if self.is_running or self.is_paused:
            self.end_time = datetime.now()
            self.is_running = False
            self.is_paused = False
            self.elapsed_seconds = (self.end_time - self.start_time).total_seconds()
            #print(f"\n✅\tFase '{self.name}' finalizada. Tempo total: {int(self.elapsed_seconds)} segundos.")
            
    def get_elapsed_time(self) -> float:
        """Retorna o tempo decorrido até o momento."""
        if self.start_time is None:
            return 0
        if self.is_paused:
            return (self.pause_time - self.start_time).total_seconds()
        elif self.is_running:
            return (datetime.now() - self.start_time).total_seconds()
        else:
            return self.elapsed_seconds
        
    def get_formatted_elapsed_time(self) -> str:
        """Retorna o tempo decorrido formatado como HH:MM:SS"""
        return str(timedelta(seconds=int(self.get_elapsed_time())))
