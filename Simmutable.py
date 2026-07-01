#strings are immutable

a = "!!Mannu!! !!!!!!!!!! Mannu"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace ("Mannu" , "Manisha"))
print(a.split(" "))


str1 = "welcome to the vs code"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Mannu"))

str1 = "welcome to the vs code !!!"
print(str1.endswith("!!!"))

str1 = "welcome to the vs code !!!"
print(str1.endswith("to" , 4 , 10))

str1 = "welcome to the vs code"
print(str1.isalpha())
str1 = "welcome"
print(str1.isalpha())

str1 = "welcome to the vs code"
print(str1.islower())

