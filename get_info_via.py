import requests
from config import headers
from get_id import get_shop_id, get_brand_id
from get_product_info import get_product_info


def get_info_via_shop(shop_url, file_name):
    shop_id = get_shop_id(shop_url=shop_url)

    page = 0
    check = True

    while check:
        page += 1
        api_url = f"https://catalog.wb.ru/sellers/catalog?appType=1&supplier={shop_id}&page={page}"
        response = requests.get(url=api_url, headers=headers)
        products = response.json()["data"]["products"]
        for product in products:
            get_product_info(product=product, mode="shop", file_name=file_name)
        if len(products) == 0:
            check = False


def get_info_via_brand(brand_url, file_name):
    brand_id = get_brand_id(brand_url=brand_url)

    check = True
    page = 0

    while check:
        page += 1
        api_url = f"https://catalog.wb.ru/brands/d/catalog?appType=1&brand={brand_id}&page={page}"
        response = requests.get(url=api_url, headers=headers)
        products = response.json()["data"]["products"]
        for product in products:
            get_product_info(product=product, mode="brand", file_name=file_name)
        if len(products) == 0:
            check = False


def get_info_via_query(query, file_name):
    query = "%20".join(query.split(" "))
    api_url_part_1 = "https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&"
    check = True
    page = 0

    while check:
        page += 1
        api_url = f"{api_url_part_1}dest=-1029256,-102269,-2162196,-1257786&query={query}&resultset=catalog&page={page}"
        response = requests.get(url=api_url, headers=headers)
        products = response.json()["data"]["products"]
        for product in products:
            get_product_info(product=product, mode="query", file_name=file_name)
        if len(products) == 0:
            check = False
