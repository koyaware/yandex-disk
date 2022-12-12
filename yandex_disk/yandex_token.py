import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from yandex_disk.config import DRIVERS, TARGET_URL, BASE_DIR


class GetToken(webdriver.Chrome):

    def __init__(self, driver_path: str):
        s = Service(driver_path)
        super().__init__(service=s)

        self.yandex_login = None
        self.yandex_password = None
        self.yandex_token = None

    def login(self):
        self.yandex_login = input("Введите логин: ")
        self.yandex_password = input("Введите пароль: ")
        self.get(TARGET_URL)
        time.sleep(3)
        self.find_element(
            By.XPATH,
            "/html/body/div/div/div[2]/div[2]/div/div/div[2]"
            "/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input",
        ).send_keys(self.yandex_login)
        time.sleep(3)
        self.find_element(
            By.XPATH,
            "/html/body/div/div/div[2]/div[2]/div/div/div[2]/"
            "div[3]/div/div/div/div[1]/form/div[4]/button"
        ).click()
        time.sleep(3)
        self.find_element(
            By.XPATH,
            "/html/body/div/div/div[2]/div[2]/div/div/div[2]/"
            "div[3]/div/div/div/form/div[2]/div[1]/span/input"
        ).send_keys(self.yandex_password)
        time.sleep(3)
        self.find_element(
            By.XPATH,
            "/html/body/div/div/div[2]/div[2]/div/div/div[2]/"
            "div[3]/div/div/div/form/div[3]/button"
        ).click()
        time.sleep(10)
        self.switch_to.frame(self.find_element(By.XPATH, "/html/body/div[3]/div/div/span/section/div[1]/div[1]"
                                                         "/div/section/div/div/section/div/div/div/div[1]/div/"
                                                         "section/div/div/div/div[4]/section/div/div/iframe"))
        time.sleep(3)
        self.yandex_token = self.find_element(By.XPATH, "/html/body/div/section/div[1]/span/input").get_attribute('value')
        time.sleep(5)
        self.write_info()
        return self.yandex_token

    def write_info(self):
        with open("info.env", "w", encoding="utf-8") as file:
            user_info = f"YANDEX_LOGIN={self.yandex_login}" \
                        f"\nYANDEX_PASSWORD={self.yandex_password}" \
                        f"\nYANDEX_TOKEN={self.yandex_token}"
            file.write(user_info)
        return True

    def __del__(self):
        self.close()
        self.quit()
        print("Браузер закрыт.")