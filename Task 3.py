import texttable as tt
import getpass

def menu():
    print("==================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")

    pilih = input("\n\tsilahkan pilih :")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/t)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tsalah input...........!!!")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        nama.append(input("Masukkan Nama: "))
        nim.append(input("Masukkan Nim: "))
        tugas = int(input("Nilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("Nilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("Nilai UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("Tambah data [y/n]?  ")


    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas', 'Nilai UTS', 'Nilai UAS','Nilai Akhir'])
    print (tab.draw())

def pembayaran():
    print("\n==============================")
    nama = input("\tmasukan nama = ")
    nim = input("\tmasukkan NIM = ")
    semester = input("\tmasukkan semester saat ini = ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran SPP")
    print("\t2. pembayaran UTS")
    print("\t3. pembayaran UAS")
    print("\t4. pembayaran SPP & UTS")
    print("\t5. pembayaran SPP & UAS")
    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        SPP()
    elif pilih == "2":
        UTS()
    elif pilih == "3":
        UAS()
    elif pilih == "4":
        SPP_UTS()
    elif pilih == "5":
        SPP_UAS()
    else:
        exit
        tanya()

def SPP():
    bulan=int(input("\n\tjumlah bulan yang dibayar ="))
    bulan = float (bulan)
    total = 500000 * bulan
    print("=========================================")
    print("\ttotal bayar SPP Rp. 500000 *" ,bulan," = Rp.",total)

def UAS():
    matkul =int(input("\n\tjumlah mata kuliah = "))
    matkul =float(matkul)
    byr_UAS = 50000*matkul
    print("=========================================")
    print("\ttotal bayar UAS Rp. 50000 *" ,matkul, " = Rp.",byr_UAS)

def UTS():
    matkul_UTS =int(input("\n\tjumlah mata kuliah = "))
    matkul_UTS =float(matkul_UTS)
    byr_UTS = 250000*matkul_UTS
    print("=========================================")
    print("\ttotal bayar UTS Rp. 250000 *",matkul_UTS," = Rp.",byr_UTS)

def SPP_UAS():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\tjumlah mata kuliah ="))
    matkul =float(matkul)
    bulan =float(bulan)
    total_SPP = 350000 * bulan
    byr_UAS = 50000*matkul
    total = total_SPP + byr_UAS  + 5000
    print("\n\ttotal_bayar SPP Rp. 350000 = ",bulan," = Rp.",total_SPP)
    print("\ttotal bayar UAS Rp. 250000 = ",matkul," = Rp.",byr_UAS)
    print("\tbiaya tambahan server sebesar Rp. 5000")
    print("========================================")
    print("\ttotal yang harus di bayar Rp. ",total)

def SPP_UTS():
    bulan=int(input("\n\tjumlah bulan yang di bayar ="))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan =float(bulan)
    total_SPP =350000 * bulan
    byr_UTS = 250000*matkul
    total = total_SPP + byr_UTS + 5000
    print("\n\ttotal bayar UAS Rp. 500000 = ",matkul," = Rp.",byr_UTS)
    print("\ttotal bayar SPP Rp. 350000 = ",bulan," = Rp.",total_SPP)
    print("\tbiaya tambahan server sebesar Rp. 5000")
    print("========================================")
    print("\ttotal yang harus di bayar" ,total)

username = input("\tusername : ")
password = getpass.getpass()
print("============================================")
if username == "hasansajili" and password == "Soekarno04":
    menu()

else:
    print ("WEW, password/username yang Anda masukkan salah..........!!!")
