numbers=[9,5,3,11,7,4,2,6,8,10,1]
letters=['d','a','c','b','e','f','z','n','i','j']

min_val_num=min(numbers)
print(min_val_num)
max_val_num=max(numbers)
print(max_val_num)

min_val_let=min(letters)
print(min_val_let)
max_val_let=max(letters)
print(max_val_let)

numbers.append(50) #en sona ekler
print(numbers)

numbers.insert(3,45) #istenen indexe ekler
print(numbers)

numbers.insert(-1,52) #ensona ekler
print(numbers)

numbers.pop() #en son elemanı siler
print(numbers)

numbers.pop(3) #istenen indexi siler
print(numbers)

numbers.remove(10) #istenen degeri siler
print(numbers)

numbers.sort() #listeyi sıralar
print(numbers)
numbers.reverse() #listeyi tersten sıralar
print(numbers)

print(len(numbers)) #listeyi uzunlugunu verir

print(numbers.count(2)) #istenen degerin kac tane oldugunu verir

numbers.clear() #listeyi temizler
print(numbers)



