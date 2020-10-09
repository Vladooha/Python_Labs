import csv

with open('items.csv', 'r+', newline="", encoding="utf8") as items_file:
    items = csv.DictReader(items_file, delimiter=';')
    columns = items.fieldnames
    min_price_item = None
    max_price_item = None
    for item in items:
        price = item["Цена"]
        if min_price_item is None or min_price_item["Цена"] > price:
            min_price_item = item
        if max_price_item is None or max_price_item["Цена"] < price:
            max_price_item = item
    
    with open('result.csv', 'w+', newline="", encoding="utf8") as result_file:
        item_writer = csv.DictWriter(result_file, fieldnames = columns)
        item_writer.writeheader()
        item_writer.writerows([min_price_item, max_price_item])