# Operadores aritméticos

# Suma, resta, multiplicación, división, módulo, potencia
a = 10
b = 3

a + b  # Suma
print(a + b)
a - b  # Resta
print(a - b)
a * b  # Multiplicación
print(a * b)
a / b  # División
print(a / b)
a % b  # Módulo
print(a % b)
a ** b  # Potencia
print(a ** b)

# Operadores de comparación
a == b  # Igualdad
print(a == b)
a != b  # Desigualdad
print(a != b)
a > b   # Mayor que
print(a > b)
a < b   # Menor que
print(a < b)
a >= b  # Mayor o igual que
print(a >= b)
a <= b  # Menor o igual que
print(a <= b)

# Operadores lógicos
x = True
y = False
print(x and y)  # AND
print(x or y)   # OR
print(not x)    # NOT

#operadores de asignación
c = 5
c += 2  # c = c + 2
print(c)
c -= 3  # c = c - 3
print(c)
c *= 4  # c = c * 4
print(c)
c /= 2  # c = c / 2
print(c)

# Operadores de identidad
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)  # True, porque list2 es la misma referencia que list1
list3 = [1, 2, 3]
print(list1 is list3)  # False, porque list3 es una nueva lista con los mismos valores, pero no es la misma referencia

# Operadores de pertenencia
print(2 in list1)  # True, porque 2 está en list1
print(4 not in list1)  # True, porque 4 no está en list


# Estructuras de control
# Condicionales
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b") 

# Bucles
# Bucle while
count = 0
while count < 5:
    print(count)
    count += 1
# Bucle for
for i in range(5):
    print(i)

 # Dificultad extra: Imprimir todos los números pares del 10 al 55, excepto el 16 y los múltiplos de 3.

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
