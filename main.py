import requests
from requests.structures import CaseInsensitiveDict
print('TESTE POSICOES')

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

idUser = "D9DBFAC2D9B25C1293B03C041A42F249"
data = '{"encryptedUid":"D9DBFAC2D9B25C1293B03C041A42F249","tradeType":"PERPETUAL"}'
url = "https://www.binance.com/gateway-api/v1/public/future/leaderboard/getOtherPosition"
r = requests.post(url, headers=headers, data=data)
posicao = r.text
print(r.status_code)
print(posicao)
