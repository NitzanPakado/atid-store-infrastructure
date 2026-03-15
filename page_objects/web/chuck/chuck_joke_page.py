from playwright.sync_api import Page

class ChuckJokePage:
    def __init__(self,page:Page):
        self.joke_value = page.locator("[id='joke_value']")