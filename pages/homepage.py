from .base_page import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {
        # Containers / Sections
        "hero section": (By.CSS_SELECTOR, ".hero-block.block"),
        "heading": (By.CSS_SELECTOR, "div[class='typography'] h1"),
        "intro feature text": (By.XPATH, "(//div[@class='intro-feature-text'])[1]"),
        "why": (By.CSS_SELECTOR, "#why"),

        # Paragraphs
        1: (By.XPATH, "//p[contains(text(),'We are a custom software studio that replaces outd')]"),
        2: (By.XPATH, "//p[contains(text(),'With bespoke systems and Agentic AI, we eliminate ')]"),
        3: (By.XPATH, "//p[normalize-space()='You define the roadmap. We create the advantage.']"),
    
        # Hero Images
        "desktop hero image": (By.XPATH, "//img[@class='hero-block__image hide-mobile']"),
        "mobile hero image": (By.XPATH, "//img[@class='hero-block__image hide-desktop']"),

        # Why Section Details
        "eyebrow text": (By.CSS_SELECTOR, "div[class='content-block__typography'] p[class='eyebrow']"),
        "heading": (By.CSS_SELECTOR, "div[class='content-block__typography'] h2"),
        "intro text block": (By.CSS_SELECTOR, "div[class='content-block__typography'] div[class='intro-feature-text']"),
        "call to action": (By.XPATH, "//a[@class='link']"),
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------

    def get_desktop_hero_image(self, visible_image):
        return self.get_element(visible_image)