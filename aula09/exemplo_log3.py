from utils_log import log_decorator
from timer_decorator import time_measure_decorator
import time

@log_decorator
@time_measure_decorator
def soma(x, y):
    time.sleep(2)
    return x + y

soma(2,3)

soma(4,7)