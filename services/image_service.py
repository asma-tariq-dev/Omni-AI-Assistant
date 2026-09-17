from urllib.parse import quote

def generate_image(prompt):
    return "https://image.pollinations.ai/prompt/" + quote(prompt)
