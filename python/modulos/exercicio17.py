from math import hypot
cat = int(input("Digite o valor do primeiro cateto :"))
catA = int(input("Digite o valor do segundo cateto :"))
hipo = hypot(cat,catA)
print ("A hipotenusa do triangulo retangulo formao por {} e {} é {}".format(cat, catA, hipo))