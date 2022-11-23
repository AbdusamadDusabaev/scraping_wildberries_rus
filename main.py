import time
from create_file_csv import create_seller_csv, create_product_csv
from get_id import get_brand_id, get_shop_id, get_seller_info
from get_info_via import get_info_via_shop, get_info_via_brand, get_info_via_query


def main():
    program_mode_templates = "(shop - анализ магазина, brand - анализ бренда, query - анализ поискового запроса)"
    input_text = f"Выберете режим программы {program_mode_templates}: "
    program_mode = input(input_text)

    if program_mode == "shop":
        url_templates = "(https://www.wildberries.ru/seller/8475, https://www.wildberries.ru/seller/9853, ...)"
        input_text = f"Введите ссылки на магазины через запятую {url_templates}: \n"
        urls = input(input_text)
        urls = [url.strip() for url in urls.split(",")]
        print("[INFO] Программа запущена, идет анализ магазинов: ")
        urls_string = "\n       ".join(urls)
        print(f"       {urls_string}")

        create_seller_csv()
        for url in urls:
            start_time = time.time()
            file_name = get_shop_id(shop_url=url)
            create_product_csv(file_name=file_name, mode=program_mode)
            get_info_via_shop(shop_url=url, file_name=file_name)
            get_seller_info(seller_id=get_shop_id(shop_url=url))
            print()
            print("=" * 100)
            print(f"Парсинг магазина {url} закончен")
            print(f"На парсинг ушло {time.time() - start_time} секунд")
    elif program_mode == "brand":
        url_templates = "(https://www.wildberries.ru/brands/timejump, https://www.wildberries.ru/brands/nuro, ...)"
        input_text = f"Введите ссылки на бренды через запятую {url_templates}: \n"
        urls = input(input_text)
        urls = [url.strip() for url in urls.split(",")]
        print("[INFO] Программа запущена, идет анализ брендов: ")
        urls_string = "\n       ".join(urls)
        print(f"       {urls_string}")

        create_seller_csv()
        for url in urls:
            start_time = time.time()
            file_name = url.split("/")[-1]
            create_product_csv(file_name=file_name, mode=program_mode)
            get_info_via_brand(brand_url=url, file_name=file_name)
            get_seller_info(seller_id=get_brand_id(brand_url=url))
            print()
            print("=" * 100)
            print(f"Парсинг бренда {url} закончен")
            print(f"На парсинг ушло {time.time() - start_time} секунд")
    else:
        queries_templates = "(телефон, наушники и зарядка, мужские туфли, ...)"
        input_text = f"Введите текст поисковых запросов через запятую {queries_templates}: \n"
        queries = input(input_text)
        queries = [query.strip() for query in queries.split(",")]
        print("[INFO] Программа запущена, идет анализ запросов: ")
        queries_string = "\n       ".join(queries)
        print(f"       {queries_string}")

        create_seller_csv()
        for query in queries:
            start_time = time.time()
            create_product_csv(file_name=query, mode=program_mode)
            get_info_via_query(query=query, file_name=query)
            print()
            print("=" * 100)
            print(f"Парсинг запроса {query} закончен")
            print(f"На парсинг ушло {time.time() - start_time} секунд")


if __name__ == "__main__":
    main()
