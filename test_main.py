# pylint: skip-file
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_two_places_info():
    response = client.get("/place/?offset=0&limit=2")
    assert response.status_code == 200
    assert response.json() == [
        {
            "ObjectId": 1,
            "Name": "Sztolnia Królowa Luiza - Zabrze",
            "Description": "Sztolnia Królowa Luiza to połączenie dwóch górniczych, historycznych obiektów: Głównej "
                           "Kluczowej Sztolni Dziedzicznej (najdłuższy obiekty hydrotechniczny w europejskim "
                           "górnictwie węglowym) oraz Kopalni Królowa Luiza Do atrakcji należą: podziemny park maszyn "
                           "górniczych, zlokalizowany w dawnych wyrobiskach kopalni, trasa wodna oraz rozbudowana "
                           "przestrzeń naziemna z tematycznymi parkami rozrywkowo-edukacyjnymi. Sztolnia Królowa "
                           "Luiza jest częścią Muzeum Górnictwa Węglowego w Zabrzu.\r\nSztolnia jest wybitnym dziełem "
                           "inżynierskim, które dokumentuje poziom rozwoju techniki w I poł. XIX w. w zakresie "
                           "budownictwa podziemnego. Dzięki odpowiedniemu udostępnieniu można obecnie spływać "
                           "łodziami na odcinku ok. 1100 m. W podziemnym porcie załadunkowym w pokładzie węgla 509 "
                           "turyści mogą zobaczyć, w jaki sposób w przeszłości wykorzystywano Sztolnię do transportu "
                           "węgla drogą wodną.\r\n",
            "ImagePath": "http://podziemia.pl/wp-content/uploads/2017/07/IMG_5102-scaled.jpg",
            "Longitude": 18.8062,
            "Latitude": 50.2957
        },
        {
            "ObjectId": 2,
            "Name": "Nieczynny kamieniołom wapieni triasowych Mikołów Mokre",
            "Description": "Nazwa Fiołkowej Góry pochodzi od kwitnących wiosną fiołków leśnych. Wzgórze zbudowane "
                           "jest z wapieni warstw gogolińskich. Wapienie te stanowiły surowiec do wypalania wapna, "
                           "o czym świadczy duża ilość (8, 13?) zachowanych na obrzeżach kamieniołomu wapienników. "
                           "Wapienniki to kamienno-ceglane budowle, służące w XVIII i XIX w. do wypalania wapna, "
                           "choć jeszcze do początku lat 80. XX wieku trwała eksploatacja.\r\nKamieniołom ma kształt "
                           "amfiteatralny. Ściany sięgają 20m wysokości i są dość dobrze zachowane. \r\nWyrobiska są "
                           "opuszczone i zarośnięte, można jednak znaleźć tu skamieniałości charakterystyczne dla "
                           "utworów węglanowych gónego triasu (liliowce, skorupy małży, ramienionogów, zęby ryb, "
                           "lub niewielkie kości gadów). Występują tu utwory triasu środkowego – wapienia muszlowego "
                           "dolnego. Na dolny wapień muszlowy składają się warstwy gogolińskie i dolomity "
                           "kruszconośne. Odsłaniające się w kamieniołomie warstwy gogolińskie, złożone są z "
                           "żółtoszarych wapieni, wapieni marglistych i margli o łącznej miąższości (w pełnym "
                           "profilu) 40 – 45 m. Warstwy gogolińskie nie mają większego znaczenia jako surowiec dla "
                           "przemysłu cementowo – wapienniczego, głównie ze względu na zmienną i niezbyt wysoką "
                           "jakość.\r\nNa terenie kamieniołomu znajduje się stara sztolnia z przełomu lat 20. i 30. "
                           "XX w, w której bytują nietoperze.\r\n",
            "ImagePath": "http://img3.garnek.pl/a.garnek.pl/031/259/31259833_800.0.jpg/mikolow-mokre-nieczynne.jpg",
            "Longitude": 18.8486,
            "Latitude": 50.1818
        }
    ]


