import os
os.system('clear')
print '\t>>>>>ARITMATIKA BY RIZKY !!<<<<<'
print
print '1. PENJUMPLAHAN'
print '2. PENGURANGAN'
print '3. PERKALIAN'
print '4. PEMBAGIAN'
print '5. SISA BAGI'
print '6. PEMANGKATAN'
print
pilih = input('PILIH MENU : ')

if pilih == 1:
	print
	angka_1 =input('ANGKA PERTAMA :')
	angka_2 =input('ANGKA KEDUA :')
	total = angka_1 + angka_2
	print 'TOTALNYA ADALAH : ', total
	
elif pilih == 2:
	print
	angka_1 =input('ANGKA PERTAMA :')
	angka_2 =input('ANGKA KEDUA :')
	total = angka_1 - angka_2
	print 'TOTALNYA ADALAH : ', total
	
elif pilih ==3:
	print
	angka_1 =input('ANGKA PERTAMA :')
	angka_2 =input('ANGKA KEDUA :')
	total = angka_1 * angka_2
	print 'TOTALNYA ADALAH : ', total
	
elif pilih ==4:
	print
	angka_1 =input('ANGKA PERTAMA :')
	angka_2 =input('ANGKA KEDUA :')
	total = angka_1 / angka_2
	print 'TOTALNYA ADALAH : ', total
	
elif pilih ==5:
	print
	angka_1 =input('ANGKA PERTAMA :')
	angka_2 =input('ANGKA KEDUA :')
	total = angka_1 % angka_2
	print 'TOTALNYA ADALAH : ', total
	
elif pilih ==6:
	print
	angka_1 =input('ANGKA PERTAMA :')
	angka_2 =input('ANGKA KEDUA :')
	total = angka_1 ** angka_2
	print 'TOTALNYA ADALAH : ', total
	
else:
	print
	print'MOHON MAAF MENU TIDAK ADA!!'
