barangbelanja = []
hargabarang = []
totalharga = 0



def pupuk () :  
        print  ( 'Beberapa Produk teratas dari kami :' ) 
        print  ( ' 1. Pupuk SP-36 ($98)\n 2. Pupuk Urea ($120)\n 3.  Pupuk KCL ($113)\n 4. Pupuk Hayati ($38)' ) 
        barang1 =  [ 'Pupuk SP-36' , 98 ]  
        barang2 =  [ 'Pupuk Urea' , 120 ]  
        barang3 =  [ 'Pupuk KCL' , 113 ]  
        barang4 =  [ 'Pupuk Hayati' , 38 ]  
        new_2 =  int (input ( '\nMasukkan barang yang ingin dibeli:' ))
        if new_2 == 1 :
            barangbelanja.append(barang1[0])
            hargabarang.append(barang1[1])
        elif new_2 == 2 :
            barangbelanja.append(barang2[0])
            hargabarang.append(barang2[1])
        elif new_2 == 3 :
            barangbelanja.append(barang3[0])
            hargabarang.append(barang3[1])
        elif new_2 == 4 :
            barangbelanja.append(barang4[0])
            hargabarang.append(barang4[1])           
        else :
            print("\nMasukkan Angka yang benar")


def bibit () :  
        print  ( 'Beberapa Produk teratas dari kami :' ) 
        print  ( ' 1. Padi ($98)\n 2. Jagung ($120)\n 3.  Kembang kol ($113)\n 4. Sawi ($38)' ) 
        barang1 =  [ 'Padi' , 98 ]  
        barang2 =  [ 'Jagung' , 120 ]  
        barang3 =  [ 'Kembang kol' , 113 ]  
        barang4 =  [ 'Sawi' , 38 ]  
        new_2 =  int (input ( '\nMasukkan barang yang ingin dibeli:' ))
        if new_2 == 1 :
            barangbelanja.append(barang1[0])
            hargabarang.append(barang1[1])
        elif new_2 == 2 :
            barangbelanja.append(barang2[0])
            hargabarang.append(barang2[1])
        elif new_2 == 3 :
            barangbelanja.append(barang3[0])
            hargabarang.append(barang3[1])
        elif new_2 == 4 :
            barangbelanja.append(barang4[0])
            hargabarang.append(barang4[1])           
        else :
            print("\nMasukkan Angka yang benar")


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
        pupuk()
        break
    elif pilihan == 2 :
        bibit()
        break
    else :
        print ('Masukkan inputan sesuai nomer yang tersedia')