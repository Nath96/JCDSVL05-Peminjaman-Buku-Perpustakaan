from datetime import datetime

listData = [
    {
        'Kode' : 'A01',
        'Nama' : 'Andika',
        'JudulBuku' : 'Finance',
        'TglPinjam' : '24/02/22',
        'TglKembali' : '30/02/22'
    },
    {
        'Kode' : 'A02',
        'Nama' : 'Budiarto',
        'JudulBuku' : 'Cooking',
        'TglPinjam' : '20/02/22',
        'TglKembali' : '24/02/22'
    },
    {
        'Kode' : 'A03',
        'Nama' : 'Carmen',
        'JudulBuku' : 'Otomotif',
        'TglPinjam' : '10/01/22',
        'TglKembali' : '14/01/22'
    }         
]

def showMenu() :
    print('Index \t| Kode\t| Nama\t\t| Judul Buku\t| Tanggal Pinjam | Tanggal Kembali')
    for i in range(len(listData)) :
        print(' {} \t| {}\t| {} \t| {} \t| {}\t | {}'.format(i,listData[i]['Kode'],listData[i]['Nama'] 
        ,listData[i]['JudulBuku'],listData[i]['TglPinjam'],listData[i]['TglKembali']))
    
def mainMenu() :
    print('\n\t============ Main Menu ============')

def createMenu() :
    while True :
        print('''\t1. Daftar Pinjaman
        2. Menambahkan Data Peminjaman
        3. Mengubah Data Peminjaman
        4. Menghapus Data Peminjaman
        5. Exit 
        ''')

        pilihanMenu = input('\n\tSilahkan Pilih Menu [1-5]:')

        if(pilihanMenu == '1') :
            menu1 = input('''
            ============== Menu 1 ==============
            1. Data Peminjaman Buku Perpustakaan
            2. Cari Data Peminjam
            3. Kembali ke Menu Utama
            Silahkan Pilih Menu [1-3]: ''')

            if (menu1 == '1') : 
                print('\nDaftar Pinjaman\n')
                showMenu()
            elif (menu1 == '2') : 
                print('\nCari Data Pinjaman\n')
                KodeB = input('Masukan kode : ')
                for i in range(len(listData)):
                    if(KodeB == listData[i]['Kode']):
                        print('Index \t| Kode\t| Nama \t| Judul Buku | Tanggal Pinjam  | Tanggal Kembali')
                        print(' {} \t| {}\t| {} \t| {}    | {}\t| {}'.format(i,listData[i]['Kode'],listData[i]['Nama'] 
                        ,listData[i]['JudulBuku'],listData[i]['TglPinjam'],listData[i]['TglKembali']))
                        
            elif (menu1 == '3') : 
                mainMenu()
                
        elif(pilihanMenu == '2') :
            x=0
            i=0
            while (x==i):
                KodeB = input('Kode : ')
                z = 0
                for i in range(len(listData)):
                    if(KodeB == listData[i]['Kode']):
                        z+=1
                        if(z>0) :
                            print('Data Kembar, Input no lain')
                    else :
                        x = x+1
                            
            Kode = KodeB
            Nama = input('Nama : ')
            JudulBuku = input('Judul Buku : ')

            i = 1
            while i==1:
                TglPinjam = input('Tanggal Pinjam (DD/MM/YY) : ')
                try:
                    PinjamObj = datetime.strptime(TglPinjam, '%d/%m/%y').date()
                except ValueError:
                    print('Format Tanggal Salah!')
                else:
                    i+=1
                
            while i==2:
                TglKembali = input('Tanggal Kembali (DD/MM/YY) : ')
                try:
                    KembaliObj = datetime.strptime(TglKembali, '%d/%m/%y').date()
                except ValueError:
                    print('Format Tangal Salah!')
                else:
                    i+=1
                
            c = KembaliObj > PinjamObj
                
            while (c == False) :
                print("Tanggal Kembali harus lebih dari Tanggal Pinjam")
                TglKembali = input('Tanggal Kembali (DD/MM/YY) : ')
                try:
                    KembaliObj = datetime.strptime(TglKembali, '%d/%m/%y').date()
                except ValueError:
                    print('Format Tanggal Salah!')
                else:
                    i+=1

                c = KembaliObj > PinjamObj
                    
            else :
                print("Input Data Berhasil")
                    
            listData.append({
                'Kode' : Kode,
                'Nama' : Nama,
                'JudulBuku' : JudulBuku,
                'TglPinjam' : TglPinjam,
                'TglKembali' : TglKembali
            })

            print('\nMenambahkan Data Peminjam\n')
            showMenu()

        elif(pilihanMenu == '3') :
            menu3 = input('''
            ============== Menu 3 ==============
            1. Mengubah Data Peminjam
            2. Kembali ke Menu Utama
            Silahkan Pilih Menu [1-2]: ''')
        
            if (menu3 == '1') : 
                showMenu()
                print('\nMengubah Data Peminjam\n')
                x=0
                i=0
                a=0
                while (x==i):
                    KodeB = input('Masukan Kode yang ingin diubah : \n')
                    for i in range(len(listData)):
                        if(KodeB == listData[i]['Kode']):
                            x+=1
                            a=i

                JudulBuku = input('Ganti Judul Buku : ')
                listData[a]['JudulBuku']= JudulBuku
                showMenu()
            elif (menu3 == '2') : 
                mainMenu()
                
        elif(pilihanMenu == '4') :
            menu4 = input('''
            ============== Menu 4 ==============
            1. Menghapus Data Peminjam
            2. Kembali ke Menu Utama
            Silahkan Pilih Menu [1-2]: ''')
            
            if (menu4 == '1') : 
                print('\nMenghapus Data Peminjam\n' )
                showMenu()

                x=0
                i=0
                a=0
                while (x==i):
                    KodeB = input('Masukan Kode yang ingin dihapus : \n')
                    for i in range(len(listData)):
                        if(KodeB == listData[i]['Kode']):
                            x+=1
                            a=i
                del listData[a]

                showMenu()

            elif (menu4 == '2') : 
                mainMenu()

        elif(pilihanMenu == '5') :
            break
        else :
            print("\nPilihan menu tidak ada\n")   

createMenu()