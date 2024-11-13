from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Klucz API nie został znaleziony. Sprawdź plik .env!")

client = OpenAI(api_key=api_key)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def send_to_ai(content, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"{prompt}\n\nTreść artykułu:\n{content}"}
        ],
        stream=False
    )
    return response.choices[0].message.content.strip()

def save_to_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)

file_path = "treść_artykułu.txt"
article = read_file(file_path)

prompt = """
Przeanalizuj poniższy artykuł i przekształć go w kod HTML. 
1. Użyj odpowiednich tagów HTML do strukturyzacji treści.
2. Określ miejsca, gdzie można wstawić obrazki, oznaczając je za pomocą tagu <img src="image_placeholder.jpg"> 
   i atrybutu alt z dokładnym opisem promptu dla generowania grafiki.
3. Dodaj podpisy pod grafikami za pomocą odpowiednich tagów HTML.
4. Wygeneruj kod wyłącznie do wstawienia między <body> a </body>, nie dodawaj <body>, bez CSS i JavaScript.
"""

html_ai = send_to_ai(article, prompt)
save_to_file("artykul.html", html_ai)
