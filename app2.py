#menampilkan data

#lihat data
def lihat():
    print("-----------------------[[List Game]]-----------------------")
    f = open("data.txt", "r")
    Lines = f.readlines()
    count = 0
    for item in Lines:
        count += 1
        data = item.strip().split(",")
        nomer = data[0]
        game = data[1]
        harga = data[2]
        print(nomer + "). Name : " + game + "\t" + " Harga : " + harga)
        print("--------------------------------------------")
    f.close()
    
    #def eror():
    #    f = open("data.txt","r")
    #    for i in f:
    #        hasil_split = i.split(",")
    #        no = hasil_split[0]
    #        nama_produk = hasil_split[1]
    #        harga = hasil_split[2]
    #        print(no +"."+"|","\t","Nama produk :", nama_produk,"\t","Harga :", harga)
    #    f.close()

#lihat data (code error)
#def error():
#    f = open("data.txt","r")
#    split = f.read()
#    hasil_split = split.split(",")
#    no = hasil_split[0]
#    nama_produk = hasil_split[1]
#    harga = hasil_split[2]
#    f.close()
#    print(no,".","\t","Nama produk :", nama_produk,"\t","Harga :", harga)

#menambah data
def tambah():
    f = open("data.txt","a")
    data = str(input("Input data dengan format (no,nama,harga game) :"))
    f.write(data)
    f.write("\n")
    f.close()
    print("Data telah ditambahkan")

#edit data
#def edit1():
#    lihat()
#    with open('data.txt', 'r+') as foo:
#        data = foo.readlines()                  #reads file as list
#        pos = int(input("Which position in list to edit? "))-1  #list position to edit
#        data_edit = input("Masukkan data :")
#        data.insert(pos, data_edit+"\n")           #inserts before item to edit
#        x = data[pos+1]
#        data.remove(x)                      #removes item to edit
#        foo.seek(0)                     #seeks beginning of file
#        for i in data:
#            i.strip()                   #strips "\n" from list items
#            foo.write(str(i))

def edit():
    lihat()
    edit_data = int(input("Masukkan no data yang akan diedit : ")) #no data dimulai dari 0
    data_edit = input("Input data dengan format (no,nama,harga game) :")
    f = open("data.txt", "r")
    data = f.readlines()
    data[edit_data - 1] = data_edit + "\n"

    f = open("data.txt", "w")
    f.writelines(data)
    f.close()
    print("Data telah diedit")

#hapus data   
def hapus():
    lihat()
    data = ""
    delete_data = int(input("Masukkan no data yang akan dihapus: ")) #no data dimulai dari 0
    with open('data.txt', 'r') as file:
        data = file.readlines()
    
    data[delete_data - 1] = '' # sesuain sama baris yang mau dihapus
    with open('data.txt', 'w') as file:
        file.writelines( data )
    print("Data telah dihapus")

#Searching
def searching():
    f = open('data.txt','r')
    Lines = f.read()
    cari_data = input('Masukkan data yang dicari:\n(NB :Data yang dicari berupa nama game dengan huruf kapital):') 
    if cari_data in Lines:
        print(cari_data, 'Found In File:', )        
        lihat()                                        
    else: 
        print(cari_data , 'Not Found') 

#shorting
def sort():
    inp = int(input('Masukkan nomor :'))
    with open("data.txt", "r") as file:
        Lines = file.readlines()

    my_data = {}
    for item in Lines:
        split = item.strip().split(",")
        useful_data = [item.strip() for item in split[1:] if item != ""]
        my_data.update({split[inp]: useful_data})

    for key in sorted(my_data.keys()):
        print(my_data[key])
    menu()

def menu_sort():
    print("Sorting Berdasarkan :")
    print("1). Nama")
    print("2). Harga")
    sort()

