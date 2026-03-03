import logging       # стандартная библиотека Python для логирования
import sys           # нужен для вывода логов в консоль
from pathlib import Path  # удобно работать с путями к файлам


# Папка для логов
LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True) # если папка уже есть, не создаём заново

# Путь к файлу логов
LOG_FILE = LOG_DIR / 'tests.log'


def setup_logger() -> None:
    """
    Настройка логирования для всего проекта:
    формат логов,
    уровни логирования,
    запись в файл,
    вывод в консоль
    """
    logging.basicConfig(
        level=logging.INFO, # уровень логирования: INFO и выше будут отображаться
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        # %(asctime)s — время события
        # %(levelname)s — уровень (INFO, WARNING, ERROR и т.д.)
        # %(name)s — имя модуля, откуда вызван лог
        # %(message)s — само сообщение
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'), # пишем в файл
            logging.StreamHandler(sys.stdout), # и одновременно в консоль
        ],
    )