import entities_order
import store

def main():
    money = 100
    tax = 0.15 * 100
    days = 0

    storage = {
        "beer": { "name": "Пиво", "amount": 10 },
        "salad": { "name": "Салат", "amount": 5 },
        "soup": { "name": "Суп", "amount": 7 },
        "wine": { "name": "Вино", "amount": 3 },
        "meat": { "name": "Жареное мясо", "amount": 8 },
        "bread": { "name": "Хлеб", "amount": 15 },
        "elf_bread": { "name": "Эльфийский хлеб", "amount": 4 },
        "bones": { "name": "Кости", "amount": 6 },
    }

    user_tavern_name = input("Введи название таверны: ")
    print(f"Это таверна {user_tavern_name}")

    

    while True:
        days += 1
        money -= tax
        print(f"День {days}")
        print(f"У нас {money} монет с вычетом налога")
        print("-----")
        if days == 0:
            print("В таверне есть:")
            for item, amount in storage.items():
                print(f"{item}: {amount}")
        print("-----")
        
        entities_order.entities_order_oop(money, storage, store.prices)
        store.store(money, storage)

        if money <= 0:
            print("Мы банкроты")
            break
        
        if money >= 500:
            print("Мы богаты")


main()