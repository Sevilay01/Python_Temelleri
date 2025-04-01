name="Veli"
surname="Ali"
# String formatting with .format() method
# 1-)Using positional arguments
print("My name is {} {}".format(name, surname))

# 2-)Using indexed arguments
print("My name is {0} {1}".format(name, surname))


# 3-)Using f-strings (Python 3.6+)
print(f"My name is {name} {surname}")
# 4-)Using keyword arguments
print("My name is {first} {last}".format(first=name, last=surname))

#Example

result= 200 / 700
print('the result is {r:1.4}'.format(r=result))
#r:1.4 means 1 digit before the decimal and 4 digits after the decimal

# 5-)Using percentage formatting (old style)
print("My name is %s %s" % (name, surname))

