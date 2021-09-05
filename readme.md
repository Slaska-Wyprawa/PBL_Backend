# Uruchomienie 
    `uvicorn main:app --reload`
    Trzeba usunąć poprzednie bilioteki i zainstalować te z requirements.
# Testy 
`pytest`
 Testy na ten moment nie przechodzą z błędami: 
 ```FAILED test_main.py::test_get_two_places_info - TypeError: unhashable type: 'list'
FAILED test_main.py::test_get_place_info - NameError: name 'true' is not defined
```
