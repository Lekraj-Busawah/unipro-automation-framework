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
        "hero intro feature text": (By.XPATH, "(//div[@class='intro-feature-text'])[1]"),
        "why": (By.CSS_SELECTOR, "#why"),
        "feature": (By.CSS_SELECTOR, ".feature-block.block"),
        "clients": (By.CSS_SELECTOR, "#clients"),
        "testimonials": (By.CSS_SELECTOR, ".testimonial-list-block.block"),

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

        # Clients block
        "clients eyebrow text": (By.CSS_SELECTOR, "div[class='left-column'] p[class='eyebrow']"),
        "clients heading": (By.CSS_SELECTOR, "div[class='left-column'] h2"),
        "clients intro text block": (By.CSS_SELECTOR, "div[class='left-column'] div[class='intro-feature-text']"),
        "client tile": (By.CSS_SELECTOR, ".image-grid-block__grid-single"),

        # Testimonials block
        "testimonials eyebrow": (By.XPATH, "//p[normalize-space()='Customer Quotes']"),
        "testimonials heading": (By.XPATH, "//h2[contains(text(),'But don’t just take our word for it…')]"),
        "testimonials intro paragraph": (By.XPATH, "//p[contains(text(),'Getting great feedback from our clients')]"),
        "testimonials list": (By.CSS_SELECTOR, ".testimonial-item__content > h3"),
        "testimonials clients": (By.CSS_SELECTOR, ".testimonial-item__content > div"),
        "testimonial decorative icon": (By.ID, "Layer_2"),
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------
        
    def get_number_tiles(self):
        tiles = self.get_elements('client tile')
        return len(tiles)
    
    def get_client_tiles(self):
        return self.get_elements("client tile")

    def get_tile_at_position(self, tile_position):
        tiles = self.get_client_tiles()
        return tiles[int(tile_position) - 1]
    
    def get_desktop_image_from_tile(self, tile):
        return tile.find_element(By.CSS_SELECTOR, "img.hide-mobile")
    
    def get_mobile_image_from_tile(self, tile):
        return tile.find_element(By.CSS_SELECTOR, "img.hide-desktop")
    
    def tile_has_link(self, tile):
        links = tile.find_elements(By.TAG_NAME, "a")
        return len(links) > 0
    
    def get_link_from_tile(self, tile):
        links = tile.find_elements(By.TAG_NAME, "a")
        return links[0] if links else None

    def get_link_href_from_tile(self, tile):
        link = self.get_link_from_tile(tile)
        return link.get_attribute("href") if link else None

    def get_link_target_from_tile(self, tile):
        link = self.get_link_from_tile(tile)
        return link.get_attribute("target") if link else None
    
    def get_testimonials_list(self):
        return self.get_elements("testimonials list")
    
    def get_testimonial_at_position(self, testimonial_position):
        testimonials = self.get_testimonials_list()
        return testimonials[int(testimonial_position) - 1]
    
    def get_testimonials_clients(self):
        return self.get_elements("testimonials clients")
    
    def get_testimonial_client_at_position(self, testimonial_position):
        clients = self.get_testimonials_clients()
        return clients[int(testimonial_position) - 1]

