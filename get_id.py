import requests
import csv
from config import headers
import pathlib


def get_brand_id(brand_url):
    brand_url_list = brand_url.split("/")
    brand_index = brand_url_list.index("brands") + 1
    brand = brand_url_list[brand_index]
    api_url = f"https://static.wbstatic.net/data/brands/{brand}.json"
    response = requests.get(url=api_url, headers=headers)
    brand_id = response.json()["id"]

    return brand_id


def get_shop_id(shop_url):
    shop_url_list = shop_url.split("/")
    seller_index = shop_url_list.index("seller") + 1
    shop_id = shop_url_list[seller_index]
    return shop_id


def get_seller_info(seller_id):
    api_url = f"https://www.wildberries.ru/webapi/seller/data/short/{seller_id}"
    response = requests.get(url=api_url, headers=headers)
    json_object = response.json()
    seller_name = json_object["name"]
    if "legalAddress" in json_object:
        seller_legal_address = json_object["legalAddress"]
    else:
        seller_legal_address = "Нет данных на Wildberries"
    if "ogrn" in json_object:
        seller_ogrn = json_object["ogrn"]
    else:
        seller_ogrn = "Нет данных на Wildberries"
    if "ogrnip" in json_object:
        seller_ogrnip = json_object["ogrnip"]
    else:
        seller_ogrnip = "Нет данных на Wildberries"
    if "inn" in json_object:
        seller_inn = json_object["inn"]
    else:
        seller_inn = "Нет данных на Wildberries"
    path = pathlib.Path("result", "seller.csv")
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([seller_name, seller_legal_address, seller_ogrn, seller_ogrnip, seller_inn])
