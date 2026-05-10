from playwright.sync_api import Page

class AtidAboutPage:
    def __init__(self, page: Page):
        self.page = page
        self.kim_kardashian_card = page.locator("h4:has-text('Kim Kardashian')").locator("..")

