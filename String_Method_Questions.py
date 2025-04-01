course="Ali Veli Kirk Dokuz Elli"
website="http://www.sadikturan.com"
# ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message=' Hello World '
message=message.strip() 
print(message)

message=website.lstrip('/:pth') # 'http://www.sadikturan.com' karakter dizisinin başındaki 'http://' kısmını silin.
print(message)

#  'www.sadikturan.com' içindeki sadikturan bilgisi harici tüm bilgileri silin.
message='www.sadikturan.com'
message=message.split('.')
message=message[1]
message=''.join(message)
print(message)

# 'course' karakter dizisinin tüm karakterlerinin küçük harf olmasını sağlayın.
message=course.lower()
print(message)

# 'website' içinde kaç tane a harfi olduğunu bulun.
message=website.count('a')
print(f"{website} icerisindeki a sayisi {message}")

#'website' www ile başlayıp com ile bitiyor mu kontrol edin.
message=website.startswith('www') and website.endswith('com')
print(message)

# 'website' içerisinde '.com' kelimesi geçiyor mu kontrol edin.
message=website.find('.com')
print(message)

message=website.index('.com') # 'website' içinde '.com' kelimesinin indexini bulun.
print(message)
#Farkları: index() methodu diziyi bulamadığında hata verirken find() methodu hata vermez.

# 'course' içerisindeki karakterlerin hepsi alfabetik mi kontrol edin.
message=course.isalpha()
print(message)

# 'Contents' ifadesini satırda 50 karakter olacak şekilde ortalayıp başına ve sonuna * ekleyin.

message ='Contents'.center(50,'*')
print(message)
message2='Contents'.ljust(50,'*') # 'Contents' ifadesini satırda 50 karakter olacak şekilde sola yaslayıp başına ve sonuna * ekleyin.
print(message2)
message3='Contents'.rjust(50,'*') # 'Contents' ifadesini satırda 50 karakter olacak şekilde sağa yaslayıp başına ve sonuna * ekleyin.
print(message3)
# 'course' karakter dizisindeki tüm boşlukları - karakteri ile değiştirin.
message=course.replace(" ","-")
print(message)

# 'Hello World' karakter dizisinin 'World' kısmını 'There' ile değiştirin.
message='Hello World'
message=message.replace('World','There')
print(message)

# 'course' karakter dizisini boşluk karakterlerinden ayırın.
message=course.split()
print(message)