DATAMAHASISWA = {}

def garis():
    print(60 * '=')

def kepala():
    garis()
    garis()

def nodata():
    kepala()
    print("|{0:^70}|".format("Tidak ada data. Silahkan tambah data terlebih dahulu"))
    garis()

def tambah():
    print("TAMBAH DATA")
    nama       = input('Nama        : ')
    nim        = input('NIM         : ')
    nilaiTUGAS = input('Nilai Tugas : ')
    nilaiUTS   = input('Nilai UTS   : ')
    nilaiUAS   = input('Nilai UAS   : ')
    nilaiakhir = (nilaiTUGAS * int(30/100)) + (nilaiUTS * int(35/100)) + (nilaiUAS * int(35/100))
    DATAMAHASISWA[nama] = [nim, nilaiTUGAS, nilaiUTS, nilaiUAS, nilaiakhir]
    print(f"Berhasil menambahkan data '{nama}' ")

def lihat():
    print("Data Mahasiswa")
    if len(DATAMAHASISWA) <= 0:
        nodata()
    else:
        no = 0
        kepala()
        for data in DATAMAHASISWA.items():
            no += 1
            print(f"| {no:>2} | {data[1][0]:<7} | {data[0]:<18} | {data[1][1]:>5} | {data[1][2]:>5} | {data[1][3]:>5} | {data[1][4]:>7.2f} |")
        garis()

def ubah():
    print('Ubah Data Mahasiswa Berdasarkan Nama')
    if len (DATAMAHASISWA) <= 0:
        nodata()
    else:
        nama = input('Masukan nama: ')
        if nama in DATAMAHASISWA.keys():
            print(f"Nama        = {nama}")
            print(f"NIM         = {DATAMAHASISWA[nama][0]}")
            print(f"Nilai Tugas = {DATAMAHASISWA[nama][1]}")
            print(f"Nilai UTS   = {DATAMAHASISWA[nama][2]}")
            print(f"Nilai UAS   = {DATAMAHASISWA[nama][3]}")
            print(40 * "=")
            print("1. Nama\n2. NIM\n3. Nilai\n0. Kembali")
            a = int(input("Masukan opsi yang ingin diubah! [1-3] : "))

        elif a == 0:
            pass

        else:
            print(f"Pilihan {a} tidak ada! Silahkan masukan [1-3]")
   

    if a == 1:
        _nama = input("Masukan Nama Baru : ")
        DATAMAHASISWA[_nama] = DATAMAHASISWA.pop(nama)
        print("Berhasil Mengubah Nama ")

    elif a == 2:
        _nim = input("Masukan Nim Baru : ")
        DATAMAHASISWA[nama][0] = _nim
        print("Berhasil Mengubah NIM")

    elif a == 3:
         _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
         _nilaiUTS = int(input("Masukan Nilai UTS Baru : "))
         _nilaiUAS = int(input("Masukan Nilai UAS Baru : "))
         _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
         DATAMAHASISWA[nama][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
         print("Berhasil Mengubah data nilai!")

def hapus():
    print("Hapus Data Mahasiswa berdasarkan Nama")
    if len(DATAMAHASISWA) <= 0:
        nodata()

    else:
        nama = str(input("Masukan nama : "))
    if (nama in DATAMAHASISWA):
            del DATAMAHASISWA[nama]
            print(f"Data {nama} berhasil dihapus!")
    else:
            print(f"Data {nama} tidak ada!")

loop = True
while loop:
                print()
                print(60 * "-")
                print(18 * "-", "INPUT NILAI MAHASISWA", 18 * "-")
                print(60 * "-")
                print("1. Lihat Data \n2. Tambah Data \n3. Ubah Data \n4. Hapus Data \n0. Keluar")
                print(60 * "-")
                menu = int(input("Pilih menu : "))
                print(60 * "-")
                print()
                if menu == 1:
                    lihat()
                elif menu == 2:
                    tambah()
                elif menu == 3:
                    ubah()
                elif menu == 4:
                    hapus()
                elif menu == 0:
                    print("Program selesai, Terima Kasih")
                    loop = False
                else:
                    print(f"Menu '{menu}' tidak ada! Silahkan masukan [0-4]")




