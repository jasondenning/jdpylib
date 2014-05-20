class JDError(Exception):
    TPL = "jdpylib Error"
    def __init__(self, msg=None, **kwargs):
        if not msg:
            msg = self.TPL.format(**kwargs)
        self.msg = msg
        super(JDError, self).__init__(msg)


class InvalidYAML(JDError):
    TPL = "Invalid YAML syntax - {error}"
    def __init__(self, msg=None, error=None, **kwargs):
        if isinstance(error, BaseException):
            error = error.message()
        if error is None:
            error = "General invalid syntax error"
        super(InvalidYAML, self).__init__(msg, error=error)



# --- File I/O Errors --- #

class InvalidPath(JDError):
    TPL = "Invalid Path - {path}"

class FileExistsNoOverwrite(JDError):
    TPL = "File '{path}' exists and the overwrite flag was not set"
