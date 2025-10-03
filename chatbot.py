import google.generativeai as genai

def setup_model(api_key: str):
    """Konfigurasi Gemini model"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        "gemini-1.5-flash-latest",
        system_instruction=(
            "Kamu adalah asisten pendidikan yang menjawab dengan santai, "
            "mudah dipahami, dan penuh contoh. Jangan terlalu formal, "
            "anggap seperti ngobrol dengan teman, tapi tetap informatif."
        )
    )

def get_response(model, prompt: str) -> str:
    """Kirim prompt ke Gemini dan ambil balasan"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

