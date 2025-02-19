from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverProvider:
    @staticmethod
    def _get_chrome_driver():
        options = webdriver.ChromeOptions()
        # Add any specific Chrome options you need here
        options.add_argument("--start-maximized")  # Maximize window on start
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )

    @staticmethod
    def _get_firefox_driver():
        options = webdriver.FirefoxOptions()
        # Add any specific Firefox options you need her
        options.add_argument("--start-maximized")  # Maximize window on starte
        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=options
        )
