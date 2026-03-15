import allure
from playwright.sync_api import Page
from extensions.ui_actions import UIActions
from extensions.web_verifications import WebVerify
from page_objects.web.chuck.chuck_joke_page import ChuckJokePage

class ChuckUIFlows:
    def __init__(self,page:Page):
        self.page = page
        self.joke = ChuckJokePage(page)

    @allure.step("Navigate to a given url")
    def navigate_to_joke(self,url:str)->None:
        UIActions.navigate_to(self.page,url)

    @allure.step("Get Joke Value:")
    def get_joke_value(self) -> str:
        return UIActions.get_text(self.joke.joke_value)
