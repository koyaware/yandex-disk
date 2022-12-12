from yandex_disk.config import DRIVERS, YANDEX_TOKEN
from yandex_disk.yandex_token import GetToken
from yandex_disk.yandex_upload import YandexUpload

if __name__ == "__main__":
    TOKEN = GetToken(str(DRIVERS["chrome"])).login()
    YandexUpload().yandex_upload(TOKEN,
                           "https://remanga.org/media/titles/was-the-boss/d5d91079825da4e9151a043a53e7f2eb.jpg")