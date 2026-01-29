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
        "why eyebrow": (By.CSS_SELECTOR, "div[class='content-block__typography'] p[class='eyebrow']"),
        "why heading": (By.CSS_SELECTOR, "div[class='content-block__typography'] h2"),
        "why intro text": (By.CSS_SELECTOR, "div[class='content-block__typography'] div[class='intro-feature-text']"),
        "why cta": (By.XPATH, "//a[@class='link']"),
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------
    
    def get_hero_heading_text(self):
        locator = self.locators.get("heading")
        return self.find_element(locator).text.strip()
    
    def get_paragraph_text(self, paragraph_index):
        locator = self.locators.get(int(paragraph_index))
        return self.find_element(locator).text.strip()
    
    def get_desktop_hero_image(self, visible_image):
        locator = self.locators.get(visible_image)
        return self.find_element(locator)

    def is_image_visible(self, image_name):
        locator = self.locators.get(image_name)

        return self.find_element(locator).is_displayed()