def test_get_place_info():
    response = client.get("/place/1")
    assert response.status_code == 200
    assert response.json() == {
        "ObjectId": 1,
        "FreeParking": True,
        "OPMapLink": "421787802",
        "Name": "Sztolnia Królowa Luiza - Zabrze",
        "Description": "Sztolnia Królowa Luiza to połączenie dwóch górniczych, historycznych obiektów: Głównej "
                       "Kluczowej Sztolni Dziedzicznej (najdłuższy obiekty hydrotechniczny w europejskim górnictwie "
                       "węglowym) oraz Kopalni Królowa Luiza Do atrakcji należą: podziemny park maszyn górniczych, "
                       "zlokalizowany w dawnych wyrobiskach kopalni, trasa wodna oraz rozbudowana przestrzeń naziemna "
                       "z tematycznymi parkami rozrywkowo-edukacyjnymi. Sztolnia Królowa Luiza jest częścią Muzeum "
                       "Górnictwa Węglowego w Zabrzu.\r\nSztolnia jest wybitnym dziełem inżynierskim, "
                       "które dokumentuje poziom rozwoju techniki w I poł. XIX w. w zakresie budownictwa podziemnego. "
                       "Dzięki odpowiedniemu udostępnieniu można obecnie spływać łodziami na odcinku ok. 1100 m. W "
                       "podziemnym porcie załadunkowym w pokładzie węgla 509 turyści mogą zobaczyć, w jaki sposób w "
                       "przeszłości wykorzystywano Sztolnię do transportu węgla drogą wodną.\r\n",
        "ImagePath": "http://podziemia.pl/wp-content/uploads/2017/07/IMG_5102-scaled.jpg",
        "Longitude": 18.8062,
        "Latitude": 50.2957,
        "EasyAcces": True,
        "FreeEntry": False,
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


def test_get_disabilities():
    response = client.get("/disabilities/1")
    assert response.status_code == 200
    assert response.json() == {
        "ObjectId": 1,
        "DisabilitiesList": [
            "Rampa dla niepełnosprawnych "
        ]
    }


def test_get_get_osm_place_info():
    response = client.get("/osm/place/1")
    assert response.status_code == 200
    assert response.json() == {
        "addr:city": "Zabrze",
        "addr:housenumber": "410",
        "addr:postcode": "41-800",
        "addr:street": "Wolności",
        "name": "Sztolnia Królowa Luiza",
        "operator": "Muzeum Górnictwa Węglowego w Zabrzu",
        "tourism": "theme_park",
        "website": "https://www.sztolnialuiza.pl/"
    }


def test_get_wrong_place_name():
    response = client.get("/osm/place/22231")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "OSM ID not found"
    }


def test_get_address():
    response = client.get("/osm/address/1")
    assert response.status_code == 200
    assert response.json() == {
        "_json": [
            {
                "place_id": 184392168,
                "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                "osm_type": "way",
                "osm_id": 421787802,
                "lat": "50.29627445",
                "lon": "18.806930225464242",
                "display_name": "Sztolnia Królowa Luiza, 410, Wolności, Zaborze Południe, Zabrze, "
                                "Górnośląsko-Zagłębiowska Metropolia, województwo śląskie, 41-800, Polska",
                "address": {
                    "tourism": "Sztolnia Królowa Luiza",
                    "house_number": "410",
                    "road": "Wolności",
                    "city_district": "Zaborze Południe",
                    "city": "Zabrze",
                    "state_district": "Górnośląsko-Zagłębiowska Metropolia",
                    "state": "województwo śląskie",
                    "postcode": "41-800",
                    "country": "Polska",
                    "country_code": "pl"
                },
                "boundingbox": [
                    "50.2953218",
                    "50.297211",
                    "18.8055386",
                    "18.8079178"
                ]
            }
        ],
        "_queryString": "reverse",
        "_params": {
            "lat": 50.2957,
            "lon": 18.8062
        }
    }


def test_get_wrong_address():
    response = client.get("/osm/address/512312")
    assert response.status_code == 404


def test_get_directions():
    response = client.get("/osm/directions/start=8.681495,49.41461&stop=8.687872,49.420318")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["type"] == "FeatureCollection"
