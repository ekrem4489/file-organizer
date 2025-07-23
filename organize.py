import os
 

#kullanıcıdan klasor yolu al 
klasor = input(f"Lütfen bir geçerli klasör adresi giriniz: ")
dosyalar = [] #dosyalar depolanacak
uzantilar = [] #uzantıları depolayacak

#klasorun gecerli olup olmadıgını kontrol et
if os.path.isdir(klasor):
    print("Klasor geçerlidir teşekkür ederiz.")
else:
    print("Klasör geçerli değildir lütfen tekrardan deneyiniz.")

#klasordeki dosyaları listele:
for dosya in os.listdir(klasor):
    if os.path.isdir(os.path.join(klasor, dosya)):    # burda klasordeki dosyaların dosya mı klasor mu oldugunu kontrol ettik dosyaysa ekledik
        continue
    else:
        dosyalar.append(dosya)

#Uzantıları alma

for dosya in dosyalar:
    uzanti = dosya.split(".")[-1]
    if uzanti in uzantilar:
        continue
    else:
        uzantilar.append(uzanti)

# Uzantılar için klasör olusturma
for uzanti in uzantilar:
    if os.path.isdir(os.path.join(klasor,uzanti)):
        continue
    else:
        os.mkdir(os.path.join(klasor,uzanti))

# Dosyaları uzantılar için olusturdugumuz klasöre göre yerleştirme

for dosya in dosyalar:
    uzanti = dosya.split(".")[-1]
    os.rename(os.path.join(klasor,dosya), os.path.join(klasor,uzanti,dosya))
	