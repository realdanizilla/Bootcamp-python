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
                "log/meu_arquivo_de_logs2.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

# criando o decorador para usar nas funções
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper

@log_decorator
def soma2(x, y):
    try:
        soma = x + y
        logger.info(f"voce digitou os valores corretos, {x}, {y}, soma= {soma}")
        return soma
    except:
        logger.critical("voce nao digitou valores corretos")

soma2(2,3)
soma2(4,5)
soma2("4",5)

@log_decorator
def falha():
    raise ValueError("Um erro intencional")

soma2(5,3)
try:
    falha()
except:
    pass
