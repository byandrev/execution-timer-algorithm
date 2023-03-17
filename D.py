a, b = map(int,input().split())

for i in range(a):
    fila = input().split()
    for elemento in fila:
        valor = int(elemento)
        tmp = valor
        j = fila.index(str(valor))
        if(i%2!=0 and j%2!=0): tmp -= 3
        else:
                if(i%2==0): tmp += 1
                if(j%2==0): tmp += 2
        if j < b-1:
            print(tmp, end=" ") # 1
        else: 
            print(tmp)
