class FileError(Exception):
    def __init__(self, message, code=1930):
        super().__init__(message)
        self.codigo = code
        self.desript = "Error in file or path validation."