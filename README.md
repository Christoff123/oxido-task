# Zadanie rekrutacyjne - Junior AI Developer

Aplikacja uruchamiana za pomocą komendy: python app.py

Klucz API znajduje się .env jako: OPENAI_API_KEY. Trzeba samodzielnie skonfigurować plik .env, ze względów bezpieczeństwa niepożądanego udostępnienia klucza.

Aplikacja składa się z funkcji, które wykonywane są w odpowiedniej kolejności, na początku czytany jest plik artykułu, następnie jego zawartość jest wysłana do AI z poleceniem strukturyzacji treści pod HTML. Wygenerowana odpowiedź jest zapisywana do pliku: artykul.html. Następnie tworzymy szablon dla naszego artykułu: szablon.html, do którego dodamy wcześniej wygenerowany artykul i zapiszemy jako plik: podglad.html.