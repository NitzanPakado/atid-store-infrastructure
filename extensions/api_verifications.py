from typing import List

from data.api.chuck_api_data import*

class APIVerify:
    @staticmethod
    def status_code(response, expected_status_code: int):
        """
        Verifies that the API response status code matches the expected status code.
        """
        if isinstance(response, dict):  # If it's already JSON, we can't check status
            raise ValueError(MSG_PLAYWRIGHT_RESP_REQUIRED)
        assert response.status == expected_status_code, \
            MSG_STATUS_CODE_MISMATCH.format(expected_status_code, response.status)
        

    @staticmethod
    def json_key_exists(response_data, key: str):
        """
        Verifies that a specific key exists in the JSON response.
        """
        assert key in response_data, MSG_KEY_NOT_FOUND.format(key)

    
    @staticmethod
    def json_value_equals(response_data, key: str, expected_value):
        """
        Verifies that a specific key in the JSON response has the expected value.
        """
        assert response_data[key] == expected_value, (
            MSG_VALUE_MISMATCH.format(key, expected_value, response_data[key])
        )

    
    @staticmethod
    def json_contains(response_data, expected_data: dict):
        """
        Verifies that the JSON response contains the expected data.
        """
        for key, value in expected_data.items():
            assert key in response_data, MSG_KEY_NOT_FOUND.format(key)
            assert response_data[key] == value, (
                MSG_VALUE_MISMATCH.format(key, value, response_data[key])
            )

    # Soft Assertions
    @staticmethod
    def soft_assert_status_code(response, expected_status_code: int):
        """
        Soft asserts that the API response status code matches the expected status code.
        """
        if isinstance(response, dict):  
            APIVerify.errors.append(MSG_PLAYWRIGHT_RESP_REQUIRED)

        elif response.status != expected_status_code:
            APIVerify.errors.append(
                MSG_STATUS_CODE_MISMATCH.format(expected_status_code, response.status)
            )

    @staticmethod
    def assert_all():
        """
        Raises all collected assertion errors at once.
        """
        if APIVerify.errors:
            error_message = "\n".join(APIVerify.errors)
            APIVerify.errors.clear()  # Clear errors after raising
            raise AssertionError(MSG_SOFT_ASSERT_FAILURES.format(error_message))
        
    @staticmethod
    def verify_schema(data:dict,fields:List[str]):
            for field in fields:
                APIVerify.json_key_exists(data, field)


    @staticmethod
    def list_contains(response_data, key: str, expected_value):
        """
        Verifies that a list inside JSON contains a specific value.
        """
        assert key in response_data, MSG_KEY_NOT_FOUND.format(key)

        assert expected_value in response_data[key], (
            MSG_CATEGORY_NOT_FOUND.format(expected_value, response_data[key]))        
        

    @staticmethod
    def is_list(data):
        """
        Verifies that the response data is a list.
        """
        assert isinstance(data, list), MSG_CATEGORIES_LIST_TYPE

    @staticmethod
    def list_not_empty(data):
        """
        Verifies that the list is not empty.
        """
        assert len(data) > EMPTY_LIST_SIZE, MSG_CATEGORIES_EMPTY      

    @staticmethod
    def value_greater_than(value, min_value, message=None):
        """
        Verifies that a numeric value is greater than a given minimum value.
        """
        assert value > min_value, message        

    @staticmethod
    def collection_size_equals(collection, expected_size, message):
        """
        Verifies that the collection size equals the expected size.
        """
        assert len(collection) == expected_size, message    

    @staticmethod
    def all_strings_contain_keyword(strings: list, keyword: str, message: str):
        """
        Verifies that every string in the list contains the keyword (case-insensitive).
        """
        for s in strings:
            assert keyword.lower() in s.lower(), message.format(keyword, s)    

    @staticmethod
    def response_time_within_limit(duration, max_duration, message):
        """
        Verifies that the response time is less than the maximum allowed duration.
        """
        assert duration < max_duration, message.format(f"{duration:.2f}")        