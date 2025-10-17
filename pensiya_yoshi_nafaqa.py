jins = input("Jins kiriting: ").lower()
yosh = int(input("Yoshingizni kiriting: "))

if jins == "ayol" and yosh >= 55 or jins == "ayol" and yosh <= 120:
    print("Buvimiz nafaqa yoshida!")
    print(f"Siz {yosh % 55} yildan beri nafaqadasiz!")
elif jins == "erkak" and yosh >= 60 or jins == "erkak" and yosh <= 120:
    print("Bobomiz nafaqa yoshida!")
    print(f"Siz {yosh % 60} yildan beri nafaqadasiz!")
elif jins ==  "erkak" or jins == "ayol" and yosh > 120 and yosh < 0:
    print("Ma'lumotlar noto'g'ri kiritilgan!")
