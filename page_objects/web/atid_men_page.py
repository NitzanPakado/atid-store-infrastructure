from playwright.sync_api import Page

class AtidMenPage:
    def __init__(self, page: Page):
        # Basic link to a product
        self.product_link = page.locator(".ast-loop-product__link .woocommerce-loop-product__title").first
        self.search_field = page.locator("input.search-field")
        self.search_submit = page.locator("button.search-submit")
        # This will be used on the single product page
        self.single_add_to_cart_btn = page.locator(".single_add_to_cart_button")
        self.search_results_container = page.locator("#main")
        self.product_names = page.locator(".product .woocommerce-loop-product__title")
        self.products_grid = page.locator(".products .product")
        self.single_product_title = page.locator(".product_title")
        self.no_results_container = page.locator(".no-results.not-found")
        self.category_title = page.locator(".woocommerce-products-header__title")
        self.sorting_dropdown = page.locator("select.orderby")
        self.product_prices = page.locator(".price .amount")
