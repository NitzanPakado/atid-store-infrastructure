# --- API Configuration & Resources ---
CHUCK_BASE_URL = "https://api.chucknorris.io/jokes/"
RANDOM_RESOURCE = "random"
SEARCH_RESOURCE = "search"
CATEGORIES_RESOURCE = "categories"
CATEGORIE_SEARCH_RESOURCE="category"

# --- Test Inputs (Values used in requests) ---
SEARCH_VALUE01 = "Barack Obama"
SEARCH_VALUE02 ="Charlie Sheen"
JOKE_CATEGORY_ANIMAL = "animal"
JOKE_CATEGORY_MUSIC = "music"
INVALID_CATEGORY = "non_existent_category"
DUMMY_PARAM_KEY = "dummy"
DUMMY_PARAM_VALUE = "1"
SEARCH_QUERY_CHUCK = "Chuck"

# --- Expected Results (Values for assertions) ---
EXPECTED_STATUS_SUCCESS_CODE = 200
EXPECTED_STATUS_NOT_FOUND_CODE = 404
EXPECTED_JOKE_FIELDS = ["id", "value", "url", "icon_url"]
EXPECTED_RANDOM_CALLS_COUNT = 3
RESPONSE_TIME_THRESHOLD = 1.0
EMPTY_LIST_SIZE = 0
ONE_VALUE = 1

# --- Error Messages ---
MSG_CATEGORY_NOT_FOUND = "Expected category {} not found in {}"
MSG_CATEGORIES_LIST_TYPE = "Categories should be a list"
MSG_CATEGORIES_EMPTY = "Categories list should not be empty"
MSG_JOKES_NOT_FOUND = "Expected some jokes for category {}"
MSG_DUPLICATE_JOKES = "Found duplicate joke IDs in {} random calls"
MSG_WORD_NOT_FOUND = "Word {} not found in joke: {}"
MSG_API_SLOW = "API response too slow: {}s"
MSG_PARAM_ORDER_ISSUE = "Parameters order affected the result count"
MSG_PLAYWRIGHT_RESP_REQUIRED = "Expected a Playwright response object, but got a dictionary"
MSG_STATUS_CODE_MISMATCH = "Expected status code {}, but got {}"
MSG_KEY_NOT_FOUND = "Key '{}' not found in the response JSON"
MSG_VALUE_MISMATCH = "Expected value for key '{}' is '{}', but got '{}'"
MSG_SOFT_ASSERT_FAILURES = "Soft assertion failures:\n{}"