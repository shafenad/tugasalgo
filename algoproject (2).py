import os, json


def clean():
   
    os.system('cls')

barangbelanja = []
hargabarang = []
totalharga = 0

def baca_laporan():
    try:
        with open("hasilbelanja.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        with open("hasilbelanja.json", "w") as file:
            kosong = []
            json.dump(kosong, file, indent=2)
            return kosong

def tulis_ulangJson(baru):
    with open("hasilbelanja.json", "w") as file:
        json.dump(baru, file, indent=2)

def laporan():
    with open("hasilbelanja.json", "r") as data:
        reader = json.load(data)
        print ('Berikut adalah laporan pembelian anda')
        print ( '-' * 50 )  
        print(reader)

def belanjatani():
 while True :
    baca_laporan()
    clean()
    print("\nhalo", nama)
    print('Apa Yang Ingin Anda Beli?')
    print("Kategori:\n 1. Pupuk \n 2. Bibit \n")
    pilihan = int(input('Masukkan kode 1-2 untuk memilih kategori yang diinginkan:'))
    if pilihan == 1:
        pupuk()
    elif pilihan == 2 :
        bibit()
    print(" \n 1.Lanjut Berbelanja\n 2.Checkout \n ")
    user = int(input("Masukkan Angka 1-2yang anda inginkan:"))
    if user == 1 :
        belanjatani()
    elif user == 2 :
        checkout()
        print('Terima kasih telah berbelanja di Tanipedia, laporan pembelian anda akan tercetak secara otomatis')
    break
    



def pupuk():
    clean()
    print ('Beberapa Produk teratas dari kami :')
    print (' 1. Pupuk Kandang Setia Tani\n 2. Pupuk Digrow Hijau\n 3. Pupuk Kompos Bokhasi\n 4. Pupuk Kompos Bokhasi\n 5. Pupuk Humic Acid Humus\n 6. Kembali')
    pupuk1 = ['Pupuk Kandang Setia Tani', 34000]
    pupuk2 = ['Pupuk Digrow Hijau', 43000]
    pupuk3 = ['Pupuk Kompos Bokhasi', 21000]
    pupuk4 = ['Pupuk Hayati Organik Micorin', 27000]
    pupuk5 = ['Pupuk Humic Acid Humus', 68000]
    new_4 = int(input('\nMasukkan barang yang ingin dibeli:'))
    if new_4 == 1 :
        print(" Pupuk Kandang Setia Tani (Rp34.000,-)\n \n> dari kotoran hewan \n> memperbaiki kesuburan dan struktur tanah \n> perbaikan struktur tanah \n> penyediaan unsur hara")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(pupuk1[0])
            hargabarang.append(pupuk1[1])
        else:
            pupuk()
    elif new_4 == 2 :
        print(" Pupuk Digrow Hijau (Rp43.000,-)\n  \n> dari tumbuhan \n> menambah unsur hara tanah, terutama nitrogen \n> perbaikan sifat fisik, kimia dan biologi tanah \n> ketahanan tanah terhadap erosi")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(pupuk2[0])
            hargabarang.append(pupuk2[1])
        else:
            pupuk()
    elif new_4 == 3 :
        print(" Pupuk Kompos Bokhasi (Rp21.000,-)\n \n> dari sisa bahan organik: tumbuhan, hewan, dan limbah organik secara alami dengan cara dekomposisi atau fermentasi \n> memberikan nutrisi pada tanaman. \n> meningkatkan Kapasitas Tukar Kation (KTK) \n> mampu meningkatkan pH tanah pada tanah asam. \n> meningkatkan ketersediaan unsur mikro.")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(pupuk3[0])
            hargabarang.append(pupuk3[1])
        else:
            pupuk()
    elif new_4 == 4 :
        print(" Pupuk Hayati Organik Micorin (Rp27.000,-)\n \n> pupuk mikrobiologis (biofertilizer) \n> membantu memperbaiki struktur tanah \n> memproduksi nutrisi bagi tanah dan tanaman \n> memangkas pertumbuhan parasit bagi tanaman")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(pupuk4[0])
            hargabarang.append(pupuk4[1])
        else:
            pupuk()
    elif new_4 == 5 :
        print("Pupuk Humic Acid Humus (Rp68.000,-)\n \n> dari pelapukan daun-daunan dan ranting tanaman yang membusuk \n> membantu meningkatkan kadar air tanah \n> mencegah erosi \n> mempercepat proses penghancuran senyawa beracun dalam tanah")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(pupuk5[0])
            hargabarang.append(pupuk5[1])
        else:
            pupuk()
    elif new_4 == 6 :
        belanjatani()
    else :
         print(str (input (' \nTekan enter untuk memasukkan angka yang benar' )))
         pupuk()


def bibit():
    clean()
    print ('Beberapa Produk teratas dari kami :')
    print (' 1. Padi\n 2. Jagung\n 3. Kembang kol\n 4. Sawi\n 5. Terong\n 6. Kembali')
    bibit1 = ['Padi', 34000]
    bibit2 = ['Jagung', 47000]
    bibit3 = ['Kembang kol', 49000]
    bibit4 = ['Sawi', 98000]
    bibit5 = ['Terong', 51000]
    new_5 = int(input('\nMasukkan barang yang ingin dibeli:'))
    if new_5 == 1 :
        print(" Padi (Rp34.000,-) \nTanah yang cocok: mengandung lempung, pasir, dan debu.")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(bibit1[0])
            hargabarang.append(bibit1[1])
        else:
            bibit()
    elif new_5 == 2 :
        print("Jagung (Rp47.000,-) \nTanah yang cocok: andosol (berasal dari gunung berapi), latosol, grumosol, tanah berpasir.")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(bibit2[0])
            hargabarang.append(bibit2[1])
        else:
            bibit()
    elif new_5 == 3:
        print(" Kembang kol (Rp49.000,- \n Tanah yang cocok: kaya nutrisi dan berdrainase baik.")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(bibit3[0])
            hargabarang.append(bibit3[1])
        else:
            bibit()
    elif new_5 == 4 :
        print(" Sawi (Rp98.000,-) \nTanah yang cocok: memiliki bahan dasar berupa endapan debu atau liat.")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(bibit4[0])
            hargabarang.append(bibit4[1])
        else:
            bibit()
    elif new_5 == 5 :
        print(" Terong (Rp51.000,-) \nTanah yang cocok: berlempung pasir dengan kisaran pH 6,5-7.")
        print ( '-' * 50 )  
        print('Masukkan keranjang? \n 1. Ya \n 2. Batal')
        beli = int(input('\nMasukkan (1/2): '))
        if beli == 1:
            barangbelanja.append(bibit5[0])
            hargabarang.append(bibit5[1])
        else:
            bibit()
    elif new_5 == 6 :
        belanjatani()
    else :
        print(str (input (' \nTekan enter untuk memasukkan angka yang benar' )))
        bibit()

def checkout() :
    clean()
    baca_laporan()
    print('List barang yang akan anda beli: \n')
    ket = ['No', 'Nama', 'Harga']
    print(f'{ket[0]:<5}{ket[1]:<38}{ket[2]:<18}')
    print('='*60)
    totalharga = sum(hargabarang)
    for j in range(len(barangbelanja)):
            print(f'{j+1:<5}{barangbelanja[j]:<38}','Rp'+ f'{hargabarang[j]:<18}')
    print('='*60)
    total = sum(hargabarang)
    print('Total Harga :' + ' Rp' + str(total))
    print('='*60)
    clean()
    print('Apakah Anda Yakin ? \n 1. Ya\n 2. Tidak, Kembali ke Menu Awal \n')
    user = int(input('Inputkan angka yang anda inginkan :'))
    if user == 1 :
        total = sum(hargabarang)
        total = int(total)
        print("Total Belanja Anda Sementara : Rp" + str(totalharga))
        ket = ['No', 'Nama', 'Harga']
        print(f'{ket[0]:<5}{ket[1]:<38}{ket[2]:<18}')
        print('='*60)
        totalharga = sum(hargabarang)
        for j in range(len(barangbelanja)):
            print(f'{j+1:<5}{barangbelanja[j]:<38}','Rp'+ f'{hargabarang[j]:<18}')
        print('='*60)
        total = sum(hargabarang)
        totalharga = totalharga 
        print('Total Harga Belanja :' + ' Rp' + str(total))
        print("Total Akhir :" + ' Rp' + str(totalharga))
        print('='*60)
        Program = {'barang' : barangbelanja}
        program1 = {'harga' : hargabarang}
        program4 = {'total' : totalharga}
        
        
        hitungan = baca_laporan()
        hitungan.append(Program)
        hitungan.append(program1)
        hitungan.append(program4)
        tulis_ulangJson(hitungan)
    else :
        belanjatani()
    
        

print ( 'Selamat Datang di Tanipedia' ) 
print ( '-' * 50 )  
nama =  input ( "Silakan Masukkan Nama Anda:" ) 
print ( '-' * 50 )
print ( 'Selamat Datang' ,  nama ) 
print ( 'Silahkan Pilih Menu' ) 
while True :
    print("Menu:\n 1. Belanja Tani \n 2. Laporan Pembelian")
    pilihan = int(input('Masukkan kode 1-2 untuk memilih menu yang diinginkan:'))
    print('-'*50)
    if pilihan == 1 :
        belanjatani()
        break
    elif pilihan == 2 :
        laporan()
        os.remove("hasilbelanja.json")
        break
    else :
        print ('Masukkan inputan sesuai nomer yang tersedia')