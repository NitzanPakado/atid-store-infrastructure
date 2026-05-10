import allure
from playwright.sync_api import Page
from extensions.ui_actions import UIActions
from extensions.web_verifications import WebVerify
from page_objects.web.atid_home_page import AtidHomePage
from page_objects.web.atid_men_page import AtidMenPage
from page_objects.web.atid_cart_page import AtidCartPage
from page_objects.web.atid_about_page import AtidAboutPage
from extensions.ai_verifications import AIVerify
from data.web.atid_store_data import *

class AtidFlows:
    def __init__(self, page: Page):
        self.page = page
        self.home = AtidHomePage(page)
        self.men = AtidMenPage(page)
        self.cart = AtidCartPage(page)
        self.about = AtidAboutPage(page)

    @allure.step("Navigate to Home:")
    def go_to_home(self):
        UIActions.navigate_to(self.page, ATID_URL)

    @allure.step("Navigate to Men Page:")
    def go_to_men_page(self):
        UIActions.navigate_to(self.page, MEN_CATEGORY_URL)

    @allure.step("Navigate to Accessories Page:")
    def go_to_accessories_page(self):
        UIActions.navigate_to(self.page, ACCESSORIES_CATEGORY_URL)

    @allure.step("Navigate to About Page:")
    def go_to_about_page(self):
        UIActions.navigate_to(self.page, ABOUT_URL)

    @allure.step("Navigate to Cart Page:")
    def go_to_cart_page(self):
        UIActions.navigate_to(self.page, CART_URL)

    @allure.step("Click Men in Menu:")
    def click_men_menu(self):
        UIActions.click(self.home.men_menu_item)

    @allure.step("Click Accessories in Menu:")
    def click_accessories_menu(self):
        UIActions.click(self.home.accessories_menu_item)

    @allure.step("Add product to cart:")
    def add_product_to_cart(self):
        # 1. Click on the first product to go to single product page
        UIActions.click(self.men.product_link)
        # 2. Verify we are on the product page
        self.verify_single_product_page()
        # 3. Click Add to cart on the product page
        UIActions.click(self.men.single_add_to_cart_btn)

    @allure.step("Update quantity in cart:")
    def update_cart_quantity(self, quantity: int):
        self.cart.quantity_input.focus()
        current_text = UIActions.get_text(self.cart.quantity_input)
        current = int(current_text) if current_text else 1
        for _ in range(quantity - current):
            self.page.keyboard.press(ARROW_UP_KEY)
        UIActions.click(self.cart.update_cart_button)

    @allure.step("Verify on single product page:")
    def verify_single_product_page(self):
        WebVerify.visible(self.men.single_product_title)

    @allure.step("Verify checkout button visibility: {visible}")
    def verify_checkout_button_visible(self, visible: bool):
        if visible:
            WebVerify.visible(self.cart.checkout_button)
        else:
            WebVerify.not_visible(self.cart.checkout_button)

    @allure.step("Verify quantity value: {expected_value}")
    def verify_quantity_value(self, expected_value: int):
        WebVerify.value_numeric(self.cart.quantity_input, expected_value)

    @allure.step("Verify quantity input visibility:")
    def verify_quantity_input_visible(self):
        WebVerify.visible(self.cart.quantity_input)

    @allure.step("Verify update button enabled state: {enabled}")
    def verify_update_button_enabled(self, enabled: bool):
        if enabled:
            WebVerify.enabled(self.cart.update_cart_button)
        else:
            WebVerify.disabled(self.cart.update_cart_button)

    @allure.step("Verify product count on page: {expected_count}")
    def verify_product_count(self, expected_count: int):
        actual_count = self.men.products_grid.count()
        WebVerify.strings_are_equal(str(actual_count), str(expected_count), f"Expected {expected_count} products but found {actual_count}")

    @allure.step("Get products count on page:")
    def get_product_count(self):
        return self.men.products_grid.count()

    @allure.step("Set quantity in cart directly:")
    def set_quantity(self, quantity: str):
        # Set value via JS and dispatch change event to notify the page using UI Actions
        UIActions.set_value_js(self.cart.quantity_input, quantity)
        # Use force_click in case the button is disabled by browser validation
        UIActions.force_click(self.cart.update_cart_button)

    @allure.step("Remove product from cart:")
    def remove_item(self):
        UIActions.click(self.cart.remove_item_button)

    @allure.step("Apply coupon:")
    def apply_coupon(self, code: str):
        UIActions.update_text(self.cart.coupon_field, code)
        UIActions.click(self.cart.apply_coupon_btn)

    @allure.step("Apply empty coupon:")
    def apply_empty_coupon(self):
        UIActions.update_text(self.cart.coupon_field, "")
        UIActions.click(self.cart.apply_coupon_btn)

    @allure.step("Search product:")
    def search_product(self, term: str):
        # Click search icon if the field is hidden (common in Astra theme)
        if not self.men.search_field.is_visible():
            UIActions.click(self.home.search_icon)
        UIActions.update_text(self.men.search_field, term)
        self.page.keyboard.press(ENTER_KEY)

    @allure.step("Verify search result for: {term}")
    def verify_product_search_result(self, term: str, expected_result: str):
        # Look for the product name within the main content area using the POM
        product_locator = self.men.get_search_result_by_name(term)
        if expected_result == SEARCH_TERM_SUCCESS:
            WebVerify.visible(product_locator)
        else:
            WebVerify.not_visible(product_locator)

    @allure.step("Verify cart is empty:")
    def verify_empty_cart(self):
        WebVerify.visible(self.cart.empty_cart_msg)

    @allure.step("Verify product is in cart:")
    def verify_product_in_cart(self, visible: bool):
        if visible:
            WebVerify.visible(self.cart.product_name_link)
        else:
            WebVerify.not_visible(self.cart.product_name_link)

    @allure.step("Verify quantity input value: {expected}")
    def verify_quantity_input_value(self, expected: str):
        WebVerify.input_value_bug_check(self.cart.quantity_input, expected)

    @allure.step("Verify cart count: {expected_count}")
    def verify_cart_count(self, expected_count: str):
        WebVerify.contain_text(self.cart.cart_count_header, expected_count)

    @allure.step("Verify error message:")
    def verify_error(self, expected_text: str):
        WebVerify.contain_text(self.cart.error_msg_box, expected_text)

    @allure.step("Verify success message:")
    def verify_success_message(self, expected_text: str):
        WebVerify.contain_text(self.cart.message_box, expected_text)

    @allure.step("Click Return to Shop:")
    def click_return_to_shop(self):
        UIActions.click(self.cart.return_to_shop_button)

    @allure.step("Verify store page:")
    def verify_store_page(self):
        WebVerify.url_contains(self.page, STORE_SLUG)

    @allure.step("Verify no results found:")
    def verify_no_results(self, expected_msg: str):
        WebVerify.visible(self.men.no_results_container)
        WebVerify.contain_text(self.men.no_results_container, expected_msg)

    @allure.step("Verify category page: {expected_title}")
    def verify_category_page(self, expected_title: str, expected_url_part: str):
        WebVerify.contain_text(self.men.category_title, expected_title)
        WebVerify.url_contains(self.page, expected_url_part)

    @allure.step("Select sorting option: {option_value}")
    def select_sorting_option(self, option_value: str):
        UIActions.select_by_value(self.men.sorting_dropdown, option_value)
        WebVerify.url_contains(self.page, PRICE_ORDER_SLUG)

    @allure.step("Verify prices are sorted Low to High")
    def verify_prices_sorted_low_to_high(self):
        # 1. Get price container locators from the Page Object Model
        price_containers = self.men.product_price_containers
        
        # 2. Extract the actual floating point prices using UI Actions
        prices = UIActions.get_effective_prices(price_containers)
        
        # 3. Verify the array is sorted Low to High using Web Verifications
        WebVerify.is_sorted_ascending(prices, f"Prices are not sorted Low to High: {prices}")

    @allure.step("Verify Kim Kardashian role using AI: {expected_role}")
    def verify_kim_kardashian_role_with_ai(self, expected_role: str):
        # 1. Get the container element for the member
        member_container = self.about.kim_kardashian_card
        
        # 2. Scroll to it so it's fully visible
        member_container.scroll_into_view_if_needed()
        
        # 3. Take a screenshot of the specific element
        screenshot_path = "screenshot_kim_kardashian.png"
        member_container.screenshot(path=screenshot_path)
        
        # 4. Call the AI verifier with the screenshot, prompt, and expected text
        AIVerify.verify_image_content(screenshot_path, AI_ROLE_PROMPT, expected_role)

