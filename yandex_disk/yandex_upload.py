import time
from datetime import datetime
from random import randint

import requests
from requests import post


class YandexUpload:

    @staticmethod
    def yandex_upload(token: str, link: str = "https://remanga.org/media/titles/was-the-boss/d5d91079825da4e9151a043a53e7f2eb.jpg"):
        requests.put(
            "https://cloud-api.yandex.net/v1/disk/resources",
            headers={"Authorization": f"OAuth {token}"},
            params={
                "path": "/IMAGES/"
            }
        )
        upload = post("https://cloud-api.yandex.net/v1/disk/resources/upload",
                       headers={"Authorization": f"OAuth {token}"},
                       params={
                                "path": f"/IMAGES/PHOTO_{randint(100000, 199999)}.jpeg/",
                                "url": link,
                       })
        if upload.status_code != 202:
            print(f"ERROR! TRY AGAIN. YOUR ERROR: {upload.status_code}.\nTitle: {upload.json()['description']}")
            return upload.status_code
        print("Успешная загрузка на яндекс диск!")