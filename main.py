
print("Kodlamaio")

baslik = "Taşıt Kredisi"
print(baslik)
#string => Metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36
ekVade = 12
vade2 = "36"

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True veya False
yukselisteMi = False

#Matematiksel operatörler
print(5 + 5)
print(vade + 12)
print(vade + ekVade)

print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)

# *
print(5*5)
print(vade *2)
print(vade*ekVade)
print(10*10)

# /
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)

yeniVade = vade/2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatör
print(10%2)
print(vade%5)
print(vade%ekVade)
print(30%11)

#mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and
#or => veya
print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)
print(1>2 and 5>2 and 3>2)
print(2>1 or 1>2 and 3>2)

#karar yapıları
#if else
sayi1 = 10
sayi2 = 10
#sayi1 sayi2 den büyükse ekrana sayi 1 daha büyük yazdır
if sayi1 > sayi2:
    print("Sayı 1 daha büyüktür")
elif sayi1 < sayi2:
    print("Sayı 2 daha büyüktür")
#if ve elif durumları dışıdaki bütün durumlarda else kullanılır
else: 
    print("Sayılar eşittir")
