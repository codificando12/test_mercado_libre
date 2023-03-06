import json

def export_json(titles, prices):
    titles_prices = {}


    for key in range(len(titles)):
        titles_prices[titles[key]] = prices[key]
    
    with open("items.json", 'w') as file:
        json.dump(titles_prices, file)


if __name__ == '__main__':
    export_json()
