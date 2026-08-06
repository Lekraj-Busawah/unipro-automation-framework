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

        # Hero section
        "hero eyebrow text": (By.CSS_SELECTOR, ".hero-block .typography > .eyebrow"),
        "hero heading": (By.CSS_SELECTOR, ".hero-block .typography > h1"),
        "hero intro text block": (By.CSS_SELECTOR, ".hero-block .intro-feature-text"),
        "desktop hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "mobile hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

        # Leaders section
        "leaders eyebrow text": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Leaders We Partner With']]//p[contains(@class, 'eyebrow')]"),
        "leaders heading": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Leaders We Partner With']]//h2"),
        "leaders intro text block": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Leaders We Partner With']]//div[contains(@class, 'intro-feature-text')]"),
        "leaders desktop image": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Leaders We Partner With']]//img[contains(@class, 'hide-mobile')]"),
        "leaders mobile image": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Leaders We Partner With']]//img[contains(@class, 'hide-desktop')]"),

        # Enterprise challenges section
        "enterprise challenges eyebrow text": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//p[contains(@class, 'eyebrow')]"),
        "enterprise challenges heading": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//h2"),
        "enterprise challenges intro text block": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//div[contains(@class, 'intro-feature-text')]"),
        "enterprise challenges list": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//div[contains(@class, 'intro-feature-text')]//ul/li"),
        "enterprise challenges list item": (By.XPATH, "(//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//div[contains(@class, 'intro-feature-text')]//ul/li)[{position}]"),
        "enterprise challenges desktop image": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//img[contains(@class, 'hide-mobile')]"),
        "enterprise challenges mobile image": (By.XPATH, "//div[contains(@class, 'content-block')][.//p[normalize-space()='The Enterprise Challenges We Solve']]//img[contains(@class, 'hide-desktop')]"),

        # Client experience section
        "client experience eyebrow text": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//p[contains(@class, 'eyebrow')]"),
        "client experience heading": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//h2"),
        "client experience intro text block": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//div[contains(@class, 'intro-feature-text')]"),
        "client experience image grid": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//div[contains(@class, 'image-grid-block__grid')]"),
        "client tile": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//div[contains(@class, 'image-grid-block__grid-single')]"),
        "client desktop images": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//img[contains(@class, 'hide-mobile')]"),
        "client mobile images": (By.XPATH, "//div[contains(@class, 'image-grid-block')][.//p[normalize-space()='Our Experience']]//img[contains(@class, 'hide-desktop')]"),

        # Sector expertise section
        "sector expertise eyebrow text": (By.XPATH, "//div[contains(@class, 'text-grid-block')][.//h2[contains(normalize-space(), 'Sector-Agnostic Expertise')]]//p[contains(@class, 'eyebrow')]"),
        "sector expertise heading": (By.XPATH, "//div[contains(@class, 'text-grid-block')][.//h2[contains(normalize-space(), 'Sector-Agnostic Expertise')]]//h2"),
        "sector expertise intro text block": (By.XPATH, "//div[contains(@class, 'text-grid-block')][.//h2[contains(normalize-space(), 'Sector-Agnostic Expertise')]]//div[contains(@class, 'intro-feature-text')]"),
        "sector expertise list": (By.XPATH, "//div[contains(@class, 'text-grid-block')][.//h2[contains(normalize-space(), 'Sector-Agnostic Expertise')]]//div[@class='text-grid-block__item']"),
        
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------
     
    def get_number_tiles(self):
        return len(self.get_client_tiles())

    def get_client_tiles(self):
        return self.get_elements("client tile")

    def get_tile_at_position(self, tile_position):
        return self.get_client_tiles()[int(tile_position) - 1]

    def get_desktop_image_from_tile(self, tile):
        return tile.find_element(By.CSS_SELECTOR, "img.hide-mobile")

    def get_mobile_image_from_tile(self, tile):
        return tile.find_element(By.CSS_SELECTOR, "img.hide-desktop")
