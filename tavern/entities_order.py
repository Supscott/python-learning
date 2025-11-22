import random

NAMES = ["Петя", "Вася", "Коля", "Оля", "Миша", "Legolas", "Gimli", "Bob"]

RACES_INFO = [
        ("Elf", 50, 100, ["elf_bread", "wine", "salad"]),
        ("Orc", 5, 20, ["meat", "beer", "bones"]),
        ("Human", 20, 60, ["bread", "beer", "meat", "soup"])
    ]

class Guest:

    def __init__(self, race, name, min_money, max_money, preferences):
        self.race = race
        self.name = name
        self.money = random.randint(min_money, max_money)
        self.preferences = preferences 

    def pay(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            return False

    def __str__(self):
        return f"{self.race} {self.name}"

def spawn_guest():
    choice = random.choice(RACES_INFO)
    
    new_guest = Guest(choice[0], random.choice(NAMES), choice[1], choice[2], choice[3])
    return new_guest

def entities_order_oop(tavern_money, storage, prices):
    guest = spawn_guest()
    print(f"--- Дзинь! ---")
    print(f"Вошел: {guest}")

    wanted_food = random.choice(guest.preferences)
    food_name_ru = storage[wanted_food]["name"]
    print(f"Он хочет заказать: {food_name_ru}")


    if wanted_food in storage:
        price = prices[wanted_food]["sell"]

        if storage[wanted_food]["amount"] > 0:

            if guest.pay(price):               
                storage[wanted_food]["amount"] -= 1 
                tavern_money += price
                print(f"{guest.name} с удовольствием съел {food_name_ru}.")
            
        else:
            food_name_ru = storage[wanted_food]["name"]
            print(f"У {guest.name} не хватило денег на {food_name_ru}!")
    else:
        print(f"Официант: 'Мы такое не готовим!'")
        print(f"{guest.name} смотрит на вас как на идиота.")

    return tavern_money