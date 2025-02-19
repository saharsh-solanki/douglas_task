import os
import logging
import allure
from datetime import datetime
from base import ScrapBase
from constants import XpathConstants, JSConstants
from config.settings import Config
import time


# Create log directory
log_dir = os.path.join("logs", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "scraper.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# Create reports directory
os.makedirs("reports", exist_ok=True)


class DouglasScraper(ScrapBase):
    def __init__(self, browser=None):
        super().__init__(browser)
        logging.info("DouglasScraper initialized")

    @allure.step("Navigating to base URL")
    def goto_base_url(self):
        logging.info("Navigating to base URL")
        return self.goto(Config.BASE_URL)

    @allure.step("Accepting cookies")
    def accept_cookies(self):
        try:
            logging.info("Attempting to accept cookies")
            self.dynamic_wait(10, 15)

            more_info_button = None

            try:
                more_info_button = self.driver.execute_script(JSConstants.ACCEPT_ALL)
            except Exception as e:
                logging.error(
                    f"Failed to locate 'Accept All' button inside shadow DOM: {e}"
                )
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="accept_cookies_error",
                    attachment_type=allure.attachment_type.PNG,
                )

            if more_info_button:
                try:
                    self.driver.execute_script(JSConstants.SCROLL, more_info_button)
                    self.driver.execute_script(JSConstants.CLICK, more_info_button)
                    logging.info("Successfully clicked 'Accept All' button")
                except Exception as e:
                    logging.error(f"Failed to click 'Accept All' button: {e}")
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="accept_click_error",
                        attachment_type=allure.attachment_type.PNG,
                    )
            else:
                logging.warning("Accept button not found, skipping click.")

            time.sleep(5)
        except Exception as e:
            logging.error(f"Error in accept_cookies: {e}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="accept_cookies_exception",
                attachment_type=allure.attachment_type.PNG,
            )
            raise

    @allure.step("Navigating to Parfum section")
    def goto_parfum(self):
        logging.info("Navigating to Parfum section")
        self.wait_util_element_clickable_by_xpath(XpathConstants.PARFUM).click()
    
    @allure.step("Selecting Sales Promo filter")
    def select_sales_promo_filter(self):
        logging.info("Selecting Sales Promo filter")
        self.wait_util_element_clickable_by_xpath(
            XpathConstants.PROMOTION_DROPDOWN
        ).click()
        self.wait_util_element_clickable_by_xpath(
            XpathConstants.FILTER_CHECKBOX.format("Sale")
        ).click()
    
    @allure.step("Selecting New Promo filter")
    def select_new_promo_filter(self):
        logging.info("Selecting new Promo filter")
        self.wait_util_element_clickable_by_xpath(
            XpathConstants.PROMOTION_DROPDOWN
        ).click()
        self.wait_util_element_clickable_by_xpath(
            XpathConstants.FILTER_CHECKBOX.format("NEU")
        ).click()
        
    @allure.step("Selecting limited Promo filter")
    def select_limited_promo_filter(self):
        logging.info("Selecting limited Promo filter")
        self.wait_util_element_clickable_by_xpath(
            XpathConstants.PROMOTION_DROPDOWN
        ).click()
        self.wait_util_element_clickable_by_xpath(
            XpathConstants.FILTER_CHECKBOX.format("Limitiert")
        ).click()

    @allure.step("Selecting brand filter")
    def select_brand_filter(self, brand_name):
        logging.info(f"Selecting brand filter: {brand_name}")
        self.wait_util_element_clickable_by_xpath(XpathConstants.BRAND_DROPDOWN).click()
        self.search_filter_text(brand_name)
        self.wait_util_element_clickable_by_xpath(XpathConstants.FILTER_CHECKBOX.format(brand_name)).click()
    
    @allure.step("Selecting product type filter")
    def select_product_type_filter(self, product_type_name):
        logging.info(f"Selecting product type filter: {product_type_name}")
        self.wait_util_element_clickable_by_xpath(XpathConstants.PRODUCT_DROPDOWN).click()
        self.dynamic_wait(5,10)
        self.search_filter_text(product_type_name)
        self.wait_util_element_clickable_by_xpath(XpathConstants.FILTER_CHECKBOX.format(product_type_name)).click()
    
    @allure.step("Selecting for whom filter")
    def select_for_whom_filter(self, for_whom_name):
        logging.info(f"Selecting 'For Whom' filter: {for_whom_name}")
        self.dynamic_wait(5, 10)
        self.wait_util_element_clickable_by_xpath(XpathConstants.FOR_WHOM_DROPDOWN).click()
        self.wait_util_element_clickable_by_xpath(XpathConstants.FILTER_CHECKBOX.format(for_whom_name)).click()
    
    @allure.step("Selecting gift for filter")
    def select_gift_for_filter(self, gift_name):
        logging.info(f"Selecting 'Gift For' filter: {gift_name}")
        expand_element = self.wait_util_element_clickable_by_xpath(XpathConstants.SHOW_MORE_FILTER)
        expand_element.click()
        self.wait_util_element_clickable_by_xpath(XpathConstants.GIFT_DROPDOWN).click()
        self.search_filter_text(gift_name)
        self.wait_util_element_clickable_by_xpath(XpathConstants.FILTER_CHECKBOX.format(gift_name)).click()
    
    @allure.step("Using search filter")
    def search_filter_text(self, text):
        logging.info(f"Searching for filter text: {text}")
        search_box = self.wait_util_element_present_by_xpath(XpathConstants.FILTER_SEARCH_BOX)
        search_box.send_keys(text)

    @allure.step("Getting product count")
    def get_products_count(self):
        logging.info("Getting product count")
        products = self.wait_util_elements_present_by_xpath(XpathConstants.PRODUCT_BOX)
        count = len(products)
        logging.info(f"Total products found: {count}")
        allure.attach(
            str(count),
            name="Product Count",
            attachment_type=allure.attachment_type.TEXT,
        )
        return count


if __name__ == "__main__":
    logging.info("Starting DouglasScraper")
    scraper = DouglasScraper()
    scraper.goto_base_url()
    scraper.accept_cookies()
    scraper.goto_parfum()
    scraper.select_sales_promo_filter()
    scraper.get_products_count()
    logging.info("Scraper execution completed")
