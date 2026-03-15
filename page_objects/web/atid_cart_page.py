from playwright.sync_api import Page

class AtidCartPage:
    def __init__(self, page: Page):
        # Robust selectors favoring stable classes and names over dynamic IDs
        self.quantity_input = page.locator("input.qty").first
        self.update_cart_button = page.locator("button[name='update_cart']")
        self.remove_item_button = page.locator("a.remove")
        self.empty_cart_msg = page.locator(".cart-empty.woocommerce-info")
        self.coupon_field = page.locator("#coupon_code")
        self.apply_coupon_btn = page.locator("button[name='apply_coupon']")
        self.error_msg_box = page.locator(".woocommerce-error")
        self.cart_count_header = page.locator(".cart-container .count")
        self.cart_item = page.locator("tr.cart_item")
        self.product_name_link = self.cart_item.locator("td.product-name a")
        self.checkout_button = page.locator(".checkout-button")
        self.return_to_shop_button = page.locator("a.button.wc-backward")
        self.message_box = page.locator(".woocommerce-message")