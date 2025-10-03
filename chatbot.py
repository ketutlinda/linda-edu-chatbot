#import google.generativeai as genai
from google import genai


MODEL_ID= 'gemini-2.5-flash'

def get_response(api_key: str, prompt: str) -> str:
    """Kirim prompt ke Gemini dan ambil balasan"""
    client = genai.Client(api_key=api_key)
    MODEL_ID= 'gemini-2.5-flash'
    try:
        response= client.models.generate_content(
        model=MODEL_ID,
        contents=[
        prompt,
        ]
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"