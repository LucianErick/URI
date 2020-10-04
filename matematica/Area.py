a, b, c = input().split(" ")

a = float (a)
b = float (b)
c = float (c)

pi=float (3.14159)
aTriangulo=(a*c)/2
aCirculo=pi*(c*c)
aTrapezio=((a+b)*c)/2
aQuadrado=b*b
aRetangulo=a*b


print("TRIANGULO: ""%.3f"%(aTriangulo))
print("CIRCULO: ""%.3f"%(aCirculo))
print("TRAPEZIO: ""%.3f"%(aTrapezio))
print("QUADRADO: ""%.3f"%(aQuadrado))
print("RETANGULO: ""%.3f"%(aRetangulo))
