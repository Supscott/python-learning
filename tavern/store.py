prices = {
        "beer": {
            "sell": 5,
            "buy": 2.5,
        },
        "wine": {
            "sell": 10,
            "buy": 5,
        },
        "meat": {
            "sell": 20,
            "buy": 10,
        },
        "bread": {
            "sell": 15,
            "buy": 7.5,
        },
    }

def store(money, storage):
    print("-----")
    print("В таверне есть:")
    for item, amount in storage.items():
        print(f"{item}: {amount}")

    print(f"У нас {money} монет")

    print(f"Вы можете купить:")
    for item, price in prices.items():
        print(f"{item}: {price['buy']} монет")

    userInput = input("Что вы хотите купить? ")    

    if userInput in prices:
        if money >= prices[userInput]["buy"]:
            storage[userInput] += 1
            money -= prices[userInput]["buy"]
            print(f"Вы купили {userInput}")
        else:
            print("У нас не хватает денег")
    else:
        print("Нет такого товара")

    print("-----")
    return money