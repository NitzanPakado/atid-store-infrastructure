import allure
from workflows.web.atid_flows import AtidFlows
from data.web.atid_store_data import *

class TestAtidE2E:
    @allure.title("Test - Full E2E Flow")
    @allure.description("This is a complete End-to-End flow: starting from Home, navigating to Men category, adding a product, and verifying it in the Cart.")
    def test_atid_full_flow(self, atid_flows: AtidFlows):
        # 1. Start from Home Page
        atid_flows.go_to_home()
        
        # 2. Navigate to Men Page
        atid_flows.click_men_menu()
        
        # 3. Add product to cart
        atid_flows.add_product_to_cart()
        
        # 4. Go to Cart
        atid_flows.go_to_cart_page()
        
        # 5. Verify item in cart
        atid_flows.verify_checkout_button_visible(True)
        
        # 6. Verify quantity matches
        atid_flows.verify_cart_count(EXPECTED_CART_COUNT)
