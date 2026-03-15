import os
import time
import uuid

import pytest
from pytest import FixtureRequest
from playwright.sync_api import Playwright
from data.api.chuck_api_data import *
from data.web.atid_store_data import *
from utils.common_ops import load_config
from utils.fixture_helpers import attach_screenshot, attach_trace, get_browser
from workflows.web.atid_flows import AtidFlows
from utils.fixture_helpers import get_browser
from workflows.api.chuck_api_flows import ChuckApiFlows
from workflows.web.chuck_ui_flows import ChuckUIFlows

# Load the configuration
CONFIG = load_config()     




@pytest.fixture(scope="class")
def page(playwright: Playwright, request:FixtureRequest):
    browser = get_browser(playwright,CONFIG["BROWSER_TYPE"].lower())
    context = browser.new_context(no_viewport=True)     
    context.tracing.start(screenshots=True, snapshots=True, sources=True) # Start tracing for this context.  
    #Listen to console messages
    page = context.new_page()
    page.on("console", handle_console_message)
    yield page    
    test_name = request.node.name
    page.close()
    context.close()
    browser.close()



@pytest.fixture(scope= "class")
def request_context(playwright: Playwright, request:FixtureRequest):
    request_context=playwright.request.new_context(base_url=CHUCK_BASE_URL)
    yield request_context
    request_context.dispose()
from data.api.chuck_api_data import *




@pytest.fixture
def atid_flows(page):
    page.goto(ATID_URL)
    return AtidFlows(page)

@pytest.fixture
def chuck_ui_flows(page):
    return ChuckUIFlows(page)


@pytest.fixture
def chuck_flows(request_context):
    return ChuckApiFlows(request_context)



#Listen to console messages
def handle_console_message(msg):
    if msg.type == "error":
        print(f"Error detected in console: {msg.text}")
    if "the server responded with a status of 404" in msg.text:
        raise AssertionError(f"Test Failed: 404 Error Detected in Console - {msg.text}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to attach screenshots, videos, and traces to Allure reports on test failure,
    and log test case names for reporting.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Attachments (only if the test failed)
        if report.failed:
            page = item.funcargs.get("page")

            if page:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                unique_id = str(uuid.uuid4())[:8]
                base_filename = f"{item.name}_{timestamp}_{unique_id}"

                # Attach screenshot
                screenshot_name = f"{CONFIG['SCREENSHOT_PREFIX']}_{base_filename}.png"
                screenshot_path = os.path.join(CONFIG['ALLURE_RESULTS_DIR'], screenshot_name)
                attach_screenshot(page, item.name, screenshot_path)
                # Attach trace
                trace_name = f"{CONFIG['TRACE_PREFIX']}_{item.name}_{timestamp}.zip"
                trace_path = os.path.join(CONFIG['ALLURE_RESULTS_DIR'], trace_name)
                attach_trace(page, item.name, trace_path)
