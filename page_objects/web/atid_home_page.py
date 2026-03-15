from playwright.sync_api import Page

class AtidHomePage:
    def __init__(self, page: Page):
        self.men_menu_item = page.locator("a.menu-link[href*='/product-category/men/']").first
        self.accessories_menu_item = page.locator("a.menu-link[href*='/product-category/accessories/']").first
        self.store_menu_item = page.locator("a.menu-link[href*='/store/']").first
        self.search_icon = page.locator(".astra-search-icon").first
