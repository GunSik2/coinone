import json
import urllib.request
import logging, sys

class coinone:
    urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/ticker/?format=json&currency=all')
    readTicker = urlTicker.read().decode('utf8')

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # debug, info, warning, error and critical
    logging.debug(readTicker)

    jsonTicker = json.loads(readTicker)
    FindETC = jsonTicker['etc']['last']
    ETC = int(FindETC)
    FindBTC = jsonTicker['btc']['last']
    BTC = int(FindBTC)
    FindETH = jsonTicker['eth']['last']
    ETH = int(FindETH)
    FindXRP = jsonTicker['xrp']['last']
    XRP = int(FindXRP)


