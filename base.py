import os
import logging
import random
import time
from datetime import datetime
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BrowserConstants
from utils.browser_setup import WebDriverProvider
from config.settings import Config

# Setup logging directory
log_dir = os.path.join("logs", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "scraper.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Setup Allure reports directory
report_dir = "reports"
os.makedirs(report_dir, exist_ok=True)


class ScrapBase:
    def __init__(self, browser: str = BrowserConstants.CHROME):
        if not browser or browser == BrowserConstants.CHROME:
            self.driver = WebDriverProvider._get_chrome_driver()
        elif browser == BrowserConstants.FIREFOX:
            self.driver = WebDriverProvider._get_firefox_driver()
        logging.info("Browser initialized: %s", browser)
        allure.attach(
            f"Browser initialized: {browser}",
            name="Initialization",
            attachment_type=allure.attachment_type.TEXT,
        )

    def goto(self, url):
        self.driver.get(url)
        logging.info("Navigated to URL: %s", url)
        allure.attach(
            f"Navigated to URL: {url}",
            name="Navigation",
            attachment_type=allure.attachment_type.TEXT,
        )

    def wait_util_element_present_by_xpath(
        self, xpath, max_wait=Config.TIMEOUT, element=None
    ):
        try:
            if element:
                return WebDriverWait(element, max_wait).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
            return WebDriverWait(self.driver, max_wait).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except:
            logging.error("Element not found! %s", xpath)
            allure.attach(
                f"Element not found: {xpath}",
                name="Error",
                attachment_type=allure.attachment_type.TEXT,
            )
    
    def wait_util_element_clickable_by_xpath(
        self, xpath, max_wait=Config.TIMEOUT, element=None
    ):
        try:
            if element:
                return WebDriverWait(element, max_wait).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
            return WebDriverWait(self.driver, max_wait).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
        except:
            logging.error("Element not found! %s", xpath)
            allure.attach(
                f"Element not found: {xpath}",
                name="Error",
                attachment_type=allure.attachment_type.TEXT,
            )


    def wait_util_element_present_by_css(self, css, max_wait=Config.TIMEOUT):
        try:
            return WebDriverWait(self.driver, max_wait).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css))
            )
        except:
            logging.error("Element not found! %s", css)
            allure.attach(
                f"Element not found: {css}",
                name="Error",
                attachment_type=allure.attachment_type.TEXT,
            )

    def wait_util_element_present_by_id(self, id, max_wait=Config.TIMEOUT):
        return WebDriverWait(self.driver, max_wait).until(
            EC.presence_of_element_located((By.ID, id))
        )

    def wait_util_elements_present_by_xpath(self, xpath, max_wait=Config.TIMEOUT):
        try:
            return WebDriverWait(self.driver, max_wait).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
        except:
            return []

    def enter_text_random(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.4))

    def press_enter_key(self, element):
        element.send_keys(Keys.ENTER)

    def enter_text_random_by_xpath(self, xpath, text):
        input_element = self.wait_util_element_present_by_xpath(xpath)
        self.enter_text_random(input_element, text)
        self.press_enter_key(input_element)

    def dynamic_wait(self, min=10, max=Config.TIMEOUT):
        time.sleep(random.uniform(min, max))

    def refresh(self, driver=None):
        if driver:
            driver.refresh()
        else:
            self.driver.refresh()
        logging.info("Page refreshed")
        allure.attach(
            "Page refreshed",
            name="Refresh",
            attachment_type=allure.attachment_type.TEXT,
        )

    def find_element_by_xpath(self, xpath, element=None):
        if element:
            return element.find_element(By.XPATH, xpath)
        else:
            return self.driver.find_element(By.XPATH, xpath)

    def find_elements_by_xpath(self, xpath, element=None):
        if element:
            return element.find_elements(By.XPATH, xpath)
        else:
            return self.driver.find_elements(By.XPATH, xpath)

    def find_element_by_id(self, xpath, element=None):
        if element:
            return element.find_element(By.XPATH, xpath)
        else:
            return self.driver.find_element(By.XPATH, xpath)

    def execute_script(self, script):
        try:
            self.driver.execute_script(script)
            logging.info("Executed script: %s", script)
            allure.attach(
                f"Executed script: {script}",
                name="Script Execution",
                attachment_type=allure.attachment_type.TEXT,
            )
        except:
            logging.error("Failed to execute script: %s", script)
            allure.attach(
                f"Failed to execute script: {script}",
                name="Error",
                attachment_type=allure.attachment_type.TEXT,
            )

    def destroy(self):
        self.driver.quit()
        logging.info("Browser session ended")
        allure.attach(
            "Browser session ended",
            name="Session End",
            attachment_type=allure.attachment_type.TEXT,
        )
