import sys

if sys.platform == "win32":
    import msvcrt
else:
    import select
    import termios
    import tty

def get_keypress():
    if sys.platform == "win32":
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try:
                return key.decode().lower()
            except:
                return ''
        return ''
    else:
        # Configura o terminal para modo raw
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            # Usa select para saber se dados estão prontos para ler (com tempo zero, não bloqueia)
            dr, _, _ = select.select([sys.stdin], [], [], 0)
            if dr:
                ch = sys.stdin.read(1)
                return ch.lower()
            return ''
        finally:
            # Restaura configurações do terminal
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)