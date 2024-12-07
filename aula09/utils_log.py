from loguru import logger
from sys import stderr
from functools import wraps


logger.remove()

#printar na tela
logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# salvar no arquivo de log
logger.add(
                "log/meu_arquivo_de_logs3.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

# criando o decorador para usar nas funções
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # adding caller file
        caller_file = __import__('inspect').stack()[1].filename
        bound_logger = logger.bind(caller=caller_file)
        bound_logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs} with caller file: {caller_file}")
        try:
            result = func(*args, **kwargs)
            bound_logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            bound_logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper

