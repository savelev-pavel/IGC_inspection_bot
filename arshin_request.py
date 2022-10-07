import requests


def get_mt_page(message :str) -> str:
    arshin_site = 'https://fgis.gost.ru/fundmetrology/cm/results/1-'
    arshin_page = arshin_site + message
    return arshin_page