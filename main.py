from fastapi import FastAPI

from routers import place, moreInfo, osm

description = """Świetne API stworzone przez jeszcze **świetniejszych** ludzi które zabierze cię w pododróż po Śląsku. Chociaż z całą aplikacją będzie łatwiej `<tu powinnien być link ale go nie ma>` 🚀 
## Szybki Opis 
Na ten moment API pozwala na pobranie danych o miejscach z naszej bazy dantch oraz z API open streets maps. 
Mamy też endpoint `/directions/start={start}&stop={stop}` który wyznacza trasę<br/><br/>  
Made by 🎓 Paweł Nalepka, Szymon Przepióra 

"""
tags_metadata = [
    {
        "name": "Place",
        "description": "Pobieranie informacji i miejscach.",
    },
    {
        "name": "More informations",
        "description": "Pobieranie informacji o dodatkowych ułatwieniach i zniżkach.",
    },
    {
        "name": "Open Street Maps",
        "description": "Pobieranie informacji z OPS i nawigowanie.",
    },
]

app = FastAPI(title="Śląska Wyprawa",
              description=description,
              version="1.0",
              contact={
                  "name": "Śląska Wyprawa Team",
                  "email": "nawelpalepka@gmail.com",
                  "url": "https://www-arch.polsl.pl/"}
              , openapi_tags=tags_metadata)

app.include_router(place.router)
app.include_router(moreInfo.router)
app.include_router(osm.router)
