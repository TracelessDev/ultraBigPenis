import random

def attack(mstrHP):
    damage = random.randint(10, 25)
    mstrHP -= damage

    if mstrHP < 0:
        mstrHP = 0
    print("Вы нанесли монстру", damage, "дамага")
    return mstrHP

def mstrAttack(plrHP):
    damage = random.randint(5, 20)
    plrHP -= damage

    if plrHP < 0:
        plrHP = 0
    print("Монстр нанес вам", damage, "дамага")
    return plrHP

def heal(plrHP):
    if plrHP == 100:
        print("Здоровье уже полное")
    else:
        plrHP = min(plrHP +15, 100)
        print("Вы восстановили хп")
    return plrHP

def show_status(plrHP, mstrHP):
    print("Ваше хп:", plrHP)
    print("Хп монстра:", mstrHP)

def main():
    plrHP = 100
    mstrHP = 100
    while plrHP > 0 and mstrHP > 0:
        print("\nБитва инвалидов. Вы - творцы истории.")
        print("1 - отпиздить")
        print("2 - захиллиться")
        print("3 - показать хп")
        print("4 - съебаться")

        choice = input("\tВыберите действие: ")

        if choice == "1":
            mstrHP = attack(mstrHP)
            if mstrHP > 0:
                plrHP = mstrAttack(plrHP)
        
        elif choice == "2":
            oldHP = plrHP
            plrHP = heal(plrHP)
            if plrHP > oldHP:
                mstrHP_check = mstrAttack
                plrHP = mstrHP_check
        
        elif choice == "3":
            show_status(plrHP, mstrHP)

        elif choice == "4":
            print("Вы успешно съебались")
            break

        else:
            print("Введи корректную команду, еблан!")

        if plrHP <= 0:
            print("Сосо, ты проиграл")
            
        elif mstrHP <= 0:
            print("Легенда, ты выиграл")
            
    
main()