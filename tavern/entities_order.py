import random

# 1. Создаем "Чертеж" гостя
class Guest:
    # __init__ - это конструктор. Он запускается, когда рождается новый гость.
    # self - это ссылка на КОНКРЕТНОГО гостя (чтобы не перепутать Петю с Васей)
    def __init__(self, race, name, min_money, max_money):
        self.race = race        # Запоминаем расу
        self.money = random.randint(min_money, max_money) # Даем денег
        self.patience = 3       # Уровень терпения (если товара нет, оно падает)
        self.name = name

    # Метод: Гость пытается заплатить
    def pay(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True # Успешно заплатил
        else:
            return False # Денег нет, бака!

    # Метод: Красивый вывод информации (чтобы не видеть <__main__.Guest object>)
    def __str__(self):
        return f"{self.race} {self.name} (Кошелек: {self.money})"


def spawn_guest():
    names = ["Петя", "Вася", "Коля", "Оля", "Миша", "Legolas", "Gimli", "Bob"]

    races_info = [
        ("Elf", 50, 100),
        ("Orc", 5, 20),
        ("Human", 20, 60)
    ]
    choice = random.choice(races_info)
    # Создаем ОБЪЕКТ класса Guest
    new_guest = Guest(choice[0], random.choice(names), choice[1], choice[2]) 
    return new_guest

# Твоя функция, переделанная под классы
def entities_order_oop(tavern_money, storage, prices):
    # Генерируем случайного гостя (уже с деньгами и характером!)
    guest = spawn_guest()
    
    print(f"--- Дзинь! Дверь открылась ---")
    print(f"Вошел: {guest}") # Тут сработает наш def __str__

    # Гость выбирает, что хочет
    order = random.choice(list(storage.keys()))
    print(f"Он хочет заказать: {order}")

    price = prices[order]["sell"]

    # Логика проверки
    if storage[order] > 0:
        # Проверяем, может ли гость заплатить своим личным методом
        if guest.pay(price):
            storage[order] -= 1
            tavern_money += price
            print(f"{guest.race} доволен и заплатил {price} монет.")
        else:
            print(f"У {guest.race} не хватило денег! Какая жалость.")
    else:
        print(f"Товара '{order}' нет! {guest.race} устроил скандал.")
        # Тут можно уменьшить терпение гостя или вычесть деньги за ущерб
        tavern_money -= 5 

    return tavern_money