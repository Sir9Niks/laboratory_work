import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    products_sum = sum(item['score'] * item['weight'] for item in data)
    rounded_sum = round(products_sum, 3)

    return rounded_sum


print(task())