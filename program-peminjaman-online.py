print("\n-----------  WELCOME IN MY PROGRAM  ----------")
print("=" * 46)
print("|          MUHAMMAD IQBAL FIRMANSYAH         |")
print("|                210441100084                |")
print("|          PROJECT PEMINJAMAN ONLINE         |")
print("=" * 46)
print("")

def warning():
    print("")
    print("=" * 46)
    print("|        MASUKKAN INPUTAN YANG BENAR         |")
    print("=" * 46) 

def checkout():
    print('PINJAMAN ANDA SEBESAR = Rp. ',uangpinjam[1])
    print('TAGIHAN ANDA SEBESAR  = Rp. ',hasil)
    print("=" * 46)
    print("|" + nama[1].center(44) + "|")
    print("|" + str(nik[1]).center(44) + "|")
    print("|" + alamat[1].center(44) + "|")
    print("-" * 46)
    print("|       PEMBAYARAN MAX SELAMA 30 HARI        |")
    print("|          JIKA LEBIH DARI 30 HARI           |")
    print("|      ANDA AKAN MENDAPAT DENDA SEBESAR      |")
    print("|              Rp. 200.000,00                |")
    print("=" * 46)

def datadiri():
    print("=" * 46)
    print("|               DATA DIRI ANDA               |")
    print("|" + nama[1].center(44) + "|")
    print("|" + str(nik[1]).center(44) + "|")
    print("|" + alamat[1].center(44) + "|")
    print("=" * 46)
    print("")

def data():
    nama.insert(1,daftar['nama'])
    nik.insert(1,daftar['NIK'])
    alamat.insert(1,daftar['Alamat'])

nama = ['-']
nik = ['-']
alamat = ['-']
uangpinjam = ['-']

