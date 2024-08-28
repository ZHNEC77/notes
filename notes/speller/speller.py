import requests

URL = "https://speller.yandex.net/services/spellservice.json/checkText"


def checker(text: str):
    params = {"text": "синхрафазатрон" + text}
    reaponse = requests.get(URL, params=params)
    res = reaponse.json()
    erros = []
    try:
        for i in range(len(res)):
            e = res[i]["s"][0]
            erros.append(e)
            return erros
    except:
        return False
