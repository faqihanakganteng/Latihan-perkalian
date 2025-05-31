import random

nomor1 = random.randint(1, 50)
nomor2 = random.randint(1, 10)

kali = nomor1 * nomor2

username = input("Masukan nama kamu: ")

print(f"Selamat datang {username}! Ayo latihan perkalian bersamaku!")

pilihan_user = int(input(f"Berapa hasil dari {nomor1} × {nomor2}? : "))

if pilihan_user == kali:
    print("Selamat kamu benar!")
else:
    print(f"Yaaah..... Kamu salah, Hasil dari {nomor1} × {nomor2} adalah {kali}")