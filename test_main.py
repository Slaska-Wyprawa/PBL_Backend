from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_two_places_info():
    response = client.get("/place/?offset=0&limit=2")
    assert response.status_code == 200
    assert response.json() == {
        [
            {
                "ObjectId": 1,
                "Name": "Sztolnia Królowa Luiza - Zabrze",
                "Description": "Sztolnia Królowa Luiza to połączenie dwóch górniczych, historycznych obiektów: Głównej Kluczowej Sztolni Dziedzicznej (najdłuższy obiekty hydrotechniczny w europejskim górnictwie węglowym) oraz Kopalni Królowa Luiza Do atrakcji należą: podziemny park maszyn górniczych, zlokalizowany w dawnych wyrobiskach kopalni, trasa wodna oraz rozbudowana przestrzeń naziemna z tematycznymi parkami rozrywkowo-edukacyjnymi. Sztolnia Królowa Luiza jest częścią Muzeum Górnictwa Węglowego w Zabrzu.\r\nSztolnia jest wybitnym dziełem inżynierskim, które dokumentuje poziom rozwoju techniki w I poł. XIX w. w zakresie budownictwa podziemnego. Dzięki odpowiedniemu udostępnieniu można obecnie spływać łodziami na odcinku ok. 1100 m. W podziemnym porcie załadunkowym w pokładzie węgla 509 turyści mogą zobaczyć, w jaki sposób w przeszłości wykorzystywano Sztolnię do transportu węgla drogą wodną.\r\n",
                "ImagePath": "http://podziemia.pl/wp-content/uploads/2017/07/IMG_5102-scaled.jpg",
                "Longitude": 50.2964,
                "Latitude": 18.7955
            },
            {
                "ObjectId": 2,
                "Name": "Nieczynny kamieniołom wapieni triasowych Mikołów Mokre",
                "Description": "Nazwa Fiołkowej Góry pochodzi od kwitnących wiosną fiołków leśnych. Wzgórze zbudowane jest z wapieni warstw gogolińskich. Wapienie te stanowiły surowiec do wypalania wapna, o czym świadczy duża ilość (8, 13?) zachowanych na obrzeżach kamieniołomu wapienników. Wapienniki to kamienno-ceglane budowle, służące w XVIII i XIX w. do wypalania wapna, choć jeszcze do początku lat 80. XX wieku trwała eksploatacja.\r\nKamieniołom ma kształt amfiteatralny. Ściany sięgają 20m wysokości i są dość dobrze zachowane. \r\nWyrobiska są opuszczone i zarośnięte, można jednak znaleźć tu skamieniałości charakterystyczne dla utworów węglanowych gónego triasu (liliowce, skorupy małży, ramienionogów, zęby ryb, lub niewielkie kości gadów). Występują tu utwory triasu środkowego – wapienia muszlowego dolnego. Na dolny wapień muszlowy składają się warstwy gogolińskie i dolomity kruszconośne. Odsłaniające się w kamieniołomie warstwy gogolińskie, złożone są z żółtoszarych wapieni, wapieni marglistych i margli o łącznej miąższości (w pełnym profilu) 40 – 45 m. Warstwy gogolińskie nie mają większego znaczenia jako surowiec dla przemysłu cementowo – wapienniczego, głównie ze względu na zmienną i niezbyt wysoką jakość.\r\nNa terenie kamieniołomu znajduje się stara sztolnia z przełomu lat 20. i 30. XX w, w której bytują nietoperze.\r\n",
                "ImagePath": "http://img3.garnek.pl/a.garnek.pl/031/259/31259833_800.0.jpg/mikolow-mokre-nieczynne.jpg",
                "Longitude": 50.1822,
                "Latitude": 18.8458
            }
        ]
    }


def test_get_place_info():
    response = client.get("/place/1")
    assert response.status_code == 200
    assert response.json() == {
        "ObjectId": 1,
        "FreeParking": true,
        "OPMapLink": null,
        "Name": "Sztolnia Królowa Luiza - Zabrze",
        "Description": "Sztolnia Królowa Luiza to połączenie dwóch górniczych, historycznych obiektów: Głównej Kluczowej Sztolni Dziedzicznej (najdłuższy obiekty hydrotechniczny w europejskim górnictwie węglowym) oraz Kopalni Królowa Luiza Do atrakcji należą: podziemny park maszyn górniczych, zlokalizowany w dawnych wyrobiskach kopalni, trasa wodna oraz rozbudowana przestrzeń naziemna z tematycznymi parkami rozrywkowo-edukacyjnymi. Sztolnia Królowa Luiza jest częścią Muzeum Górnictwa Węglowego w Zabrzu.\r\nSztolnia jest wybitnym dziełem inżynierskim, które dokumentuje poziom rozwoju techniki w I poł. XIX w. w zakresie budownictwa podziemnego. Dzięki odpowiedniemu udostępnieniu można obecnie spływać łodziami na odcinku ok. 1100 m. W podziemnym porcie załadunkowym w pokładzie węgla 509 turyści mogą zobaczyć, w jaki sposób w przeszłości wykorzystywano Sztolnię do transportu węgla drogą wodną.\r\n",
        "ImagePath": "http://podziemia.pl/wp-content/uploads/2017/07/IMG_5102-scaled.jpg",
        "Longitude": 50.2964,
        "Latitude": 18.7955,
        "EasyAcces": true,
        "FreeEntry": false,
        "GMapLink": "https://goo.gl/maps/LYvX4TUyLqFDYHjL8"
    }


def test_get_wrong_place_id():
    response = client.get("/place/64646")
    assert response.status_code == 404


def test_get_discount():
    response = client.get("/discount/2")
    assert response.status_code == 200
    assert response.json() == {
        "ObjectId": 2,
        "DiscountList": [
            "Karta Dużej Rodziny",
            "Do lat 11",
            "Uczniowska",
            "Emerycka"
        ]
    }
