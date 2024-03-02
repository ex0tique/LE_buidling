from configparser import ConfigParser
import os

CONFIG_FILE = "config.ini"

def file_exist(filename: str) -> bool:
    return os.path.exists(filename)

def config_file_exist() -> bool:
        return file_exist(CONFIG_FILE)

def get_profil_name() -> str:
        return os.getlogin()

class Config:
    def __init__(self) -> None:
        self.parser = ConfigParser()
        self.profil_name = get_profil_name()
        self.parser.read(CONFIG_FILE) # Parser need to be in Read Mode
        if not self.profil_exist(): # Also create the config.ini file if doesn't exist
            self.create_default_config(self.profil_name)

        self.config_user = self.parser[self.profil_name]
    
    def profil_exist(self) -> bool:
        return self.parser.has_section(self.profil_name)
    
    def create_default_config(self, section_name: str) -> None:
        self.parser[section_name] = {
            "screen_width": 800,
            "screen_height": 600
            }
        self.save_file() 
        self.parser.read(CONFIG_FILE) # Back to read mod

    def section_exist(self, section_name):
        print(section_name)
        print(self.parser.has_section("Johan"))
        return self.parser.has_section(section_name)
    
    def write_setting_data(self, data_name: str, data: str) -> None:
        self.config_user[data_name] = data

    def read_setting_data(self, data_name) -> str:
        return self.config_user[data_name]
    
    def save_file(self) -> None:
        with open(CONFIG_FILE, "w") as f:
            self.parser.write(f)