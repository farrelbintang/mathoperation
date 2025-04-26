print("*" * 41)
print(f"**" + "WELCOME TO BASIC MATH OPERATION TOOLS" + "**")
print("*" * 41)

user_nama_depan = input("Masukkan nama depan anda = ")
user_nama_belakang = input("Masukkan nama belakang anda = ")

def sapa_user(nama_depan, nama_belakang):
    
    print(f"\nHi.. {nama_depan} {nama_belakang}")
    print("Ini adalah tool matematika sederhana, yang bertujuan untuk menjadi kalkulator sederhana yang memudahkan dalam menghitung operasi dalam matematika.")
sapa_user(user_nama_depan, user_nama_belakang)

ulang = True
while ulang:
    perintah = input("\nKetik 'menu' untuk memilih operasi bilangan = ")
    if perintah.lower() == "menu":
        print("\nketik [1] - untuk operasi pertambahan.")
        print("ketik [2] - untuk operasi pengurangan.")
        print("ketik [3] - untuk operasi perkalian.")
        print("ketik [4] - untuk operasi pembagian.")
        perintah2 = input("\nSilakan masukkan nomor yang anda inginkan = ")
        if perintah2 == "1":
            print("\nSilahkan masukkan data yang diperlukkan seperti angka yang ingin ditambah dan angka tersebut ingin ditambah dengan berapa.")
            user_input_tambah = int(input("\nSilahkan masukkan angka = "))
            user_input_operasi_tambah = int(input("Ingin ditambah dengan berapa = "))
            operasi_tambah = user_input_tambah + user_input_operasi_tambah
            print(f"\nMaka, hasilnya adalah {operasi_tambah}")
        elif perintah2 == "2":
            print("\nSilahkan masukkan data yang diperlukkan seperti angka yang ingin dikurang dan angka tersebut ingin dikurang dengan berapa.")
            user_input_kurang = int(input("\nSilahkan masukkan angka = "))
            user_input_operasi_kurang = int(input("Ingin dikurang dengan berapa = "))
            operasi_kurang = user_input_kurang - user_input_operasi_kurang
            print(f"\nMaka, hasilnya adalah {operasi_kurang}")
        elif perintah2 == "3":
            print("\nSilahkan masukkan data yang diperlukkan seperti angka yang ingin dikali dan angka tersebut ingin dikali dengan berapa.")
            user_input_kali = int(input("\nSilahkan masukkan angka = "))
            user_input_operasi_kali = int(input("Ingin dikali dengan berapa = "))
            operasi_kali = user_input_kali * user_input_operasi_kali
            print(f"\nMaka, hasilnya adalah {operasi_kali}")
        elif perintah2 == "4":
            print("\nSilahkan masukkan data yang diperlukkan seperti angka yang ingin dibagi dan angka tersebut ingin dibagi dengan berapa.")
            user_input_bagi = int(input("\nSilahkan masukkan angka = "))
            user_input_operasi_bagi = int(input("Ingin dibagi dengan berapa = "))  
            operasi_bagi = user_input_bagi / user_input_operasi_bagi
            print(f"\nMaka, hasilnya adalah {operasi_bagi}")                
    else:
        print("Maaf, saya tidak mengerti hal itu.")
        
lanjut = input("Apakah ingin menggunakan tool ini lagi? (ya/tidak)")
if lanjut.lower() != "ya":
    ulang = False
    print("\nYahhhhh.... Terimakasih telah menggunakan tool ini, terima kasih😁😁😁😁")
