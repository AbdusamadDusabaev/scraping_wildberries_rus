import csv
import pathlib


def create_seller_csv():
    path = pathlib.Path("result", "seller.csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Название продавца", "Юридический адрес", "ОГРН", "ОГРНИП", "ИНН"])


def create_product_csv(file_name, mode):
    path = pathlib.Path("result", f"{file_name}.csv")
    if mode == "shop":
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Название товара", "Описание", "Характеристики",
                             "Цена без скидки", "Цена со скидкой", "Рейтинг", "Отзывы",
                             "Заказы", "Бренд", "Ссылка на товар"])
    elif mode == "brand":
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Название товара", "Описание", "Характеристики",
                             "Цена без скидки", "Цена со скидкой", "Рейтинг", "Отзывы",
                             "Заказы", "Магазин", "Ссылка на магазин", "Ссылка на товар"])
    else:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Название товара", "Описание", "Характеристики",
                             "Цена без скидки", "Цена со скидкой", "Рейтинг", "Отзывы",
                             "Заказы", "Бренд", "Магазин", "Ссылка на магазин", "Ссылка на товар"])
