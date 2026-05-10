import os
import allure
import pytest
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

class AIVerify:
    @staticmethod
    @allure.step("Visual Verification using Gemini AI")
    def verify_image_content(image_path: str, prompt: str, expected_text: str):
        """
        Sends an image and a prompt to Gemini AI and verifies the response contains the expected text.
        """
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            # Note: pytest.fail would require pytest imported, using assert here
            assert False, "GEMINI_API_KEY environment variable is missing."
            
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        try:
            # Load the screenshot
            img = Image.open(image_path)
            
            # Using flash model for fast multi-modal tasks
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # Send prompt and image
            response = model.generate_content([prompt, img])
            ai_response_text = response.text.strip()
            
            # Log the AI response to Allure
            allure.attach(ai_response_text, name="Gemini Response", attachment_type=allure.attachment_type.TEXT)
            print(f"DEBUG: Gemini AI Response: {ai_response_text}")
            
            # Assert the AI responded with the expected text
            assert expected_text.lower() in ai_response_text.lower(), f"Visual Verification Failed. Expected '{expected_text}' to be confirmed, but AI responded: {ai_response_text}"
            
        except Exception as e:
            assert False, f"Failed during AI verification process: {e}"
