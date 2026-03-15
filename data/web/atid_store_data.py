# URLs
ATID_URL = "https://atid.store/"
MEN_CATEGORY_URL = "https://atid.store/product-category/men/"
ACCESSORIES_CATEGORY_URL = "https://atid.store/product-category/accessories/"
CART_URL = "https://atid.store/cart/"
STORE_URL = "https://atid.store/store/"

# File Paths & Data Sources
SEARCH_TERMS_PATH = "data/ddt/search_data.csv"
DB_PATH = "data/data_base/atid_db.db"
SEARCH_QUERY = "SELECT search_term, expected_result FROM search_data"

# Expected Messages
INVALID_COUPON_MSG = 'Coupon "invalid_code" does not exist!'
EMPTY_COUPON_MSG = "Please enter a coupon code."
EMPTY_CART_MSG = "Your cart is currently empty."
NO_RESULTS_MSG = "Sorry, but nothing matched your search terms."
NO_PRODUCTS_FOUND_MSG = "No products were found matching your selection."
CART_UPDATED_MSG = "Cart updated."
MIN_QTY_ERROR_MSG = "Value must be greater than or equal to 1"
MAX_QTY_ERROR_MSG = "Value must be less than or equal to"
ACCESSORIES_TITLE = "Accessories"

# Test Data
INVALID_COUPON_CODE = "invalid_code"
DEFAULT_QUANTITY = 3
EXPECTED_CART_COUNT = "1"
OUT_OF_STOCK_TEXT = "OUT OF STOCK"
ADD_TO_CART_TEXT = "Add to cart"
SEARCH_TERM_SUCCESS = "found"
NON_EXISTENT_PRODUCT = "NonExistent123"
SPECIAL_CHARS_TERM = "!@#$"
SEARCH_FIELD_PLACEHOLDER = "Search products…"
ACCESSORIES_SLUG = "/accessories/"
STORE_SLUG = "/store/"
PRICE_ORDER_SLUG = "orderby=price"

# Boundary Data
SORT_BY_PRICE = "price"
QTY_ZERO = "0"
QTY_NEGATIVE = "-1"
QTY_LARGE = "9999"
QTY_NON_NUMERIC = "abc"
EXPECTED_MEN_PRODUCTS_COUNT = 12
RESET_QTY_VALUE = "1"

# Keyboard/System
ENTER_KEY = "Enter"
ARROW_UP_KEY = "ArrowUp"
