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

def send_to_ai(article, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"{prompt}\n\nTreść artykułu:\n{article}"}
        ],
        stream=False
    )
    return response.choices[0].message.content.strip()

def save_to_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)

def generate_preview(template_content, article_content):
    return template_content.replace(
        "<body>\n    <!-- Miejsce na artykuł -->", f"<body>\n{article_content}"
    )

prompt = """
Przeanalizuj poniższy artykuł i przekształć go w kod HTML. 
1. Użyj odpowiednich tagów HTML do strukturyzacji treści.
2. Określ miejsca, gdzie można wstawić obrazki, oznaczając je za pomocą tagu <img src="image_placeholder.jpg"> 
   i atrybutu alt z dokładnym opisem promptu dla generowania grafiki.
3. Dodaj podpisy pod grafikami za pomocą odpowiednich tagów HTML.
4. Wygeneruj kod wyłącznie do wstawienia między <body> a </body>, nie dodawaj <body>, bez CSS i JavaScript.
"""

def main():
    file_path = "treść_artykułu.txt"
    article_path = "artykul.html"
    template_path = "szablon.html"
    preview_path = "podglad.html"

    # 1. Czytaj treść artykułu
    article = read_file(file_path)

    # 2. Przetwórz artykuł z AI
    print("Przetwarzanie artykułu z OpenAI...")
    html_ai = send_to_ai(article, prompt)
    save_to_file(article_path, html_ai)
    print(f"Artykuł zapisany w {article_path}.")

    # 3. Stwórz szablon
    if not os.path.exists(template_path):
        template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Szablon Artykułu</title>
    <style>
        body {
            width: 70vw;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0 auto;
            background-color: #f9f9f9;
        }
        img {
            display: block;
            margin: 20px auto;
            max-width: 100%;
            height: auto;
        }
        figcaption {
            text-align: center;
            font-style: italic;
            margin-top: -10px;
            margin-bottom: 20px;
            color: #666;
        }
        p {
            color: #333;
        }
        h1, h2, h3 {
            text-align: center;
            color: #0056b3;
        }
        footer {
            text-align: center;
        }
    </style>
</head>
<body>
    <!-- Miejsce na artykuł -->
</body>
</html>"""
        
    save_to_file(template_path, template_content)
    print(f"Szablon zapisany w {template_path}.")

    # 4. Wygeneruj podgląd
    template_content = read_file(template_path)
    preview_html = generate_preview(template_content, html_ai)
    save_to_file(preview_path, preview_html)
    print(f"Podgląd zapisany w {preview_path}.")

if __name__ == "__main__":
    main()
