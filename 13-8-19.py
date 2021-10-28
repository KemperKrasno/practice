try:
    kol_biletov = input("Введите количество билетов. При регистрации более 3 человек скидка 10%:")
    kol_biletov = int(kol_biletov)
except ValueError as error:
    print("Ведите количество билетов. ЧИСЛАМИ!:")
    kol_biletov = input()
    kol_biletov = int(kol_biletov)
else:
    summa = 0
    for i in range(1, kol_biletov + 1):
        print("Введите возраст держателя", i, "билета:")
        try:
            vozrast = input()
            vozrast = int(vozrast)
            if vozrast <= 0:
                print("Возраст не может быть меньше или равен 0!")
                print("Введите возраст держателя", i, "билета:")
                vozrast = input()
                vozrast = int(vozrast)
        except ValueError as error:
            print("Введите возраст держателя", i, "билета. ЧИСЛАМИ!:")
            vozrast = input()
            vozrast = int(vozrast)
        else:
            if 0 < vozrast < 18 :
                summa = summa + 0
            if 18 <= vozrast < 25 :
                summa = summa + 990
            if vozrast >= 25 :
                summa = summa + 1390
if kol_biletov > 3 :
    summa = summa - (summa * 0.1)
print("Сумма к оплате:", summa)