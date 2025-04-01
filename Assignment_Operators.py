# x=5
# y=10
# z=20

x,y,z=5,10,20
# print(x,y,z)

# #assignment operator
# x,y=y,x
# print(x,y,z)

# #assignment operator
# x+=5 # x=x+5
# print(x,y,z)
# x-=5 # x=x-5
# print(x,y,z)
# x*=5 # x=x*5
# print(x,y,z)
# x/=5 # x=x/5 floata çevirme yapar,ondalıklı böler
# print(x,y,z)
# x%=5 # x=x%5  0 kalan verir
# print(x,y,z)
# x=2 # yeniden atama 
# x**=5 # x=x**5 üs alır
# print(x,y,z)
# x//=5 # x=x//5  tam böler
# print(x,y,z)

# y**=z # y=y**z
# print(x,y,z)

x,y,z=5,10,20
values=1,2,3
x,y,z=values
print(values)
print(type(values))
print(x,y,z)

value=4,6,8,97,45,6

x,y,*z=value # z listeye atar x=4,y=6 z=[8,97,45,6]
print(x,y,z)
print(x,y,z[0])