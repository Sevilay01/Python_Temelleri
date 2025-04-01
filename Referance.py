
#value type => string ,number
x=5
y=25
x=y
y=10
# print(x,y) 


#reference types => list
#adres bilgisi taşınır.
a=["apple",'banana']
b=["apple",'banana']

print("Before copy")
print(id(a)) #adres yazdırır
print(id(b))

a=b # adresler aynı oluyor. listeA=listeB
print("After copy")
print(id(a))
print(id(b))
b[0]="grape"
print(a,b)