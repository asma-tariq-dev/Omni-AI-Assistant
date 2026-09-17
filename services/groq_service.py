from groq import Groq
from utils.config import GROQ_API_KEY, MODEL
from utils.prompts import get_prompt

client = Groq(api_key=GROQ_API_KEY)

def ask_groq(question, mode):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system","content":get_prompt(mode)},
            {"role":"user","content":question}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