#fungsi menu
def menu():
    print("")
    print("-------------------")
    print("      ||MENU||")
    print("-------------------")
    print("1). Lihat Data")
    print("2). Edit Data")
    print("3). Tambah Data")
    print("4). Hapus Data")
    print("5). Cari Data")
    print("6). Urutkan Data ")
    print("7). Keluar Program")
    print("-------------------")
    kode = input("Masukkan kode :")
    if kode == "1":
        lihat()
        menu()
    elif kode == "2":
        edit()
        menu()
    elif kode == "3":
        tambah()
        menu()
    elif kode == "4":
        hapus()
        menu()
    elif kode == "5":
        searching()
    elif kode == "6":
        menu_sort()
        pass
    elif kode == "7":
        print("Anda sudah keluar dari program")
        pass
    else:
        print("Kode salah")
        menu()

#cara pembayaran
list_transaksi = {}
menu_pembayaran = {
     1:"Kartu Kredit",
     2:"VISA",
     3:"E-Wallet",
     4:"Transfer Bank",
     5:"Virtual Account",
     6:"Pulsa"
}

#konfirmasi 
def confirm():
    confirm = input("Yakin ingin membeli? (Y/N):")
    if confirm == "Y" or confirm == "y" or confirm == "yes" or confirm == "Yes":
        
        print("")
        print("-------------STRUCK PEMBELIAN-------------")
        struck()
        print("------------------------------------------")
        print("")
        print("PEMBAYARAN SUKSES")
        print("TRANSAKSI BERHASIL TERMAKASIH")
        print("------------------------------------------")

    elif confirm == "N" or confirm == "n" or confirm == "no" or confirm == "No":
        print("")
        print("TRANSAKSI DIBATALKAN")
    else:
        print("")
        print("TRANSAKSI DIBATALKAN")

#Struck
def struck():
    print("Nama User         :", list_transaksi["Nama User"])
    print("No HP             :", list_transaksi["No HP"])
    print("Email             :", list_transaksi["Email"])
    print("Metode Pembayaran :", menu_pembayaran[pilih_menu_pembayaran])
    print("Nama Game         :", game)
    print("Harga Game        :", harga)

#PROGRAM CUSTOMER
print("~~~~~~[SELAMAT DATANG DI TOKO GAME ONLINE]~~~~~~")
login = {
    1:"Admin",
    2:"Customer"
}
for i in login:
    print(i, login[i])
pilih_login = int(input('pilih nomor :'))
if pilih_login == 1:
    menu()
elif pilih_login == 2:
    print("")
    lihat()
    pilih_game = int(input("Pilih Nomor Game yang akan dibeli:"))
    f = open("data.txt", "r")
    Lines = f.readlines()
    d = Lines[pilih_game - 1]
    f.close()
    for item in d:
        data = d.strip().split(",")
        nomer = data[0]
        game = data[1]
        harga = data[2]
        break

    if pilih_game >= 0:
        pilih_beli = input("ingin membeli (Y/N):")
        if pilih_beli == 'Y' or pilih_beli == 'y':
            nama_pembeli   = input("Nama User    : ")
            telepon        = input("No HP        : ")
            email_p        = input("Email        : ")
            list_transaksi = {
                "Nama User"   : nama_pembeli,
                "No HP"       : telepon,
                "Email"       : email_p,
            }
            if len (list_transaksi)> 0:
                print("")
                print("-----------[[Metode Pembayaran]]-----------")
                for i in menu_pembayaran:
                    print("No :",i,"\t", menu_pembayaran[i])
                    print("-------------------------------")
            pilih_menu_pembayaran = int(input('Pilih nomor metode pembayaran:'))
            if pilih_menu_pembayaran in menu_pembayaran:
                print("")
                print("-------------[DATA CUSTOMER]-------------")
                struck()
                print("")
                print("Pilih Yes untuk Membeli, pilih No untuk membatalkan")
                confirm()
        else:
            print("Transaksi Dibatalkan")
            print("Silahkan Melakukan Ulang Pesanan")
    else:
        pass
else:
    print("KODE SALAH")