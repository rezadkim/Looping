jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = raw_input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break

print "Total perulagan: " + str(hitung)
