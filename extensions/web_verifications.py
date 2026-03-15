from smart_assertions import soft_assert, verify_expectations
import allure
import re
from playwright.sync_api import Locator, expect, Page

class WebVerify:
  
    @staticmethod    
    @allure.step("Verify that the element has text")
    def text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element matches the expected text.
        """
        expect(element).to_have_text(expected_text)

    @staticmethod
    @allure.step("Verify String")
    def strings_are_equal(actual:str,expected:str,message=None):
        assert actual == expected,message


    @staticmethod
    @allure.step("Verify that the element is visible")
    def visible(element: Locator):
        """
        Verifies that the element is visible.
        """
        expect(element).to_be_visible()
    
    @staticmethod
    @allure.step("Verify that the element is not visible")
    def not_visible(element: Locator):
        """
        Verifies that the element is not visible.
        """
        expect(element).not_to_be_visible()
    
    @staticmethod
    @allure.step("Verifies that the number of elements matching the locator is equal to the expected count")
    def count(element: Locator, count: int):
        """
        Verifies that the number of elements matching the locator is equal to the expected count.
        """
        expect(element).to_have_count(count)

    @staticmethod
    @allure.step("Verify that the element contains the expected text")
    def contain_text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element contains the expected text.
        """
        expect(element).to_contain_text(expected_text)
    
    @staticmethod
    @allure.step("Verify that the element has the expected value")
    def value(element: Locator, expected_value: str):
        """
        Verifies that the value of the element matches the expected value.
        """
        expect(element).to_have_value(expected_value)

    @staticmethod
    @allure.step("Verify that the input has text and report bug if not")
    def input_value_bug_check(element: Locator, expected: str):
        """
        Verifies that the value of the element matches the expected value.
        If not, reports a bug specifically for invalid input acceptance.
        """
        actual = element.input_value()
        assert actual == expected, f"Expected quantity {expected} but found {actual} (Bug: Invalid input was accepted)"
    
    @staticmethod
    @allure.step("Verify that the element has the expected value")
    def value_numeric(element: Locator, expected_value: int):
        """
        Verifies that the value of the element matches the expected value.
        """
        expect(element).to_have_value(str(expected_value))

    @staticmethod
    @allure.step("Verify that the URL contains the expected text")
    def url_contains(page: Page, expected_text: str):
        """
        Verifies that the current URL contains the expected text.
        """
        expect(page).to_have_url(re.compile(f".*{expected_text}.*"))
    


    @staticmethod
    @allure.step("Verify that the element is disabled")
    def disabled(element: Locator):
        """
        Verifies that the element is disabled.
        """
        expect(element).to_be_disabled()

    @staticmethod
    @allure.step("Verify that the element is enabled")
    def enabled(element: Locator):
        """
        Verifies that the element is enabled.
        """
        expect(element).to_be_enabled()


    # Soft Assertions    
    @staticmethod
    @allure.step("Soft assertion to check if the element has the expected text")
    def soft_text(element: Locator, expected_text: str, message: str):
        """
        Soft assertion to check if the element has the expected text.
        Test execution will continue even if this assertion fails.
        """
        actual_text = element.inner_text()
        soft_assert(actual_text == expected_text, message)

    @staticmethod
    @allure.step("Soft assertion to check if the element is visible")
    def soft_is_visible(element: Locator, message: str):
        """
        Soft assertion to check if the element is visible.
        Test execution will continue even if this assertion fails.
        """
        soft_assert(element.is_visible(), message)

    @staticmethod
    @allure.step("Raises all collected assertion errors at once")
    def soft_all():
        """Raises all collected assertion errors at once."""
        verify_expectations()