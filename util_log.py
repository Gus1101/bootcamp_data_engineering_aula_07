from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
            "mes_arquivo_de_logs.log",
            format = "{time} {level} {message} {file}",
            level = "INFO"
        )

logger.add(
            "mes_arquivo_de_logs.log",
            format = "{time} {level} {message} {file}",
            level = "CRITICAL"
        )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args,**kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise
    return wrapper