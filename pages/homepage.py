from .base_page import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):
    # locators
    containers = {
        "hero section": (By.CSS_SELECTOR, ".hero-block.block"),
        "heading": (By.CSS_SELECTOR, "div[class='typography'] h1"),
        "intro feature text":  (By.XPATH, "(//div[@class='intro-feature-text'])[1]")
    }

    paragraph_text = {
        1: (By.XPATH, "//p[contains(text(),'We are a custom software studio that replaces outd')]"),
        2: (By.XPATH, "//p[contains(text(),'With bespoke systems and Agentic AI, we eliminate ')]"),
        3: (By.XPATH, "//p[normalize-space()='You define the roadmap. We create the advantage.']")
    }
    hero_image = {
        'desktop hero image': (By.XPATH, "//img[@class='hero-block__image hide-mobile']"),
        'mobile hero image': (By.XPATH, "//img[@class='hero-block__image hide-desktop']")
    }

    # actions
    def is_container_visible(self, element_name):
        locator = self.containers.get(element_name)
        if not locator:
            raise ValueError(f"No locator defined for container: {element_name}")
        
        return self.find_element(locator).is_displayed()
    
    def get_hero_heading_text(self):
        locator = self.containers.get("heading")
        return self.find_element(locator).text.strip()
    
    def get_paragraph_text(self, paragraph_index):
        locator = self.paragraph_text.get(int(paragraph_index))
        return self.find_element(locator).text.strip()
    
    def get_desktop_hero_image(self, visible_image):
        locator = self.hero_image.get(visible_image)
        return self.find_element(locator)

    def is_image_visible(self, image_name):
        locator = self.hero_image.get(image_name)

        return self.find_element(locator).is_displayed()
