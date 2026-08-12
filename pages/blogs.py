from selenium.webdriver.common.by import By
from .base_page import BasePage


class Blogs(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {

        # Sections
        "hero": (By.CSS_SELECTOR, ".hero-block"),
        "breadcrumb": (By.CSS_SELECTOR, ".sub-menu-bar-block"),
        "featured post": (By.CSS_SELECTOR, ".feature-block"),
        "search bar": (By.CSS_SELECTOR, ".archive-page .search-bar"),
        "search input": (By.CSS_SELECTOR, ".archive-page .search-bar input"),
        "topics": (By.XPATH, "(//div[contains(@class, 'archive-page__content')]//*[contains(@class, 'typography')])[2]"),
        "blog card grid": (By.CSS_SELECTOR, ".archive-page__cards"),
        "final cta": (By.CSS_SELECTOR, ".cta-block"),

        # Hero section
        "hero heading": (By.CSS_SELECTOR, ".hero-block .typography h1"),
        "hero intro text": (By.CSS_SELECTOR, ".hero-block .intro-feature-text p"),
        "hero desktop image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "hero mobile image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

        # Breadcrumb
        "breadcrumb home link": (By.CSS_SELECTOR, ".breadcrumbs .item-home a.bread-link"),
        "breadcrumb current page label": (By.CSS_SELECTOR, ".breadcrumbs .item-current .bread-current"),
        "sub menu bar contact us cta": (By.CSS_SELECTOR, ".sub-menu-bar-block__links a.primary-button"),

        # Featured post
        "featured post heading": (By.CSS_SELECTOR, ".feature-block__typography h2"),
        "featured post cta": (By.CSS_SELECTOR, ".feature-block__typography a.primary-button"),
        "featured post type label": (By.CSS_SELECTOR, ".feature-block .post-icon p"),
        "featured post image": (By.CSS_SELECTOR, ".feature-block__image img"),

    }