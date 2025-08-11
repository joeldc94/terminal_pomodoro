import json
import os
import time

class ConfigFile:
    # diretório padrão para o arquivo config.json é no mesmo diretório do arquivo pomodoro.py
    DEFAULT_CONFIG_FILE_PATH = os.path.abspath(os.path.join(os.getcwd(), ".", "config.json"))
    DEFAULT_CONFIGURATIONS = {
        "work": {
            "label": "Foco",
            "color": "red",
            "duration": 25
        },
        "short_break": {
            "label": "Descanso Curto",
            "color": "blue",
            "duration": 5
        },
        "long_break": {
            "label": "Descanso Longo",
            "color": "green",
            "duration": 15
        },
        "cycles": 4
    }


    def __init__(self, file_path: str = None) -> None:
        self.file_path = file_path or self.DEFAULT_CONFIG_FILE_PATH
        self.settings = {}
        
        # leitura inicial das configurações do arquivo
        self.read_config()

                
    def read_config(self):
        """Lê configurações do arquivo JSON e atribui ao objeto."""
        if not os.path.exists(self.file_path):
            print(f"Aviso: Arquivo de configurações {self.file_path} não encontrado. Será criado uma rquivo com valores padrão.")
            self.write_default_config()
            return                
        with open(self.file_path, 'r', encoding='utf-8') as f:
            try:
                self.settings = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Erro ao ler o arquivo de configuração: {e}")
                self.settings = {}
                
    
                
    def print_config(self):
        print("Configurações:")
        for key, value in self.settings.items():
            print(f"{key}: {value}")
            
    def write_default_config(self):
        """Escreve o arquivo config.json com as configurações padrão."""
        self.settings = self.DEFAULT_CONFIGURATIONS.copy()
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4, ensure_ascii=False)
        print("Arquivo de configuração criado com valores padrão.")

    def reset_to_default(self):
        """Restaura config.json para os valores padrão."""
        self.write_default_config()
        print("Configuração restaurada para os padrões iniciais.")
        
    def interactive_setup(self):
        """Solicita interativamente as configurações ao usuário e grava no arquivo."""
        print("Configuração interativa do Pomodoro.\nPressione Enter para manter os valores padrão mostrados entre parênteses.\n")

        def ask_int(prompt, default):
            while True:
                user_input = input(f"{prompt} ({default}): ").strip()
                if not user_input:
                    return default
                if user_input.isdigit() and int(user_input) > 0:
                    return int(user_input)
                else:
                    print("Por favor, insira um número inteiro positivo.")

        def ask_str(prompt, default):
            user_input = input(f"{prompt} ({default}): ").strip()
            return user_input if user_input else default

        reset = input("Deseja restaurar as configurações padrões? (S/N): ").strip().lower() == 's'
        if reset:
            self.reset_to_default()
            print("\nRetornando ao menu inicial...")
            time.sleep(2)
            return

        # Carregar valores atuais como padrão
        settings = self.settings if self.settings else self.DEFAULT_CONFIGURATIONS.copy()

        # fases e nomes usados internamente
        phases = ['work', 'short_break', 'long_break']

        # Solicitar tempos de cada fase
        for phase_key in phases:
            phase_info = settings[phase_key]
            prompt = f"Insira o tempo em minutos da fase '{phase_info['label']}'"
            phase_info['duration'] = ask_int(prompt, phase_info['duration'])
            settings[phase_key] = phase_info

        # Solicitar a quantidade de ciclos
        cycles = settings.get('cycles', 4)
        settings['cycles'] = ask_int(
            "Insira a quantidade de ciclos 'Foco' + 'Descanso Curto' antes da fase 'Descanso Longo'", cycles)

        # Solicitar os nomes de cada fase — mostrar a chave interna e o valor atual
        for phase_key in phases:
            phase_info = settings[phase_key]
            prompt = f"Insira o nome da fase '{phase_key}'"
            phase_info['label'] = ask_str(prompt, phase_info['label'])
            settings[phase_key] = phase_info

        # Solicitar as cores
        for phase_key in phases:
            phase_info = settings[phase_key]
            prompt = f"Insira a cor da fase '{phase_info['label']}'"
            phase_info['color'] = ask_str(prompt, phase_info['color'])
            settings[phase_key] = phase_info

        # Atualiza o atributo da classe
        self.settings = settings
        #chama o método para salvar as configurações atuais no arquivo json
        self.save()
        
        print("\nConfigurações atualizadas e salvas com sucesso.\nRetornando ao menu inicial...")
        time.sleep(2)
        return

    def save(self):
        """Salva as configurações atuais no arquivo .json"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4, ensure_ascii=False)