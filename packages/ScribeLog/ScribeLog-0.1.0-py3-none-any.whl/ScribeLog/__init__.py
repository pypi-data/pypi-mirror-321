# __init__.py
from .logger_module import FileLogger
from .exception import FileError

# Crear una instancia global
_FileLogger_instance = FileLogger()

# Exponer los métodos con tipado explícito
def ConfigLog(pathLogin: str):
    return _FileLogger_instance.ConfigLog(pathLogin)

def GetPathLogin():
    return _FileLogger_instance.GetPathLogin()

def Log(message,time=True):
    return _FileLogger_instance.Log(message,time)