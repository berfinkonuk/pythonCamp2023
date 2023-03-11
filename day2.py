faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
# vade = int(vade)
vade = vade + 12

#string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))

#listeler 
#döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10 , 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])

print((len(krediler))) #lenght
#print(krediler[3]) => Hata verir

krediler.append("Özel Kredi") #listenin sonuna ekler
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) #verilen indexdeki elemanı siler
print(krediler)

krediler.remove("Taşıt Kredisi") #verilen değeri siler
print(krediler)
krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"]) #listedeki elemanları ekler
print(krediler)

#döngüler
# for

for i in range(10):
    print(i)
print("**************")
for i in range(5,11): #5 den 10 a kadar yazar
    print(i)
print("**************")
for i in range(0,51,10): #0 dan 50 ye kadar 10 ar 10 ar arttırarark yazar
    print(i)
print("***************")
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(krediler)
print("***************")
for i in range(len(krediler)):
    print(krediler[i])
print("***************")

#sonsuz döngü
i = 0
while i < 10:
    i = i + 1
    print("x")
print("y")

print("***************")

while True:
    print("x")
    break

print("***************")

i = 0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i+=1

#Fonksiyonlar

fiyat = 100
indirim = 20

#definition define
def calculate():
    print(100 - 20)

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50, 10)
sayHello("berfin")
sayHello("özlem")

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat)

