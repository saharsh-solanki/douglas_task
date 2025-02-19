class XpathConstants:
    COOKIE = '//button[@data-testid="uc-accept-all-button"]'
    PARFUM = "//a[contains(text(), 'PARFUM')]"

    PROMOTION_DROPDOWN = "//div[@data-testid = 'flags']"
    PRODUCT_DROPDOWN = "//div[@data-testid = 'classificationClassName']"
    BRAND_DROPDOWN = "//div[@data-testid = 'brand']"
    GIFT_DROPDOWN = "//div[@data-testid = 'Geschenk für']"
    FOR_WHOM_DROPDOWN = "//div[@data-testid = 'gender']"

    FILTER_SEARCH_BOX = "//input[@name='facet-search']"
    SHOW_MORE_FILTER = "//button[contains(text(), 'Mehr Filter anzeigen')]"
    
    FILTER_CHECKBOX = "//a[@class='link link--text facet-option' and @role='checkbox'][.//div[normalize-space(text())='{}']]"
    PRODUCT_BOX = "//div[contains(@class, 'product-grid-column')]"


class JSConstants:
    ACCEPT_ALL = "return document.querySelector('#usercentrics-root').shadowRoot.querySelector('button[data-testid=\"uc-accept-all-button\"]');"
    SCROLL = "arguments[0].scrollIntoView(true);"
    CLICK = "arguments[0].click();"


class CSSConstants:
    ACCEPT_BTN = 'button[data-testid="cookie-accept-button"]'


class BrowserConstants:
    CHROME = "chorme"
    FIREFOX = "firefox"
