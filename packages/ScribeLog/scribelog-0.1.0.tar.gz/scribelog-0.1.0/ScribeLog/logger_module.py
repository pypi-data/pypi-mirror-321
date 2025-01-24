#logger_module.py
import datetime
from pathlib import Path
from .exception import FileError

class FileLogger:
    def __init__(self, pathLogin=None):
        if pathLogin and self.validate_file_log(pathLogin):
            self.pathLogin = pathLogin
        else:
            self.pathLogin = None
            
    def validate_file_log(self,path_file):
        path = Path(path_file)
    
        # Verificar si el archivo termina en .log
        if not path.name.endswith(".log"):
            raise FileError("The file does not have the .log extension")

        # Verificar si la ruta del archivo existe
        if not path.parent.exists():
            raise FileError("The file path does not exist.")
        return True
    
    def ConfigLog(self, pathLogin: str):
        if pathLogin and self.validate_file_log(pathLogin):
            self.pathLogin = pathLogin
        return self

    def GetPathLogin(self):
        return self.pathLogin
    
    def Log(self, message,time=True):
        if self.pathLogin:
            current_time=""
            if time:
                current_time = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            with open(self.pathLogin, 'a') as file:
                file.write(f"{current_time}{message}\n")
        else:
            raise FileError("Cannot log if a file is not defined.Use ConfigLog method")
 