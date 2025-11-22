import entities_order
import store

def main():
    money = 100
    tax = 0.15 * 100
    days = 0

    storage = {
        "beer": 10,
        "wine": 5,
        "meat": 3,
        "bread": 10,
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
        
        money = entities_order.entities_order_oop(money, storage, store.prices)
        money = store.store(money, storage)

        if money <= 0:
            print("Мы банкроты")
            break
        
        if money >= 500:
            print("Мы богаты")


main()