import os
from pathlib import Path

from dotenv import load_dotenv

TARGET_URL = "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fyandex.ru%2Fdev%2Fdisk%2Fpoligon%2F"

BASE_DIR = Path().resolve()
DRIVER_PATH = BASE_DIR / "drivers"
DRIVERS = {
    "chrome": DRIVER_PATH / "chromedriver.exe"
}

load_dotenv(BASE_DIR.parent / ".env")

YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")