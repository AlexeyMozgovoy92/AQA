from random import randint

class Horse:
    count = 0
    def __init__(self, color, breed, name):
        self.hooves = 4
        self.color = color
        self.breed = breed
        self.name = name
        self.jokey = ""
        Horse.count +=1

    def set_jokey(self, jokeyName):
        self.jokey = jokeyName

    def nicker(self):
        return "Иго-го"

    def hop(self):
        return "Скачууу"

    def eat(self):
        return "Ням-ням"

class Jokey:
    def __init__(self, name, Horse):
        self.name = name
        self.Horse = Horse

    def name_jokey(self, name):
        self.name = name

"""    def ride(self):
        Horse.hop()"""


def winner(win_h):
    if win_h == 1:
        return Horse1.name
    elif win_h == 2:
        return Horse2.name
    else:
        return Horse3.name

def win_jokey(win_h):
    if win_h == 1:
        return jokey1.name
    elif win_h == 2:
        return jokey2.name
    else:
        return jokey3.name


###########################
if __name__ == '__main__':
    win_h = randint(1, 4)


    Horse1 = Horse("белый", "андалузская", "Молли")
    Horse2 = Horse("коричневый", "Морган", "Морган")
    Horse3 = Horse("чёрный", "Фризская", "Пуля")

    jokey1 = Jokey("Стэфан", Horse1)
    jokey2 = Jokey("Франциско", Horse2)
    jokey3 = Jokey("Фернандо", Horse3)

    Horse1.set_jokey(jokey1.name)
    Horse2.set_jokey(jokey2.name)
    Horse3.set_jokey(jokey3.name)

    print(f"{Horse.count} лошадки в забеге, давайте знакомиться:")
    print("*" * 30)
    print(f"1 - я лошадка: \nИмя лошадки:  {Horse1.name} \nИмя жокея: {jokey1.name} \nПорода:  {Horse1.breed} \nЦвет:  {Horse1.color} \nКоличество копыт: {Horse1.hooves}")
    print(f"Приветствие от {Horse1.name} - {Horse1.nicker()}")

    print("*" * 30)
    print(f"2 - я лошадка: \nИмя лошадки:  {Horse2.name} \nИмя жокея {jokey2.name}\nПорода:  {Horse2.breed} \nЦвет:  {Horse2.color} \nКоличество копыт: {Horse2.hooves}")
    print(f"Приветствие от {Horse2.name} - {Horse2.hop()}")

    print("*" * 30)
    print(f"3 - я лошадка: \nИмя лошадки:  {Horse3.name} \nИмя жокея: {jokey3.name}\nПорода:  {Horse3.breed} \nЦвет:  {Horse3.color} \nКоличество копыт: {Horse3.hooves}")
    print(f"Приветствие от {Horse3.name} - {Horse3.eat()}")

    print(f"\n!!! Забег состоялся. В забеге участвовало {Horse.count} лошадки и победила  *** {winner(win_h)} *** Жокей: {win_jokey(win_h)} *** !!!")


