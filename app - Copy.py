#heading
batas_bintang= "***********************************"
batas_garis = "-----------------------------------"
print(batas_bintang)
print("SELAMAT DATANG DI TOKO GAME OLINE")
print(batas_bintang)
print(end="")

#list game
daftar_game = {
     1:"Warlord",
     2:"Osu",
     3:"Subway",
     4:"Pou",
     5:"Hotwheel",
}

#list harga
daftar_harga = {
     1:108999,
     2:500000,
     3:234990,
     4:123009,
     5:120999,
}
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

#menampilkan
print("--------------List Game--------------")
for i in daftar_game:
     print("No :",i,"\t","\t",end="")
     print("Nama Game :",daftar_game[i],"\t",end="")
     print("Harga Game :", daftar_harga[i],)
pilih_nomor = int(input("Pilih Nomor Game yang akan dibeli:"))
if pilih_nomor in daftar_game:
     pilih_beli = int(input("ingin membeli (Y/N):"))
     if pilih_beli == "Y" or pilih_beli == "y":
          nama_pembeli   = "Nama Pembeli : "
          telepon        = "No HP        : "
          email_p        = "Email        : "
          list_transaksi = {
               "Nama Pembeli": nama_pembeli,
               "No HP"       : telepon,
               "Email"       : email_p,
          }
     else:
          pass
     if len (list_transaksi)> 0:
          print ("metode transaksi")

