# list compresion in this we coded for loop inside list

square = [i * i for i in range(1,6)]
print(square)


even = [i for i in range (1,11) if i % 2 == 0]
print(even)



# Aliasing vs copy()

a = [10,20,30]
b = a
b.append(40)
print(a)
print(b)

c = a.copy()
c.append(50)
print(a)
print(c)
