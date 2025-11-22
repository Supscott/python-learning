prices = {
        "beer": {
            "name": "Пиво",
            "sell": 5,
            "buy": 2.5,
        },
        "salad": {
            "name": "Салат",
            "sell": 7,
            "buy": 3.5,
        },
        "soup": {
            "name": "Суп",
            "sell": 8,
            "buy": 4,
        },
        "wine": {
            "name": "Вино",
            "sell": 10,
            "buy": 5,
        },
        "meat": {
            "name": "Жареное мясо",
            "sell": 20,
            "buy": 10,
        },
        "bread": {
            "name": "Хлеб",
            "sell": 15,
            "buy": 7.5,
        },
        "elf_bread": {
            "name": "Эльфийский хлеб",
            "sell": 25,
            "buy": 12.5,
        },
        "bones": {"name": "Кости","sell": 3,"buy": 1.5,},
    }

def store(money, storage):
    print(f"\n")
    print(f"{'Товар':<20} | {'Кол-во':<5}") 
    print("-" * 30)

    for key, info in storage.items():
        print(f"{info['name']:<20} | {info['amount']:<5}")

    print(f"\n")
    print(f"У нас {money} монет")

    print(f"\n")
    print(f"Вы можете купить:")
    print(f"{'Товар':<20} | {'Цена':<5}") 
    print("-" * 30)
    for key, info in prices.items():
        print(f"{info['name']:<20}: {info['buy']} монет")

    userInput = input("Что вы хотите купить? ")    

    if userInput in prices:
        if money >= prices[userInput]["buy"]:
            storage[userInput]["amount"] += 1
            money -= prices[userInput]["buy"]
            print(f"Вы купили {userInput}")
        else:
            print("У нас не хватает денег")
    else:
        print("Нет такого товара")

    print("-----")
    return money