PilihLain = 'Y'
while PilihLain.capitalize() == 'Y' :
    while True:
        print("=" * 46)
        print("|          MENU AKSES SHOPEPAY LATER         |")
        print("|               (1) TRANSAKSI                |")
        print("|             (2) KELUAR PROGRAM             |")
        print("=" * 46)
        pilih = int(input('\nMasukkan pilihan : '))
        if pilih == 1 :
            print("")
            print("=" * 46)
            print("|        SILAHKAN MASUKKAN DATA ANDA         |")
            print("=" * 46)
            daftar = {
                'nama' : str(input('\nMasukkan Nama \t: ')) ,
                'NIK' : int(input('Masukkan NIK \t: ')), 
                'Alamat' : str(input('Masukkan Alamat : ')),}  

            while True:
                rubah = str(input('\nApakah ingin merubah data tersebut (Y/N) ?: '))
                if rubah.capitalize() == 'Y':
                    daftar['nama'] = str(input('\nMasukkan Nama \t: '))
                    daftar['NIK'] = int(input('Masukkan NIK \t: '))
                    daftar['Alamat'] = str(input('Masukkan Alamat : '))
                    data()
                elif rubah.capitalize() == 'N':
                    data()
                    break
                else :
                    warning()
                    data()
                    
            
            menu = 'Y'
            while menu.capitalize() == 'Y':
                while True :
                    print("")
                    print("=" * 46)
                    print("|        MENU TRANSAKSI SHOPEPAYLATER        |")
                    print("-" * 46)
                    print("|           (1) MELAKUKAN PINJAMAN           |")
                    print("|          (2) MELAKUKAN PEMBAYARAN          |")
                    print("|             (3) MENGHAPUS DATA             |")
                    print("|              (4) BACK TO HOME              |")
                    print("=" * 46)

                    pilih = int(input('\nMasukkan pilihan : '))
                    if pilih == 1 :
                        print("")
                        datadiri()
                        Pinjam ={'pinjam' : int(input('Masukkan nominal Peminjaman : Rp. '))}
                        if Pinjam['pinjam'] == 0 :
                            print('Anda niat meminjam atau hanya bermain-main?')
                            break
                        if Pinjam['pinjam'] > 0 :
                            uangpinjam.insert(1,Pinjam['pinjam'])
                            bunga = uangpinjam[1]*15/100
                            hasil = Pinjam['pinjam'] + bunga
                            print('Bunga = 15%')
                            print('\nNominal tagihan = Rp ',hasil)

                            rbh = str(input('\nAnda ingin mengubah nominal Peminjaman (Y/N) ? : '))
                            if rbh.capitalize() == 'Y':
                                Pinjam['pinjam'] = int(input('Masukkan nominal Peminjaman : '))
                                uangpinjam.insert(1,Pinjam['pinjam'])
                                bunga = uangpinjam[1]*15/100
                                hasil = Pinjam['pinjam'] + bunga
                                print('Bunga = 15%')
                                print('\nNominal tagihan = Rp ',hasil)
                            elif rbh.capitalize() == 'N':
                                break 
                            else:
                                warning()

                            tanya = str(input('\nApakah ingin membatalkan Peminjaman (Y/N) ? : '))
                            if tanya.capitalize() == 'Y':
                                print("")
                                print("=" * 46)
                                exit("|            PEMINJAMAN DIBATALKAN           |")
                                print("=" * 46)
                            elif tanya.capitalize() == 'N':
                                print("")
                                print("=" * 46)
                                print("|           PEMINJAMAN DISETUJUI             |")
                                print("=" * 46)
                                checkout()
                                break
                            else :
                                warning()
                        else :
                            warning()
                        

                    elif pilih == 2 :
                        datadiri()
                        print('Pinjaman \t: Rp ',uangpinjam[1])
                        print('Tagihan \t: Rp ',hasil)
                        denda = int(input('\nJarak peminjaman dengan pembayaran (hari) : '))
                        if denda > 30 :
                            hari = denda - 30
                            BayarDenda = hari * 200000
                            totalTghn = hasil + BayarDenda
                            print('Anda terlambat ', hari , 'hari')
                            print('Maka total tagihan yang harus anda bayar = Rp. ', totalTghn)
                            pay = int(input('\nMasukkan uang anda : Rp.  '))
                            if pay > totalTghn :
                                kembalian = pay - totalTghn
                                print('\n\nUang anda : Rp ', pay)
                                print('Kembalian : Rp ', kembalian)
                                struk = str(input('\nApakah anda ingin mencetak struk (Y/N) ? : '))
                                if struk.capitalize() == 'Y':
                                    print('\n******************* STRUK PEMBAYARAN *******************')
                                    datadiri()
                                    print('Jumlah tagihan = Rp ',hasil)
                                    print('Nominal Uang Customer = Rp ',pay)
                                    print('Uang kembalian = Rp ',kembalian)
                                    print('\n********************** THANK YOU ***********************')
                                break
                            if pay < totalTghn :
                                kurang = totalTghn - pay
                                print('WARNING! UANG ANDA KURANG!')
                                print('Uang anda kurang Rp ',kurang)
                                break
                            if pay == totalTghn :
                                print('Uang anda pas')
                                print('\n******************* STRUK PEMBAYARAN *******************')
                                datadiri()
                                print('\nJumlah tagihan = Rp ',hasil)
                                print('Nominal Uang Customer = Rp ',pay)
                                print('Uang kembalian = Rp ',kembalian)
                                print('\n********************** THANK YOU ***********************')
                                break
                            else :
                                print('Thank you')

                            break

                        else : 
                            print('ANDA BEBAS DARI DENDA!')
                            pay = int(input('\nMasukkan uang anda : Rp '))
                            if pay > hasil :
                                kembalian = pay - hasil
                                print('\n\nUang anda : Rp ', pay)
                                print('Kembalian : Rp ', kembalian)
                                struk = str(input('\nApakah anda ingin mencetak struk (Y/N) ? : '))
                                if struk.capitalize() == 'Y':
                                    print('\n******************* STRUK PEMBAYARAN *******************')
                                    datadiri()
                                    print('\nJumlah tagihan = Rp ',hasil)
                                    print('Nominal Uang Customer = Rp ',pay)
                                    print('Uang kembalian = Rp ',kembalian)
                                    print('\n********************** THANK YOU ***********************')
                                    break
                                else :
                                    break

                            if pay < hasil :
                                kurang = hasil - pay
                                print('WARNING! WARNING! WARNING! WARNING!')
                                print('UANG ANDA KURANG!',kurang)
                                break
                            if pay == hasil :
                                kembali = pay - hasil
                                print('UANG ANDA PAS - THANK YOU')
                                print('\n******************* STRUK PEMBAYARAN *******************')
                                print('\nJumlah tagihan = Rp ',hasil)
                                print('Nominal Uang Customer = Rp ',pay)
                                print('Uang kembalian = Rp ', kembali)
                                print('\n********************** THANK YOU ***********************')
                                break

                    elif pilih == 3 :
                        print('\nLOADING! PENGAHPUSAN DATA')
                        hapus = str(input('\nApakah anda ingin menghapus data (Y/N) ? : '))
                        if hapus.capitalize() == 'Y' :
                            nomor = int(input('\nMasukkan NIK anda : '))
                            a = nik[1]
                            if nomor == a : 
                                datadiri()
                                konfirm = str(input('Apakah anda yakin ingin menghapus data? (Y/N) : '))
                                if konfirm.capitalize() == 'Y' :
                                    del nama[1]
                                    del nik[1]
                                    del alamat[1]
                                    print("")
                                    print("=" * 46)
                                    print("|           DATA BERHASIL DIHAPUS            |")
                                    print("=" * 46) 

                                    cek = str(input('\nApakah anda ingin cek data? (Y/N) : '))
                                    if cek.capitalize() == 'Y':
                                        print('nama \t\t: ',nama)
                                        print('nik \t\t: ',nik)
                                        print('alamat \t\t: ',alamat)
                                        print("")
                                        print("=" * 46)
                                        print("|                DATA KOSONG                 |")
                                        print("|          PROGRAM BERHENTI! BYEEEE          |")
                                        print("=" * 46) 
                                    elif cek.capitalize() == 'N':
                                        break
                                    else :
                                        print('MAKASI YAAA')
                                        exit('\nPROGRAM STOP')
                                else :
                                    print('WARNING! HAPUS DATA DIBATALKAN!\n')
                                    break
                            else :
                                print("")
                                print("=" * 46)
                                print("|    NIK YANG ANDA MASUKKAN TIDAK SESUAI!    |")
                                print("=" * 46) 
                                break
                        else :
                            print('\nDATA ANDA TIDAK DI HAPUS')
                            break

                    elif pilih == 4 :
                        print("=" * 46)
                        print("|     KETIK (N) UNTUK KELUAR KE MENU HOME    |")
                        print("=" * 46)
                        break
                    else :
                        warning()

                menu = str(input('\nKembali ke Menu Transaksi (Y/N) ? : '))
                                   
        elif pilih == 2 :
            print("")
            print("=" * 46)
            print("|            PROGRAM TELAH SELESAI           |")
            print("=" * 46)
            print("")
            exit()
        else :
            warning()