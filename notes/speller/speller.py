import requests

URL = "https://speller.yandex.net/services/spellservice.json/checkText"


def checker(text: str):
    params = {"text": "синхрафазатрон" + text}
    reaponse = requests.get(URL, params=params)
    print(reaponse)
    res = reaponse.json()
    # print(res)
    erros = []
    try:
        for i in range(len(res)):
            e = res[i]["s"][0]
            # print(e)
            erros.append(e)
        return erros
    except:
        return False
