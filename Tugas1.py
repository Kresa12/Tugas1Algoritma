listSupirdanTujuan = {'Paijo' : 'Semarang', 'Slamet' : 'Pekalongan', 'Rahmat' : 'Tegal', 'Adi' : 'Kebumen'}

namaSupir = str(input('Nama Supir : '))
jumlahPenumpang = int(input('Jumlah Penumpang : '))
tujuan = str(input('Tujuan : '))
kondisiBus = str(input('Kondisi Bus : '))
hargaTiket = 100_000 * jumlahPenumpang

if namaSupir in listSupirdanTujuan and jumlahPenumpang >= 20 and tujuan in listSupirdanTujuan.values() and kondisiBus == 'Baik':
     print({'Nama Supir' : namaSupir, 'Status Supir' : 'Terdaftar', 'Jumlah Penumpang' : jumlahPenumpang, 'Tujuan' : tujuan,'Total Uang Tiket' : hargaTiket},
           '\n BUS DIIZINKAN BERANGKAT! SILAHKAN CETAK SURAT JALAN DAN UANG JALAN DI POOL!')
elif namaSupir in listSupirdanTujuan or jumlahPenumpang >= 20 or tujuan in listSupirdanTujuan.values() or kondisiBus == 'Baik':
     print('PERJALAN DITUNDA KARENA ADA SOP YANG BELUM TERPENUHI')
else:
     print('BUS TIDAK DIIZINKAN JALAN KARENA SOP TIDAK TERPENUHI')