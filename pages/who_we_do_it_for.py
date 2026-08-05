from selenium.webdriver.common.by import By

from .base_page import BasePage


class WhoWeDoItFor(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {

        # Sections
        "hero": (By.CSS_SELECTOR, ".hero-block.block"),
        "leaders": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Leaders We Partner With']]"),
        "enterprise challenges": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]"),
        "client experience": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]"),
        "sector expertise": (By.XPATH, "//div[contains(@class, 'text-grid-block')][.//h2[contains(normalize-space(), 'Sector-Agnostic Expertise')]]"),
        "strategic advantage": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Strategic Advantage We Deliver']]"),
        "final cta": (By.CSS_SELECTOR, ".cta-block.cta-block--cta-side-block"),


        
    }
