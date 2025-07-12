print(
'''
****************************************
***** Selamat datang di kalkulator *****
****************************************
'''
)

pilihan_user = int(input("Silahkan pilih menu : \n1. Penjumlahan \n2. Pengurangan \n3. Perkalian \n4. Pembagian \n5. Keluar \nMasukkan pilihan anda [1/2/3/4/5] : "))

angka_1 = angka_2 = angka_3 = angka_4 = angka_5 = 0

if pilihan_user == 1:
    print("Selamat datang di kalkulator penjumlahan")
    
    ulang_penjumlahan = True
    
    while ulang_penjumlahan:
        pilih_berapa_angka = int(input("Masukkan jumlah angka untuk dijumlahkan [2/3/4/5] : "))
        
        if pilih_berapa_angka == 2:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                
                hasil = angka_1 + angka_2
                
                print(f"Hasil penjumlahan {angka_1} + {angka_2} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    ulang_penjumlahan = False
                    break
            
        elif pilih_berapa_angka == 3:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                
                hasil = angka_1 + angka_2 + angka_3
                
                print(f"Hasil penjumlahan {angka_1} + {angka_2} + {angka_3} = {hasil}")
                
                if ulang.lower() == "n":
                    ulang_penjumlahan = False
                    break
        
        elif pilih_berapa_angka == 4:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                
                hasil = angka_1 + angka_2 + angka_3 + angka_4
                
                print(f"Hasil penjumlahan {angka_1} + {angka_2} + {angka_3} + {angka_4} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    ulang_penjumlahan = False
                    break
                
        elif pilih_berapa_angka == 5:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                angka_5 = int(input("Masukkan angka kelima : "))
                
                hasil = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
                
                print(f"Hasil penjumlahan {angka_1} + {angka_2} + {angka_3} + {angka_4} + {angka_5} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    ulang_penjumlahan = False
                    break
                
        else:
            print("Pilihan tidak tersedia")
            ulang = input("Ulangi lagi? (y/n) : ")
            if ulang.lower() == "n":
                ulang_penjumlahan = False
                break
  
elif pilihan_user == 2:
    print("Selamat datang di kalkulator pengurangan")
    
    pengurangan = True
    
    while pengurangan:
        pilih_berapa_angka = int(input("Masukkan jumlah angka untuk dikurangkan [2/3/4/5] : "))
        
        if pilih_berapa_angka == 2:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                    
                hasil = angka_1 - angka_2
                    
                print(f"Hasil pengurangan {angka_1} - {angka_2} = {hasil}")
                    
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pengurangan = False
                    break
        
        elif pilih_berapa_angka == 3:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                
                hasil = angka_1 - angka_2 - angka_3
                
                print(f"Hasil pengurangan {angka_1} - {angka_2} - {angka_3} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pengurangan = False
                    break
                
        elif pilih_berapa_angka == 4:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                
                hasil = angka_1 - angka_2 - angka_3 - angka_4
                
                print(f"Hasil pengurangan {angka_1} - {angka_2} - {angka_3} - {angka_4} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pengurangan = False
                    break 
                              
        elif pilih_berapa_angka == 5:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                angka_5 = int(input("Masukkan angka kelima : "))
                
                hasil = angka_1 - angka_2 - angka_3 - angka_4 - angka_5
                
                print(f"Hasil pengurangan {angka_1} - {angka_2} - {angka_3} - {angka_4} - {angka_5} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pengurangan = False
                    break               
          
elif pilihan_user == 3:
    print("Selamat datang di kalkulator perkalian")
    
    perkalian = True
    
    while perkalian:
        pilih_berapa_angka = int(input("Masukkan jumlah angka untuk dikalikan [2/3/4/5] : "))
        
        if pilih_berapa_angka == 2:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                    
                hasil = angka_1 * angka_2
                    
                print(f"Hasil perkalian {angka_1} * {angka_2} = {hasil}")
                    
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    perkalian = False
                    break
        
        elif pilih_berapa_angka == 3:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                
                hasil = angka_1 * angka_2 * angka_3
                
                print(f"Hasil perkalian {angka_1} * {angka_2} * {angka_3} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    perkalian = False
                    break
                
        elif pilih_berapa_angka == 4:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                
                hasil = angka_1 * angka_2 * angka_3 * angka_4
                
                print(f"Hasil perkalian {angka_1} * {angka_2} * {angka_3} * {angka_4} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    perkalian = False
                    break 
                              
        elif pilih_berapa_angka == 5:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                angka_5 = int(input("Masukkan angka kelima : "))
                
                hasil = angka_1 * angka_2 * angka_3 * angka_4 * angka_5
                
                print(f"Hasil perkalian {angka_1} * {angka_2} * {angka_3} * {angka_4} * {angka_5} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    perkalian = False
                    break               
          
elif pilihan_user == 4:
    print("Selamat datang di kalkulator pembagian")
    
    pembagian = True
    
    while pembagian:
        pilih_berapa_angka = int(input("Masukkan jumlah angka untuk dibagi [2/3/4/5] : "))
        
        if pilih_berapa_angka == 2:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                    
                hasil = angka_1 / angka_2
                    
                print(f"Hasil pembagian {angka_1} / {angka_2} = {hasil}")
                    
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pembagian = False
                    break
        
        elif pilih_berapa_angka == 3:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                
                hasil = angka_1 / angka_2 / angka_3
                
                print(f"Hasil pembagian {angka_1} / {angka_2} / {angka_3} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pembagian = False
                    break
                
        elif pilih_berapa_angka == 4:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                
                hasil = angka_1 / angka_2 / angka_3 / angka_4
                
                print(f"Hasil pembagian {angka_1} / {angka_2} / {angka_3} / {angka_4} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pembagian = False
                    break 
                              
        elif pilih_berapa_angka == 5:
            while True:
                angka_1 = int(input("Masukkan angka pertama : "))
                angka_2 = int(input("Masukkan angka kedua : "))
                angka_3 = int(input("Masukkan angka ketiga : "))
                angka_4 = int(input("Masukkan angka keempat : "))
                angka_5 = int(input("Masukkan angka kelima : "))
                
                hasil = angka_1 / angka_2 / angka_3 / angka_4 / angka_5
                
                print(f"Hasil pembagian {angka_1} / {angka_2} / {angka_3} / {angka_4} / {angka_5} = {hasil}")
                
                ulang = input("Ulangi lagi? (y/n) : ")
                if ulang.lower() == "n":
                    pembagian = False
                    break               
          
elif pilihan_user == 5:
    print("Terima kasih telah menggunakan kalkulator ini")
else:
    print("Pilihan tidak tersedia")