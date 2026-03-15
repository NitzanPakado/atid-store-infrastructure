import pytest
import allure
from utils.common_ops import *
from data.web.atid_store_data import *
from workflows.web.atid_flows import AtidFlows

class TestAtidMen:
    @allure.title("Test - Add Product From Men Page")
    @allure.description("This test verifies that a product can be successfully added to the cart from the Men category page, including verification of being on the product page.")
    def test_atid_add_product(self, atid_flows: AtidFlows):
        atid_flows.go_to_men_page()
        atid_flows.add_product_to_cart()
        atid_flows.go_to_cart_page()
        atid_flows.verify_checkout_button_visible(True)

    @allure.title("Test - Products Count")
    @allure.description("This test verifies that the number of products displayed on the Men category page matches the expected count.")
    def test_atid_product_count(self, atid_flows: AtidFlows):
        atid_flows.go_to_men_page()
        atid_flows.verify_product_count(EXPECTED_MEN_PRODUCTS_COUNT)

    @allure.title("Test - DDT Search")
    @allure.description("This test performs a Data-Driven search to verify that various search terms return the expected results (success or failure).")
    @pytest.mark.parametrize("data", read_data_from_csv(SEARCH_TERMS_PATH))
    def test_atid_ddt_search(self, atid_flows: AtidFlows, data: dict):
        atid_flows.go_to_men_page()
        atid_flows.search_product(data['search_term'])
        atid_flows.verify_product_search_result(data['search_term'], data['expected_result'])

    @allure.title("Test - DB Search")
    @allure.description("This test performs a Data-base search using data directly from an SQLite database.")
    @pytest.mark.parametrize("data", read_data_from_db(DB_PATH, SEARCH_QUERY))
    def test_atid_ddt_db_search(self, atid_flows: AtidFlows, data: dict):
        atid_flows.go_to_men_page()
        atid_flows.search_product(data['search_term'])
        atid_flows.verify_product_search_result(data['search_term'], data['expected_result'])

    @allure.title("Test - No Results Search")
    @allure.description("Verifies that searching for a non-existent product displays the 'no results' message.")
    def test_atid_no_results_search(self, atid_flows: AtidFlows):
        atid_flows.go_to_home()
        atid_flows.search_product(NON_EXISTENT_PRODUCT)
        atid_flows.verify_no_results(NO_RESULTS_MSG)

    @allure.title("Test - Category Navigation")
    @allure.description("Verifies that navigating to the Accessories category displays the correct page and products.")
    def test_atid_category_navigation(self, atid_flows: AtidFlows):
        atid_flows.go_to_home()
        atid_flows.click_accessories_menu()
        atid_flows.verify_category_page(ACCESSORIES_TITLE, ACCESSORIES_SLUG)

    @allure.title("Test - Special Characters Search")
    @allure.description("Verifies that searching with special characters handles input safely and shows 'no products found'.")
    def test_atid_special_chars_search(self, atid_flows: AtidFlows):
        atid_flows.go_to_home()
        atid_flows.search_product(SPECIAL_CHARS_TERM)
        atid_flows.verify_no_results(NO_RESULTS_MSG)

    @allure.title("Test - Sort by Price Low to High")
    @allure.description("Verifies that products can be sorted by price in ascending order.")
    def test_atid_sort_by_price(self, atid_flows: AtidFlows):
        atid_flows.go_to_home()
        atid_flows.go_to_men_page()
        atid_flows.select_sorting_option(SORT_BY_PRICE)
        atid_flows.verify_prices_sorted_low_to_high()
