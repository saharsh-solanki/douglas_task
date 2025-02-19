import pytest
from scrapy import DouglasScraper
from utils.helper import save_to_excel


@pytest.fixture(scope="class")
def scraper():
    scraper = DouglasScraper()
    scraper.goto_base_url()
    scraper.accept_cookies()
    scraper.goto_parfum()
    scraper.select_sales_promo_filter()
    yield scraper
    scraper.destroy()


class TestSalePromo:
    @pytest.mark.parametrize(
        "brand, product_type, for_whom, gift",
        [
            ("4711", None, None, None),
            (None, None, "Unisex", None),
            # ("Chanel", "Eau de Parfum", "Women", "Weihnachten")
        ],
    )
    def test_parametrized_sales_promo_filter(
        self, scraper, brand, product_type, for_whom, gift
    ):
        if brand:
            scraper.select_brand_filter(brand)
        if product_type:
            scraper.select_product_type_filter(product_type)
        if for_whom:
            scraper.select_for_whom_filter(for_whom)
        if gift:
            scraper.select_gift_for_filter(gift)

        count = scraper.get_products_count()
        assert (
            count > 0
        ), "No products found for Limited Promo filter"
        
        save_to_excel("Sale", brand, product_type, for_whom, gift, count)
