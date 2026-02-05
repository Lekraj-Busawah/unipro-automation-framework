from .base_page import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {
        # Containers / Sections
        "hero section": (By.CSS_SELECTOR, ".hero-block.block"),
        "hero heading": (By.CSS_SELECTOR, "div[class='typography'] h1"),
        "intro feature text": (By.XPATH, "(//div[@class='intro-feature-text'])[1]"),
        "why": (By.CSS_SELECTOR, "#why"),
        "feature": (By.CSS_SELECTOR, ".feature-block.block"),

        # Paragraphs
        1: (By.XPATH, "//p[contains(text(),'We are a custom software studio that replaces outd')]"),
        2: (By.XPATH, "//p[contains(text(),'With bespoke systems and Agentic AI, we eliminate ')]"),
        3: (By.XPATH, "//p[normalize-space()='You define the roadmap. We create the advantage.']"),
    
        # Hero Images
        "desktop hero image": (By.XPATH, "//img[@class='hero-block__image hide-mobile']"),
        "mobile hero image": (By.XPATH, "//img[@class='hero-block__image hide-desktop']"),

        # Why Section Details
        "why eyebrow text": (By.CSS_SELECTOR, "div[class='content-block__typography'] p[class='eyebrow']"),
        "why heading": (By.CSS_SELECTOR, "div[class='content-block__typography'] h2"),
        "why intro text block": (By.CSS_SELECTOR, "div[class='content-block__typography'] div[class='intro-feature-text']"),
        "why call to action": (By.XPATH, "//a[@class='link']"),
        "why desktop image": (By.CSS_SELECTOR, ".content-block__image.hide-mobile"),
        "why mobile image": (By.CSS_SELECTOR, ".content-block__image.hide-desktop"),

        # Feature block
        "feature eyebrow text": (By.XPATH, "//p[normalize-space()='The Unipro advantage (pillars of value)']"),
        "feature heading": (By.XPATH, "//h2[contains(text(),'Unrivalled Advantage')]"),
        "feature intro text block": (By.XPATH, "(//div[@class='intro-feature-text'])[3]"),
        "feature call to action": (By.CSS_SELECTOR, ".button.button--primary"),
        "feature image": (By.CSS_SELECTOR, "div[class='feature-block__image'] img[decoding='async']"),
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------

    def get_desktop_hero_image(self, visible_image):
        return self.get_element(visible_image)
    
    def is_image_visible(self):
        """
        Check if image is visible.
        """
        try:
            element = self.wait_for_visibility(self.locators['why'])
            breakpoint
            return element.is_displayed()
        except:
            return False