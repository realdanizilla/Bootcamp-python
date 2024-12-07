from loguru import logger

# print -> logger.info

logger.add("log/meu_arquivo_de_logs.log")

def soma(x, y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

soma(2, 3)


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