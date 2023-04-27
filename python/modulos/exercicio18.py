from math import radians,sin, cos, tan
angulo = float(input("digite um angulo que voce deseja :"))
print ("O angulo de {} tem o seno de {:.2f}".format(angulo,sin(radians(angulo))))
print ("O angulo de {} tem o cosseno de {:.2f}".format(angulo,cos(radians(angulo))))
print ("O angulo de {} tem o tangente de {:.2f}".format(angulo,tan(radians(angulo))))
