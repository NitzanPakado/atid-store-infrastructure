import pytest
import allure
from utils.common_ops import *
from data.web.atid_store_data import *
from workflows.web.atid_flows import AtidFlows

class TestAtidAbout:
    @allure.title("Test - AI Visual Verification (Kim Kardashian Role)")
    @allure.description("Navigates to the About page and uses Gemini AI to visually verify that Kim Kardashian's role is indeed 'Intern Designer'.")
    def test_atid_kim_kardashian_role_ai(self, atid_flows: AtidFlows):
        # 1. Go to About Page
        atid_flows.go_to_about_page()
        
        # 2. Visually verify the role using AI
        atid_flows.verify_kim_kardashian_role_with_ai(KIM_ROLE)

