import time
from tqdm import tqdm


def progress_bar(message: str):
    bar_format = '{l_bar}{bar}'
    for i in tqdm(range(10), desc=f"{message}", colour='green', bar_format=bar_format):
        time.sleep(0.1)

