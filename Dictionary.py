#  key - value çifti

# dictionary olmadan 

# sehirler=['kocaeli','istanbul']
# plakalar=[41,34]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])


#  dictionary ile
# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

# plakalar={'kocaeli':41 , 'istanbul':34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalara ekleme yapar
# plakalar['ankara']=6
# print(plakalar)

# varolan eleman güncellenir
# plakalar['kocaeli']='new value'
# print(plakalar)

# dictionary olusturma
users={
    'sevilay':5,
    'dell' : 10
}
print(users['sevilay'])
print(users['dell'])
# dictionary icinde dictionary

users={
    'sevilay':{
        'age':20,
        'roles':['admin','user'],
        'mail':'sevilaycelik829@gmail.com',
        'phone':'1234567890'
    },
    'dell' : {
        'firm':'dell',
        'roles':['user'],
        'model':'xps',
        'color':'black',
        
    }
}
print(users['sevilay'])
print(users['sevilay']['mail'])
print(users['dell']['color'])
print(users['dell']['roles'])
print(users['sevilay']['roles'][0])