numeros = [10,20,(1,3),30,50,69,(10,20),40]


result1 = isinstance(numeros[0],int)
print(result1)

if result1 == False:
    numeros.pop(0)
elif result1 == True:
    pass

print (numeros)

result2 = isinstance(numeros[2],int)
print(result2)

if result2 == False:
    numeros.pop(2)
elif result1 == True:
    pass

print (numeros)
'''
for i in numeros:
    result = isinstance(numeros,int)
    print(result)

'''

