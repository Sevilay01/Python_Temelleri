fruits={'orange','apple','banana'}
print(fruits)
#print(fruits[0]) # setler indexlenemez

for i in fruits:
    print(i)

#setler sıralanamaz ve pop metodu kullanılamaz çünkü rastgele eleman silinebilir.


fruits.add('cherry')
print(fruits)

#birden fazla eleman ekler
fruits.update(['mango','kiwi'])
print(fruits)

#sette elemanlar tekrarlanmaz
fruits.add('apple')
print(fruits)

#örnek

myList=[1,1,6,9,6,5,5,7]
print(myList)
print(set(myList))

#eleman siler
fruits.remove('apple') or fruits.discard('apple')
print(fruits)