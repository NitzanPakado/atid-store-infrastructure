import allure
import pytest
from data.api.chuck_api_data import*
from extensions.api_verifications import APIVerify
from extensions.web_verifications import WebVerify
from workflows.api.chuck_api_flows import ChuckApiFlows
from workflows.web.chuck_ui_flows import ChuckUIFlows

class TestChuckAPIExtended:
    
    @allure.title("Random Joke Test")
    @allure.description("Test for a random joke from the API and verify schema and status code")
    def test01_verify_random_joke(self, chuck_flows: ChuckApiFlows):
        # Test for a random joke from the site
        response = chuck_flows.get_random_joke()
        APIVerify.status_code(response, EXPECTED_STATUS_SUCCESS_CODE)
        data = response.json()
        APIVerify.verify_schema(data,EXPECTED_JOKE_FIELDS)


    @allure.title("Random Joke by Category Test")
    @allure.description("Test for a random joke filtered by a specific category")
    def test02_verify_random_joke_by_category(self, chuck_flows: ChuckApiFlows):
        # Test for a random joke by category
        category = JOKE_CATEGORY_ANIMAL
        response = chuck_flows.get_random_joke_by_category(category)
        APIVerify.status_code(response, EXPECTED_STATUS_SUCCESS_CODE)
        data = response.json()
        APIVerify.list_contains(data, "categories", category)


    @allure.title("Get All Categories Test")
    @allure.description("Test retrieving all joke categories and verify the response is a non-empty list")
    def test03_verify_get_all_categories(self, chuck_flows: ChuckApiFlows):
        # Test the retrieval of all existing categories
        response = chuck_flows.get_categories()
        APIVerify.status_code(response, EXPECTED_STATUS_SUCCESS_CODE)
        categories = response.json()
        APIVerify.is_list(categories)
        APIVerify.list_not_empty(categories) 


    @allure.title("Joke Count in Category Test")
    @allure.description("Test counting jokes in a specific category using search API")
    def test04_verify_joke_count_in_category(self, chuck_flows: ChuckApiFlows):
        # Test for the number of jokes in a specific category (via search)
        category = JOKE_CATEGORY_MUSIC
        response = chuck_flows.search_for_joke(category)
        APIVerify.status_code(response, EXPECTED_STATUS_SUCCESS_CODE)
        data = response.json()
        total = data.get("total", EMPTY_LIST_SIZE)
        print(f"\nTotal jokes for category '{category}': {total}")
        APIVerify.value_greater_than(
            total,
            EMPTY_LIST_SIZE,
            MSG_JOKES_NOT_FOUND.format(category))


    @allure.title("No Duplicate Jokes Test")
    @allure.description("Ensure that multiple random joke calls return unique joke IDs")
    def test05_verify_no_duplicate_jokes(self, chuck_flows: ChuckApiFlows):
        # Verify that there are no duplicate jokes by ID
        ids = chuck_flows.get_random_joke_ids(EXPECTED_RANDOM_CALLS_COUNT)
        APIVerify.collection_size_equals(
            ids,
            EXPECTED_RANDOM_CALLS_COUNT,
            MSG_DUPLICATE_JOKES.format(EXPECTED_RANDOM_CALLS_COUNT))


    @allure.title("Double Parameter Test")
    @allure.description("Test API handling when duplicate query parameters are provided")
    def test06_verify_double_parameter(self, chuck_flows: ChuckApiFlows):
        # Test for the use of duplicate parameters
        params = {"query": [SEARCH_VALUE01, SEARCH_QUERY_CHUCK]}
        response = chuck_flows.get_with_custom_params(SEARCH_RESOURCE, params)
        # Usually the API will take the last one or combine them, let's ensure it doesn't crash
        APIVerify.status_code(response, EXPECTED_STATUS_SUCCESS_CODE)


    @allure.title("Search Word in Joke Test")
    @allure.description("Test searching for jokes containing a specific keyword")
    def test07_verify_search_word_in_joke(self, chuck_flows: ChuckApiFlows):
        # Test searching for a specific word within the joke
        query = SEARCH_VALUE01
        jokes = chuck_flows.search_jokes_by_word(query)
        APIVerify.all_strings_contain_keyword(
                                                jokes,
                                                query,
                                                MSG_WORD_NOT_FOUND)


    @allure.title("Invalid Category Test")
    @allure.description("Test API response when requesting a joke from an invalid category")
    def test08_verify_invalid_category(self, chuck_flows: ChuckApiFlows):
        # Test with invalid input (non-existent category)
        response = chuck_flows.get_random_joke_by_category(INVALID_CATEGORY,False)
        APIVerify.status_code(response, EXPECTED_STATUS_NOT_FOUND_CODE)
    

    @allure.title("Performance Check Test")
    @allure.description("Verify the API response time is within the acceptable limit")
    def test09_verify_performance_check(self, chuck_flows: ChuckApiFlows):
        # Performance test to ensure API response time is within acceptable limits
        response, duration = chuck_flows.get_random_joke_with_duration()
        APIVerify.status_code(response, EXPECTED_STATUS_SUCCESS_CODE)
        print(f"API Response time: {duration:.2f}s")
        APIVerify.response_time_within_limit(duration, RESPONSE_TIME_THRESHOLD, MSG_API_SLOW)        


    @allure.title("Parameters Order Test")
    @allure.description("Verify that changing the order of parameters does not affect the API result")
    def test10_verify_parameters_order(self, chuck_flows: ChuckApiFlows):
        # Verify that the order of fields or parameters does not affect the result
        params1 = {"query": SEARCH_VALUE01, DUMMY_PARAM_KEY: DUMMY_PARAM_VALUE}
        params2 = {DUMMY_PARAM_KEY: DUMMY_PARAM_VALUE, "query": SEARCH_VALUE01}

        res1 = chuck_flows.get_custom_search_result(params1)
        res2 = chuck_flows.get_custom_search_result(params2)

        APIVerify.json_value_equals(res2, "total", res1["total"])


    @allure.title("Compare jokes count between Barack Obama and Charlie Sheen")
    @allure.description("Verify that Charlie Sheen has more jokes than Barack Obama in the Chuck Norris API search results")
    def test11_verify_who_has_more_jokes(self, chuck_flows: ChuckApiFlows):
        barack_total_jokes = chuck_flows.get_total_jokes_by_query(SEARCH_VALUE01)
        print(f"\nBarack's Total Jokes: {barack_total_jokes}")
        charlie_total_jokes = chuck_flows.get_total_jokes_by_query(SEARCH_VALUE02)
        print(f"Charlie's Total Jokes: {charlie_total_jokes}")
        APIVerify.value_greater_than(charlie_total_jokes, barack_total_jokes)

    @allure.title("Verify joke from UI and API")
    @allure.description("Test verifies that the joke received from the API is the same joke displayed in the UI")
    def test12_verify_joke_from_ui_and_api(self,chuck_flows: ChuckApiFlows,chuck_ui_flows:ChuckUIFlows):
        joke_data=chuck_flows.get_joke_data_from_api(JOKE_CATEGORY_MUSIC)
        chuck_ui_flows.navigate_to_joke(joke_data["url"])
        WebVerify.strings_are_equal(joke_data["value"],chuck_ui_flows.get_joke_value())
        






