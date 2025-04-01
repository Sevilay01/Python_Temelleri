list = [1, 'iki', 3]
tuple = (1, 'iki', 3, 1)

print(list)
print(tuple)


# print(type(list))
# print(type(tuple))

# print(list[0])
# print(tuple[0])

# print(len(tuple))
# print(len(list))

# list[0]='bir'
# tuple[0]='bir' # tuple değiştirilemez

print(tuple.count(1))
print(tuple.index(1)) # verilen elemanın indexini verir

list+=tuple # listeye tuple ekler

print(list)

# tuple+=list # tupleye liste eklenmez

# print(tuple)

tuple+=tuple #tuple,tuple ile concatenate edilebilir
print(tuple) 



