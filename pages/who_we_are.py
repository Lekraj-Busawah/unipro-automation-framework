from .base_page import BasePage
from selenium.webdriver.common.by import By


class WhoWeAre(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------
    locators = {
        # Containers / Sections
        "hero section": (By.CSS_SELECTOR, ".hero-block.block"),
        "who eyebrow text": (By.XPATH , "//p[normalize-space()='WHO WE ARE']"),
        "who heading": (By.CSS_SELECTOR , "div[class='typography'] h1"),
        "who intro text block": (By.XPATH , "//p[contains(text(),'We are a team of inquisitive software specialists ')]"),

        # Hero images
        "desktop hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "mobile hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

        # Team block
        "team": (By.CSS_SELECTOR, "#team"),
        "team eyebrow text": (By.CSS_SELECTOR, "div[class='content-block__typography'] p[class='eyebrow']"),
        "team heading": (By.CSS_SELECTOR, "div[class='content-block__typography'] h2"),
        "team intro text block": (By.CSS_SELECTOR, "div[class='content-block__typography'] div[class='intro-feature-text'] p"),
        "team desktop image": (By.CSS_SELECTOR, "img[alt='Unipro Team']"),

        # Culture block
        "culture": (By.CSS_SELECTOR, "#culture"),
        "culture eyebrow text": (By.CSS_SELECTOR, "div[id='culture'] p[class='eyebrow']"),
        "culture heading": (By.CSS_SELECTOR, "div[id='culture'] h2"),
        "culture intro text block": (By.CSS_SELECTOR, "div[id='culture'] div[class='intro-feature-text'] p"),
        "culture grid": (By.CSS_SELECTOR, ".text-grid-block__content"),
        "culture grid item": (By.CSS_SELECTOR, ".text-grid-block__item"),
        "culture grid item title": (By.CSS_SELECTOR, ".text-grid-block__item-title"),
        "culture grid item copy": (By.CSS_SELECTOR, ".text-grid-block__item-copy"),

        # Process block
        "process": (By.CSS_SELECTOR, ".slideshow-block.block.block--white"),
        "process eyebrow text": (By.CSS_SELECTOR, "div[class='slideshow-block__content'] p[class='eyebrow']"),
        "process heading": (By.CSS_SELECTOR, "div[class='slideshow-block__content'] h2"),
        "process intro text block": (By.CSS_SELECTOR, "div[class='slideshow-block__content'] div[class='intro-feature-text']"),
        "process desktop image": (By.XPATH, "//div[@class='slideshow-block__slide']//img[contains(@class, 'hide-mobile')]"),
        "process mobile image": (By.XPATH, "//div[@class='slideshow-block__slide']//img[contains(@class, 'hide-desktop')]"),

        # Tooling block
        "tooling": (By.CSS_SELECTOR, "div.image-grid-block.block--light-grey"),
        "tooling eyebrow text": (By.XPATH, "//p[contains(text(), 'Our Tooling')]"),
        "tooling heading": (By.XPATH, "//h2[contains(text(), 'Human-Led, AI-Accelerated')]"),
        "tooling intro text block": (By.XPATH, "//div[contains(@class, 'intro-feature-text')]/p[contains(., 'agentic AI')]"),
        "tooling image grid": (By.XPATH, "(//div[contains(@class, 'image-grid-block__grid four-columns')])[1]/div"),
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------

    def get_culture_grid_items(self, locator):
        return self.get_elements(locator)
    
    def get_culture_grid_items_at_index(self, locator, position):
        items = self.get_elements(locator)
        item = items[position - 1]
        return item