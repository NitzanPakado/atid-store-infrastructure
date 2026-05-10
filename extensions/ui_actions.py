import allure
from playwright.sync_api import Locator, Page

from utils.common_ops import load_config

CONFIG = load_config()
DEFAULT_TIMEOUT = CONFIG["DEFAULT_COMMAND_TIMEOUT"]

class UIActions:

    @staticmethod
    @allure.step("Navigte to")
    def navigate_to(page:Page,url:str):
        page.goto(url)

    @staticmethod
    @allure.step("Click on element")
    def click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.wait_for(state="attached", timeout=timeout)
        element.click(timeout=timeout)

    @staticmethod
    @allure.step("Force click on element (JS click)")
    def force_click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="attached", timeout=timeout)
        element.evaluate("el => el.click()")

    @staticmethod
    @allure.step("Get text from element")
    def get_text(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        element.wait_for(state="visible", timeout=timeout)

        tag_name = element.evaluate("el => el.tagName.toLowerCase()")

        if tag_name in ["input", "textarea"]:
            text = element.input_value(timeout=timeout)
        else:
            text = element.inner_text(timeout=timeout)

        return text.strip()

    @staticmethod
    @allure.step("Update text in element to: '{text}'")
    def update_text(element: Locator, text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.fill("")  # clear first (more stable)
        element.fill(text, timeout=timeout)

import allure
from playwright.sync_api import Locator, Page

from utils.common_ops import load_config

CONFIG = load_config()
DEFAULT_TIMEOUT = CONFIG["DEFAULT_COMMAND_TIMEOUT"]

class UIActions:

    @staticmethod
    @allure.step("Navigte to")
    def navigate_to(page:Page,url:str):
        page.goto(url)

    @staticmethod
    @allure.step("Click on element")
    def click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.wait_for(state="attached", timeout=timeout)
        element.click(timeout=timeout)

    @staticmethod
    @allure.step("Force click on element (JS click)")
    def force_click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="attached", timeout=timeout)
        element.evaluate("el => el.click()")

    @staticmethod
    @allure.step("Get text from element")
    def get_text(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        element.wait_for(state="visible", timeout=timeout)

        tag_name = element.evaluate("el => el.tagName.toLowerCase()")

        if tag_name in ["input", "textarea"]:
            text = element.input_value(timeout=timeout)
        else:
            text = element.inner_text(timeout=timeout)

        return text.strip()

    @staticmethod
    @allure.step("Update text in element to: '{text}'")
    def update_text(element: Locator, text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.fill("")  # clear first (more stable)
        element.fill(text, timeout=timeout)

    @staticmethod
    @allure.step("Select option by value: '{value}'")
    def select_by_value(element: Locator, value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.select_option(value=value, timeout=timeout)

    @staticmethod
    @allure.step("Extract effective prices from price container elements")
    def get_effective_prices(elements: Locator) -> list[float]:
        """
        Extracts the effective price from a list of price containers.
        Handles sale prices (inside <ins>) and regular prices.
        """
        prices = []
        for container in elements.all():
            sale_price = container.locator("ins .amount")
            if sale_price.count() > 0:
                price_text = sale_price.inner_text()
            else:
                price_text = container.locator(".amount").inner_text()
            
            val = float(price_text.replace('₪', '').replace(',', '').strip())
            prices.append(val)
        return prices

    @staticmethod
    @allure.step("Set input value forcibly via JS: '{value}'")
    def set_value_js(element: Locator, value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """
        Sets the value of an input field directly via JS and dispatches a change event.
        Useful when standard fill() is blocked by the browser.
        """
        element.wait_for(state="attached", timeout=timeout)
        element.evaluate(f"el => {{ el.value = '{value}'; el.dispatchEvent(new Event('change', {{ bubbles: true }})); }}")
