import time
import allure
from playwright.sync_api import APIRequestContext, APIResponse
from data.api.chuck_api_data import*
from extensions.api_actions import APIActions

class ChuckApiFlows:

    def __init__(self, request_context: APIRequestContext):
        self.api = APIActions(request_context)

    @allure.step("Get a random joke")
    def get_random_joke(self) -> APIResponse:
        return self.api.get(RANDOM_RESOURCE)

    @allure.step(f"Get a random joke by category: {JOKE_CATEGORY_ANIMAL}")
    def get_random_joke_by_category(self, category: str, log_response=True) -> APIResponse:
        params = {"category": category}
        return self.api.get(RANDOM_RESOURCE, params,log_response=log_response)
    
    @allure.step("Get all joke categories")
    def get_categories(self) -> APIResponse:
        return self.api.get(CATEGORIES_RESOURCE)
    
    @allure.step("Search for jokes with query")
    def search_for_joke(self, query: str) -> APIResponse:
        params = {"query": query}
        return self.api.get(SEARCH_RESOURCE, params)
    
    @allure.step("Get count random joke IDs")
    def get_random_joke_ids(self, count):
        ids = set()
        for i in range(count):
            response = self.get_random_joke()
            data = response.json()
            ids.add(data["id"])
        return ids
    
    @allure.step("Search jokes containing word")
    def search_jokes_by_word(self, query):
        # Searches for jokes containing a specific word and returns the list of joke texts.
        response = self.search_for_joke(query)
        data = response.json()
        # מחזיר רשימה של כל הערכים של הבדיחות
        return [joke["value"] for joke in data.get("result", [])]
    
    @allure.step("Get random joke with duration measurement")
    def get_random_joke_with_duration(self):
        # Returns the response and the duration of the API call.
        start_time = time.time()
        response = self.get_random_joke()
        duration = time.time() - start_time
        return response, duration
    
    @allure.step("Get custom search result with parameters")
    def get_custom_search_result(self, params: dict):
        # Sends a GET request with custom parameters and returns JSON response.
        response = self.get_with_custom_params(SEARCH_RESOURCE, params)
        return response.json()
    
    @allure.step("GET request with custom params")
    def get_with_custom_params(self, resource: str, params: dict) -> APIResponse:
        return self.api.get(resource, params)

    @allure.step("Get total jokes count for query")
    def get_total_jokes_by_query(self, query: str):
        response = self.search_for_joke(query)
        data = response.json()
        return data.get("total", 0)
    
     
    @allure.step("Get a random joke from a given - Category")
    def get_joke_data_from_api(self, category: str) -> dict:
        params = {"category": category}
        joke_data =  self.api.get(RANDOM_RESOURCE, params).json()
        print(joke_data)
        return {"value":joke_data["value"],"url":joke_data["url"]}